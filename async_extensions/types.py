from typing import TypeVar, Union

from solus import Singleton
from typing_extensions import TypeIs


class NoDefault(Singleton):
    pass


T = TypeVar("T")

NoDefaultOr = Union[NoDefault, T]

no_default = NoDefault()


def is_no_default(item: NoDefaultOr[T]) -> TypeIs[NoDefault]:
    return item is no_default
