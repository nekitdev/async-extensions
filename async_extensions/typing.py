from builtins import isinstance as is_instance
from typing import Any, AsyncIterable, Iterable, Type, TypeVar, Union

from typing_extensions import TypeGuard

__all__ = (
    "AnyType",
    "AnyIterable",
    "is_async_iterable",
    "is_iterable",
    "is_instance",
)

T = TypeVar("T")

AnyType = Type[Any]

AnyIterable = Union[AsyncIterable[T], Iterable[T]]


def is_async_iterable(async_iterable: AnyIterable[T]) -> TypeGuard[AsyncIterable[T]]:
    return is_instance(async_iterable, AsyncIterable)


def is_iterable(iterable: AnyIterable[T]) -> TypeGuard[Iterable[T]]:
    return is_instance(iterable, Iterable)
