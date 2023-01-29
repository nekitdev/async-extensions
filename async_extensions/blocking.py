from functools import partial
from typing import Callable, TypeVar

from anyio.to_process import run_sync as standard_run_blocking_in_process
from anyio.to_thread import run_sync as standard_run_blocking_in_thread
from typing_extensions import ParamSpec

__all__ = ("run_blocking_in_thread", "run_blocking_in_process")

P = ParamSpec("P")
T = TypeVar("T")


async def run_blocking_in_thread(function: Callable[P, T], *args: P.args, **kwargs: P.kwargs) -> T:
    return await standard_run_blocking_in_thread(partial(function, *args, **kwargs))


async def run_blocking_in_process(function: Callable[P, T], *args: P.args, **kwargs: P.kwargs) -> T:
    return await standard_run_blocking_in_process(partial(function, *args, **kwargs))
