from typing import Awaitable, TypeVar

from typing_aliases import NormalError
from wraps.result import Error, Ok, Result

__all__ = ("NormalResult", "normal_result_of")

T = TypeVar("T")

NormalResult = Result[T, NormalError]


async def normal_result_of(awaitable: Awaitable[T]) -> NormalResult[T]:
    try:
        value = await awaitable

    except NormalError as error:
        return Error(error)

    else:
        return Ok(value)
