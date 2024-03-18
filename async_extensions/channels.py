from typing import Generic, Optional, Tuple, TypeVar

from anyio import create_memory_object_stream as create_memory_channel
from anyio.streams.memory import MemoryObjectReceiveStream as MemoryReceiveStream
from anyio.streams.memory import MemoryObjectSendStream as MemorySendStream

from async_extensions.defaults import INFINITY

__all__ = (
    "MemoryChannel",
    "MemoryChannelFactory",
    "MemorySendStream",
    "MemoryReceiveStream",
)

T = TypeVar("T")

MemoryChannel = Tuple[MemorySendStream[T], MemoryReceiveStream[T]]


class MemoryChannelFactory(Generic[T]):
    def __init__(self, max_size: Optional[int] = None) -> None:
        self._sender, self._receiver = create_memory_channel[T](
            INFINITY if max_size is None else max_size
        )

    @property
    def sender(self) -> MemorySendStream[T]:
        return self._sender

    @property
    def receiver(self) -> MemoryReceiveStream[T]:
        return self._receiver

    @property
    def channel(self) -> MemoryChannel[T]:
        return (self.sender, self.receiver)
