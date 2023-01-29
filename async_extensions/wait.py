from typing import Awaitable, Optional, TypeVar, Union

from anyio import fail_after, move_on_after

from async_extensions.constants import DEFAULT_SHIELD

__all__ = ("fail_after", "move_on_after", "wait_for", "wait_for_or_else")

T = TypeVar("T")


async def wait_for(
    awaitable: Awaitable[T], timeout: Optional[float], *, shield: bool = DEFAULT_SHIELD
) -> T:
    with fail_after(timeout, shield=shield):
        return await awaitable


U = TypeVar("U")


async def wait_for_or_else(
    awaitable: Awaitable[T],
    default: U,
    timeout: Optional[float],
    *,
    shield: bool = False,
) -> Union[T, U]:
    with move_on_after(timeout, shield=shield):
        return await awaitable

    return default  # type: ignore
