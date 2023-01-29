from builtins import isinstance as is_instance
from typing import AsyncIterable, Iterable, Tuple, TypeVar, Union

from typing_extensions import TypeAlias

__all__ = ("AnyException", "AnyIterable", "DynamicTuple", "EmptyTuple", "is_instance")

AnyException: TypeAlias = BaseException

T = TypeVar("T")

AnyIterable = Union[AsyncIterable[T], Iterable[T]]

DynamicTuple = Tuple[T, ...]

EmptyTuple = Tuple[()]
