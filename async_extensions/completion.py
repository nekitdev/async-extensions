from typing import AsyncIterator, Awaitable, TypeVar

from typing_aliases import AnyIterable

from async_extensions.channels import MemoryChannelFactory
from async_extensions.results import NormalResult
from async_extensions.standard import async_iter_any_iter
from async_extensions.tagged import (
    NormalTaggedResult,
    receive_normal_tagged_result,
    send_normal_tagged_result_of,
)
from async_extensions.task_groups import TaskGroup

__all__ = (
    "as_completed_tagged_results",
    "as_completed_results",
    "as_completed",
)

T = TypeVar("T")


async def as_completed_tagged_results(
    task_group: TaskGroup, awaitables: AnyIterable[Awaitable[T]]
) -> AsyncIterator[NormalTaggedResult[T]]:
    sender, receiver = MemoryChannelFactory[NormalTaggedResult[T]]().channel

    length = 0

    async for awaitable in async_iter_any_iter(awaitables):
        task_group.start_soon(send_normal_tagged_result_of, awaitable, length, sender)

        length += 1

    for _ in range(length):
        yield await receive_normal_tagged_result(receiver)


async def as_completed_results(
    task_group: TaskGroup, awaitables: AnyIterable[Awaitable[T]]
) -> AsyncIterator[NormalResult[T]]:
    async for tagged_result in as_completed_tagged_results(task_group, awaitables):
        yield tagged_result.result


async def as_completed(
    task_group: TaskGroup, awaitables: AnyIterable[Awaitable[T]]
) -> AsyncIterator[T]:
    async for result in as_completed_results(task_group, awaitables):
        yield result.raising()
