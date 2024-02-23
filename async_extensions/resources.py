from anyio import aclose_forcefully as async_close_forcefully
from anyio.abc import AsyncResource

__all__ = (
    "AsyncResource",
    "async_close",
    "async_close_forcefully",
)


async def async_close(resource: AsyncResource) -> None:
    await resource.aclose()
