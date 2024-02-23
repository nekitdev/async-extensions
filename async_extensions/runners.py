from typing import Awaitable, TypeVar

from anyio import run as run_standard
from funcs.functions import awaiting

from async_extensions.constants import DEFAULT_BACKEND

__all__ = ("run",)

T = TypeVar("T")


def run(awaitable: Awaitable[T], backend: str = DEFAULT_BACKEND) -> T:
    return run_standard(awaiting, awaitable, backend=backend)  # type: ignore[arg-type]
