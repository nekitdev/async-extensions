from typing import (
    Any, AsyncIterable, AsyncIterator, Awaitable, List, Tuple, TypeVar, Union, overload
)

from async_extensions.standard import iter_to_async_iter
from async_extensions.task_group import create_task_group
from async_extensions.typing import (
    AnyException, AnyIterable, DynamicTuple, EmptyTuple, is_async_iterable, is_error, is_iterable
)

__all__ = ("collect", "collect_results", "collect_iterable", "collect_iterable_results")

T = TypeVar("T")
ET = TypeVar("ET", bound=AnyException)


Result = Union[T, ET]
TaggedResult = Tuple[int, Result[T, ET]]

AnyTaggedResult = TaggedResult[T, AnyException]
AnyResult = Result[T, AnyException]


async def append_tagged_result(
    awaitable: Awaitable[T],
    tag: int,
    results: List[AnyTaggedResult[T]],
) -> None:
    result: AnyResult[T]

    try:
        result = await awaitable

    except AnyException as error:
        result = error

    results.append((tag, result))


def by_tag(tagged_result: AnyTaggedResult[Any]) -> int:
    tag, _ = tagged_result

    return tag


def result(tagged_result: TaggedResult[T, ET]) -> Result[T, ET]:
    _, result = tagged_result

    return result


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


NOT_ANY_ITERABLE = "{} is neither an async iterable, nor an iterable"


async def tag_awaitables(
    awaitables: AsyncIterable[Awaitable[T]]
) -> AsyncIterator[Tuple[int, Awaitable[T]]]:
    tag = 0

    async for awaitable in awaitables:
        yield (tag, awaitable)

        tag += 1


async def collect_iterable_results(
    iterable: AnyIterable[Awaitable[T]],
) -> List[AnyResult[T]]:
    results: List[AnyTaggedResult[T]] = []

    awaitables: AsyncIterable[Awaitable[T]]

    if is_async_iterable(iterable):
        awaitables = iterable

    elif is_iterable(iterable):
        awaitables = iter_to_async_iter(iterable)

    else:
        raise TypeError(NOT_ANY_ITERABLE.format(repr(iterable)))

    async with create_task_group() as task_group:
        async for tag, awaitable in tag_awaitables(awaitables):
            task_group.start_soon(append_tagged_result, awaitable, tag, results)

    results.sort(key=by_tag)

    return list(map(result, results))  # type: ignore


def unwrap_error(result: AnyResult[T]) -> T:
    if is_error(result):
        raise result

    return result  # type: ignore


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
    return list(map(unwrap_error, await collect_iterable_results(iterable)))
