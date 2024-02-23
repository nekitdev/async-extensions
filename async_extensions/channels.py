from typing import Generic, Optional, Tuple, TypeVar, cast

from anyio import create_memory_object_stream as create_memory_channel
from anyio.streams.memory import MemoryObjectReceiveStream as MemoryReceiveChannel
from anyio.streams.memory import MemoryObjectSendStream as MemorySendChannel

from async_extensions.constants import INFINITY

__all__ = (
    "MemoryChannel",
    "MemoryChannelFactory",
    "MemorySendChannel",
    "MemoryReceiveChannel",
)

T = TypeVar("T")

MemoryChannel = Tuple[MemorySendChannel[T], MemoryReceiveChannel[T]]


class MemoryChannelFactory(Generic[T]):
    def __init__(self, max_size: Optional[int] = None) -> None:
        self._sender, self._receiver = cast(
            MemoryChannel[T],
            create_memory_channel(INFINITY if max_size is None else max_size),
        )

    @property
    def sender(self) -> MemorySendChannel[T]:
        return self._sender

    @property
    def receiver(self) -> MemoryReceiveChannel[T]:
        return self._receiver

    @property
    def channel(self) -> MemoryChannel[T]:
        return (self.sender, self.receiver)

    def execute(self) -> MemoryChannel[T]:
        return self.channel
