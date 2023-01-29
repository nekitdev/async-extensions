from abc import abstractmethod as required
from types import TracebackType as Traceback
from typing import Awaitable, Generic, Optional, Type, TypeVar, overload

from typing_extensions import Protocol, runtime_checkable

from async_extensions.cancel import create_cancel_scope
from async_extensions.typing import AnyException

__all__ = (
    "AsyncCloseable", "AsyncClosing", "async_close", "async_close_forcefully", "async_closing"
)


@runtime_checkable
class AsyncCloseable(Protocol):
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
E = TypeVar("E", bound=AnyException)


class AsyncClosing(Generic[R]):
    def __init__(self, resource: R) -> None:
        self._resource = resource

    @property
    def resource(self) -> R:
        return self._resource

    async def __aenter__(self) -> R:
        return self.resource

    @overload
    async def __aexit__(
        self, error_type: Type[E], error: E, traceback: Traceback
    ) -> None:
        ...

    @overload
    async def __aexit__(self, error_type: None, error: None, traceback: None) -> None:
        ...

    async def __aexit__(
        self,
        error_type: Optional[Type[E]],
        error: Optional[E],
        traceback: Optional[Traceback],
    ) -> None:
        await async_close(self.resource)


async_closing = AsyncClosing
