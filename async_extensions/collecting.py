from typing import Any, Awaitable, List, Tuple, TypeVar, overload

from anyio import create_task_group
from typing_aliases import AnyIterable, DynamicTuple, EmptyTuple

from async_extensions.completion import as_completed_tagged_results
from async_extensions.results import NormalResult
from async_extensions.tagged import by_tag

__all__ = ("collect", "collect_results", "collect_iterable", "collect_iterable_results")

A = TypeVar("A")
B = TypeVar("B")
C = TypeVar("C")
D = TypeVar("D")
E = TypeVar("E")
F = TypeVar("F")
G = TypeVar("G")
H = TypeVar("H")

T = TypeVar("T")


@overload
async def collect_results() -> EmptyTuple: ...


@overload
async def collect_results(__awaitable_a: Awaitable[A]) -> Tuple[NormalResult[A]]: ...


@overload
async def collect_results(
    __awaitable_a: Awaitable[A], __awaitable_b: Awaitable[B]
) -> Tuple[NormalResult[A], NormalResult[B]]: ...


@overload
async def collect_results(
    __awaitable_a: Awaitable[A], __awaitable_b: Awaitable[B], __awaitable_c: Awaitable[C]
) -> Tuple[NormalResult[A], NormalResult[B], NormalResult[C]]: ...


@overload
async def collect_results(
    __awaitable_a: Awaitable[A],
    __awaitable_b: Awaitable[B],
    __awaitable_c: Awaitable[C],
    __awaitable_d: Awaitable[D],
) -> Tuple[NormalResult[A], NormalResult[B], NormalResult[C], NormalResult[D]]: ...


@overload
async def collect_results(
    __awaitable_a: Awaitable[A],
    __awaitable_b: Awaitable[B],
    __awaitable_c: Awaitable[C],
    __awaitable_d: Awaitable[D],
    __awaitable_e: Awaitable[E],
) -> Tuple[NormalResult[A], NormalResult[B], NormalResult[C], NormalResult[D], NormalResult[E]]: ...


@overload
async def collect_results(
    __awaitable_a: Awaitable[A],
    __awaitable_b: Awaitable[B],
    __awaitable_c: Awaitable[C],
    __awaitable_d: Awaitable[D],
    __awaitable_e: Awaitable[E],
    __awaitable_f: Awaitable[F],
) -> Tuple[
    NormalResult[A],
    NormalResult[B],
    NormalResult[C],
    NormalResult[D],
    NormalResult[E],
    NormalResult[F],
]: ...


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
    NormalResult[A],
    NormalResult[B],
    NormalResult[C],
    NormalResult[D],
    NormalResult[E],
    NormalResult[F],
    NormalResult[G],
]: ...


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
    NormalResult[A],
    NormalResult[B],
    NormalResult[C],
    NormalResult[D],
    NormalResult[E],
    NormalResult[F],
    NormalResult[G],
    NormalResult[H],
]: ...


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
    __awaitable_n: Awaitable[Any],
    *awaitables: Awaitable[Any],
) -> DynamicTuple[NormalResult[Any]]: ...


async def collect_results(*awaitables: Awaitable[Any]) -> DynamicTuple[NormalResult[Any]]:
    return tuple(await collect_iterable_results(awaitables))


async def collect_iterable_results(awaitables: AnyIterable[Awaitable[T]]) -> List[NormalResult[T]]:
    async with create_task_group() as task_group:
        tagged_results = [
            tagged_result
            async for tagged_result in as_completed_tagged_results(task_group, awaitables)
        ]

    tagged_results.sort(key=by_tag)

    return [tagged_result.result for tagged_result in tagged_results]


@overload
async def collect() -> EmptyTuple: ...  # pragma: overload


@overload
async def collect(__awaitable_a: Awaitable[A]) -> Tuple[A]: ...  # pragma: overload


@overload
async def collect(
    __awaitable_a: Awaitable[A], __awaitable_b: Awaitable[B]
) -> Tuple[A, B]: ...  # pragma: overload


@overload
async def collect(
    __awaitable_a: Awaitable[A], __awaitable_b: Awaitable[B], __awaitable_c: Awaitable[C]
) -> Tuple[A, B, C]: ...  # pragma: overload


@overload
async def collect(
    __awaitable_a: Awaitable[A],
    __awaitable_b: Awaitable[B],
    __awaitable_c: Awaitable[C],
    __awaitable_d: Awaitable[D],
) -> Tuple[A, B, C, D]: ...  # pragma: overload


@overload
async def collect(
    __awaitable_a: Awaitable[A],
    __awaitable_b: Awaitable[B],
    __awaitable_c: Awaitable[C],
    __awaitable_d: Awaitable[D],
    __awaitable_e: Awaitable[E],
) -> Tuple[A, B, C, D, E]: ...  # pragma: overload


@overload
async def collect(
    __awaitable_a: Awaitable[A],
    __awaitable_b: Awaitable[B],
    __awaitable_c: Awaitable[C],
    __awaitable_d: Awaitable[D],
    __awaitable_e: Awaitable[E],
    __awaitable_f: Awaitable[F],
) -> Tuple[A, B, C, D, E, F]: ...  # pragma: overload


@overload
async def collect(
    __awaitable_a: Awaitable[A],
    __awaitable_b: Awaitable[B],
    __awaitable_c: Awaitable[C],
    __awaitable_d: Awaitable[D],
    __awaitable_e: Awaitable[E],
    __awaitable_f: Awaitable[F],
    __awaitable_g: Awaitable[G],
) -> Tuple[A, B, C, D, E, F, G]: ...  # pragma: overload


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
) -> Tuple[A, B, C, D, E, F, G, H]: ...  # pragma: overload


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
) -> DynamicTuple[Any]: ...  # pragma: overload


async def collect(*awaitables: Awaitable[Any]) -> DynamicTuple[Any]:
    return tuple(await collect_iterable(awaitables))


async def collect_iterable(awaitables: AnyIterable[Awaitable[T]]) -> List[T]:
    return [result.raising() for result in await collect_iterable_results(awaitables)]
