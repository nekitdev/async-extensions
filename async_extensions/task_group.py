from typing import TYPE_CHECKING

from anyio import create_task_group
from typing_aliases import AnyType

__all__ = ("TaskGroup", "create_task_group")

if TYPE_CHECKING:
    TaskGroup = type(create_task_group())

else:
    TaskGroup = AnyType
