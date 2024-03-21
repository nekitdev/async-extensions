from typing import Any

from solus import Singleton
from typing_extensions import TypeIs


class NoDefault(Singleton):
    pass


no_default = NoDefault()


def is_no_default(item: Any) -> TypeIs[NoDefault]:
    return item is no_default
