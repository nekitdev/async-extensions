from builtins import isinstance as is_instance
from typing import Any, AsyncIterable, Iterable, Tuple, TypeVar, Union

from typing_extensions import TypeAlias, TypeGuard

__all__ = (
    "AnyException",
    "AnyIterable",
    "DynamicTuple",
    "EmptyTuple",
    "is_error",
    "is_async_iterable",
    "is_iterable",
    "is_instance",
)

AnyException: TypeAlias = BaseException

T = TypeVar("T")

AnyIterable = Union[AsyncIterable[T], Iterable[T]]

DynamicTuple = Tuple[T, ...]

EmptyTuple = Tuple[()]


def is_error(item: Any) -> TypeGuard[AnyException]:
    return is_instance(item, AnyException)


def is_async_iterable(async_iterable: AnyIterable[T]) -> TypeGuard[AsyncIterable[T]]:
    return is_instance(async_iterable, AsyncIterable)


def is_iterable(iterable: AnyIterable[T]) -> TypeGuard[Iterable[T]]:
    return is_instance(iterable, Iterable)
