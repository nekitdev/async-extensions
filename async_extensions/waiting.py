from typing import Awaitable, Optional, TypeVar

from anyio import fail_after, move_on_after
from wraps.option import NULL, Option, Some
from wraps.wraps import wrap_future_option

from async_extensions.constants import DEFAULT_SHIELD

__all__ = ("fail_after", "move_on_after", "wait_for")

T = TypeVar("T")


@wrap_future_option
async def wait_for(
    awaitable: Awaitable[T], timeout: Optional[float], *, shield: bool = DEFAULT_SHIELD
) -> Option[T]:
    with move_on_after(timeout, shield=shield):
        value = await awaitable

        return Some(value)

    return NULL
