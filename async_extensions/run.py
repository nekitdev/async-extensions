from functools import partial
from typing import Awaitable, Callable, TypeVar

from anyio import run as run_standard
from typing_extensions import ParamSpec

__all__ = ("run",)

P = ParamSpec("P")
T = TypeVar("T")

async def awaiting(awaitable: Awaitable[T]) -> T:
    return await awaitable


def run(function: Callable[P, Awaitable[T]], *args: P.args, **kwargs: P.kwargs) -> T:
    return run_standard(awaiting(partial(function, *args, **kwargs)))  # type: ignore
