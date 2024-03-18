from typing import Awaitable, Generic, TypeVar, final

from attrs import frozen
from typing_aliases import NormalError
from wraps.result import Result

from async_extensions.channels import MemoryReceiveStream, MemorySendStream
from async_extensions.results import normal_result_of

__all__ = ("TaggedResult", "NormalTaggedResult", "normal_tagged_result_of")

T = TypeVar("T", covariant=True)
E = TypeVar("E", covariant=True)


@final
@frozen()
class TaggedResult(Generic[T, E]):
    result: Result[T, E]
    tag: int


NormalTaggedResult = TaggedResult[T, NormalError]


def by_tag(tagged_result: TaggedResult[T, E]) -> int:
    return tagged_result.tag


async def normal_tagged_result_of(awaitable: Awaitable[T], tag: int) -> NormalTaggedResult[T]:
    return TaggedResult(await normal_result_of(awaitable), tag)


async def send_normal_tagged_result_of(
    awaitable: Awaitable[T], tag: int, sender: MemorySendStream[NormalTaggedResult[T]]
) -> None:
    await sender.send(await normal_tagged_result_of(awaitable, tag))


async def receive_normal_tagged_result(
    receiver: MemoryReceiveStream[NormalTaggedResult[T]],
) -> NormalTaggedResult[T]:
    return await receiver.receive()
