from abc import abstractmethod as required
from types import TracebackType as Traceback
from typing import AsyncContextManager, Awaitable, Optional, Type, TypeVar

from attrs import frozen
from typing_aliases import AnyError
from typing_extensions import Protocol, final, runtime_checkable

from async_extensions.cancel import create_cancel_scope

__all__ = (
    "AsyncCloseable",
    "AsyncClosing",
    "async_close",
    "async_close_forcefully",
    "async_closing",
)


@runtime_checkable
class AsyncCloseable(Protocol):
    """Represents resources implementing asynchronous closing."""

    @required
    def aclose(self) -> Awaitable[None]:
        """Close the resource asynchronously."""
        ...


async def async_close(resource: AsyncCloseable) -> None:
    """Close the resource asynchronously."""
    await resource.aclose()


async def async_close_forcefully(resource: AsyncCloseable) -> None:
    """Close the resource asynchronously and forcefully."""
    with create_cancel_scope() as scope:
        scope.cancel()

        await async_close(resource)


R = TypeVar("R", bound=AsyncCloseable)
E = TypeVar("E", bound=AnyError)


@final
@frozen()
class AsyncClosing(AsyncContextManager[R]):
    resource: R

    async def __aenter__(self) -> R:
        return self.resource

    async def __aexit__(
        self,
        error_type: Optional[Type[E]],
        error: Optional[E],
        traceback: Optional[Traceback],
    ) -> None:
        await async_close(self.resource)


def async_closing(resource: R) -> AsyncClosing[R]:
    return AsyncClosing(resource)
