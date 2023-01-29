from typing import Awaitable, TypeVar

from anyio import CancelScope

from async_extensions.constants import DEFAULT_SHIELD

__all__ = ("CancelScope", "create_cancel_scope")


def create_cancel_scope(*, shield: bool = DEFAULT_SHIELD) -> CancelScope:
    return CancelScope(shield=shield)


T = TypeVar("T")


async def shield(awaitable: Awaitable[T]) -> T:
    with create_cancel_scope(shield=True):
        return await awaitable
