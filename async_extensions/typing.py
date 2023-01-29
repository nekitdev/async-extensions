from builtins import isinstance as is_instance
from typing import Any, AsyncIterable, Iterable, Tuple, TypeVar, Union

from typing_extensions import TypeAlias, TypeGuard

__all__ = ("AnyException", "AnyIterable", "DynamicTuple", "EmptyTuple", "is_error", "is_instance")

AnyException: TypeAlias = BaseException

T = TypeVar("T")

AnyIterable = Union[AsyncIterable[T], Iterable[T]]

DynamicTuple = Tuple[T, ...]

EmptyTuple = Tuple[()]


def is_error(item: Any) -> TypeGuard[AnyException]:
    return is_instance(item, AnyException)
