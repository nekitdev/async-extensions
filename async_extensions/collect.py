from typing import Any, Awaitable, Generic, List, Tuple, TypeVar, overload

from attrs import frozen
from wraps import Result, wrap_result_await

from async_extensions.task_group import create_task_group
from async_extensions.typing import AnyException, AnyIterable, DynamicTuple, EmptyTuple

__all__ = ("collect", "collect_results", "collect_iterable", "collect_iterable_results")

T = TypeVar("T")
ET = TypeVar("ET", bound=AnyException)


@frozen()
class TaggedResult(Generic[T, ET]):
    result: Result[T, ET]
    tag: int


AnyTaggedResult = TaggedResult[T, AnyException]
AnyResult = Result[T, AnyException]


@wrap_result_await
async def awaiting(awaitable: Awaitable[T]) -> T:
    return await awaitable


async def append_tagged_result(
    awaitable: Awaitable[T],
    tag: int,
    results: List[AnyTaggedResult[T]],
) -> None:
    result = await awaiting(awaitable)

    results.append(TaggedResult(result, tag))


def by_tag(tagged_result: AnyTaggedResult[Any]) -> int:
    return tagged_result.tag


def result(tagged_result: TaggedResult[T, ET]) -> Result[T, ET]:
    return tagged_result.result


A = TypeVar("A")
B = TypeVar("B")
C = TypeVar("C")
D = TypeVar("D")
E = TypeVar("E")
F = TypeVar("F")
G = TypeVar("G")
H = TypeVar("H")


@overload
async def collect_results() -> EmptyTuple:
    ...


@overload
async def collect_results(__awaitable_a: Awaitable[A]) -> Tuple[AnyResult[A]]:
    ...


@overload
async def collect_results(
    __awaitable_a: Awaitable[A], __awaitable_b: Awaitable[B]
) -> Tuple[AnyResult[A], AnyResult[B]]:
    ...


@overload
async def collect_results(
    __awaitable_a: Awaitable[A], __awaitable_b: Awaitable[B], __awaitable_c: Awaitable[C]
) -> Tuple[AnyResult[A], AnyResult[B], AnyResult[C]]:
    ...


@overload
async def collect_results(
    __awaitable_a: Awaitable[A],
    __awaitable_b: Awaitable[B],
    __awaitable_c: Awaitable[C],
    __awaitable_d: Awaitable[D],
) -> Tuple[AnyResult[A], AnyResult[B], AnyResult[C], AnyResult[D]]:
    ...


@overload
async def collect_results(
    __awaitable_a: Awaitable[A],
    __awaitable_b: Awaitable[B],
    __awaitable_c: Awaitable[C],
    __awaitable_d: Awaitable[D],
    __awaitable_e: Awaitable[E],
) -> Tuple[AnyResult[A], AnyResult[B], AnyResult[C], AnyResult[D], AnyResult[E]]:
    ...


@overload
async def collect_results(
    __awaitable_a: Awaitable[A],
    __awaitable_b: Awaitable[B],
    __awaitable_c: Awaitable[C],
    __awaitable_d: Awaitable[D],
    __awaitable_e: Awaitable[E],
    __awaitable_f: Awaitable[F],
) -> Tuple[
    AnyResult[A], AnyResult[B], AnyResult[C], AnyResult[D], AnyResult[E], AnyResult[F]
]:
    ...


@overload
async def collect_results(
    __awaitable_a: Awaitable[A],
    __awaitable_b: Awaitable[B],
    __awaitable_c: Awaitable[C],
    __awaitable_d: Awaitable[D],
    __awaitable_e: Awaitable[E],
    __awaitable_f: Awaitable[F],
    __awaitable_g: Awaitable[G],
) -> Tuple[
    AnyResult[A],
    AnyResult[B],
    AnyResult[C],
    AnyResult[D],
    AnyResult[E],
    AnyResult[F],
    AnyResult[G],
]:
    ...


@overload
async def collect_results(
    __awaitable_a: Awaitable[A],
    __awaitable_b: Awaitable[B],
    __awaitable_c: Awaitable[C],
    __awaitable_d: Awaitable[D],
    __awaitable_e: Awaitable[E],
    __awaitable_f: Awaitable[F],
    __awaitable_g: Awaitable[G],
    __awaitable_h: Awaitable[H],
) -> Tuple[
    AnyResult[A],
    AnyResult[B],
    AnyResult[C],
    AnyResult[D],
    AnyResult[E],
    AnyResult[F],
    AnyResult[G],
    AnyResult[H],
]:
    ...


