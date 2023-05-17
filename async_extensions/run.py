from typing import Awaitable, TypeVar

from anyio import run as run_standard

from async_extensions.constants import DEFAULT_BACKEND

__all__ = ("awaiting", "run")

T = TypeVar("T")


async def awaiting(awaitable: Awaitable[T]) -> T:
    return await awaitable


def run(awaitable: Awaitable[T], backend: str = DEFAULT_BACKEND) -> T:
    return run_standard(awaiting, awaitable, backend=backend)
