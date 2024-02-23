from typing import Awaitable, TypeVar

from anyio import CancelScope
from anyio import get_cancelled_exc_class as get_cancelled_error_type

from async_extensions.constants import DEFAULT_SHIELD

__all__ = ("CancelScope", "create_cancel_scope", "get_cancelled_error_type")


def create_cancel_scope(*, shield: bool = DEFAULT_SHIELD) -> CancelScope:
    return CancelScope(shield=shield)


T = TypeVar("T")


async def shield(awaitable: Awaitable[T]) -> T:
    with create_cancel_scope(shield=True):
        return await awaitable