@overload
async def collect_results(
    __awaitable_a: Awaitable[Any],
    __awaitable_b: Awaitable[Any],
    __awaitable_c: Awaitable[Any],
    __awaitable_d: Awaitable[Any],
    __awaitable_e: Awaitable[Any],
    __awaitable_f: Awaitable[Any],
    __awaitable_g: Awaitable[Any],
    __awaitable_h: Awaitable[Any],
    *awaitables: Awaitable[Any],
) -> DynamicTuple[AnyResult[Any]]:
    ...


async def collect_results(*awaitables: Awaitable[Any]) -> DynamicTuple[AnyResult[Any]]:
    return tuple(await collect_iterable_results(awaitables))


async def collect_iterable_results(
    iterable: AnyIterable[Awaitable[T]],
) -> List[AnyResult[T]]:
    results: List[AnyTaggedResult[T]] = []

    async with create_task_group() as task_group:
        async for tag, awaitable in async_iter(iterable).enumerate().unwrap():
            task_group.start_soon(append_tagged_result, awaitable, tag, results)

    results.sort(key=by_tag)

    return iter(results).map(result).list()  # type: ignore


def raising(result: AnyResult[T]) -> T:
    return result.raising()


@overload
async def collect() -> EmptyTuple:
    ...  # pragma: overload


@overload
async def collect(__awaitable_a: Awaitable[A]) -> Tuple[A]:
    ...  # pragma: overload


@overload
async def collect(
    __awaitable_a: Awaitable[A], __awaitable_b: Awaitable[B]
) -> Tuple[A, B]:
    ...  # pragma: overload


@overload
async def collect(
    __awaitable_a: Awaitable[A], __awaitable_b: Awaitable[B], __awaitable_c: Awaitable[C]
) -> Tuple[A, B, C]:
    ...  # pragma: overload


@overload
async def collect(
    __awaitable_a: Awaitable[A],
    __awaitable_b: Awaitable[B],
    __awaitable_c: Awaitable[C],
    __awaitable_d: Awaitable[D],
) -> Tuple[A, B, C, D]:
    ...  # pragma: overload


@overload
async def collect(
    __awaitable_a: Awaitable[A],
    __awaitable_b: Awaitable[B],
    __awaitable_c: Awaitable[C],
    __awaitable_d: Awaitable[D],
    __awaitable_e: Awaitable[E],
) -> Tuple[A, B, C, D, E]:
    ...  # pragma: overload


@overload
async def collect(
    __awaitable_a: Awaitable[A],
    __awaitable_b: Awaitable[B],
    __awaitable_c: Awaitable[C],
    __awaitable_d: Awaitable[D],
    __awaitable_e: Awaitable[E],
    __awaitable_f: Awaitable[F],
) -> Tuple[A, B, C, D, E, F]:
    ...  # pragma: overload


@overload
async def collect(
    __awaitable_a: Awaitable[A],
    __awaitable_b: Awaitable[B],
    __awaitable_c: Awaitable[C],
    __awaitable_d: Awaitable[D],
    __awaitable_e: Awaitable[E],
    __awaitable_f: Awaitable[F],
    __awaitable_g: Awaitable[G],
) -> Tuple[A, B, C, D, E, F, G]:
    ...  # pragma: overload


@overload
async def collect(
    __awaitable_a: Awaitable[A],
    __awaitable_b: Awaitable[B],
    __awaitable_c: Awaitable[C],
    __awaitable_d: Awaitable[D],
    __awaitable_e: Awaitable[E],
    __awaitable_f: Awaitable[F],
    __awaitable_g: Awaitable[G],
    __awaitable_h: Awaitable[H],
) -> Tuple[A, B, C, D, E, F, G, H]:
    ...  # pragma: overload


@overload
async def collect(
    __awaitable_a: Awaitable[Any],
    __awaitable_b: Awaitable[Any],
    __awaitable_c: Awaitable[Any],
    __awaitable_d: Awaitable[Any],
    __awaitable_e: Awaitable[Any],
    __awaitable_f: Awaitable[Any],
    __awaitable_g: Awaitable[Any],
    __awaitable_h: Awaitable[Any],
    *awaitables: Awaitable[Any],
) -> DynamicTuple[Any]:
    ...  # pragma: overload


async def collect(*awaitables: Awaitable[Any]) -> DynamicTuple[Any]:
    return tuple(await collect_iterable(awaitables))


async def collect_iterable(iterable: AnyIterable[Awaitable[T]]) -> List[T]:
    return iter(await collect_iterable_results(iterable)).map(raising).list()


# import cycle solution
from iters import async_iter, iter
