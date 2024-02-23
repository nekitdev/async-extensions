"""Asynchronous extensions."""

__description__ = "Asynchronous extensions."
__url__ = "https://github.com/nekitdev/async-extensions"

__title__ = "async_extensions"
__author__ = "nekitdev"
__license__ = "MIT"
__version__ = "2.0.0"

from async_extensions.blocking import run_blocking_in_process, run_blocking_in_thread
from async_extensions.cancellation import CancelScope, create_cancel_scope, shield
from async_extensions.channels import (
    MemoryChannel,
    MemoryChannelFactory,
    MemoryReceiveChannel,
    MemorySendChannel,
)
from async_extensions.collecting import (
    collect,
    collect_iterable,
    collect_iterable_results,
    collect_results,
)
from async_extensions.current import current_async_library
from async_extensions.errors import AsyncLibraryNotFoundError
from async_extensions.files import AsyncFile, open_file, wrap_file
from async_extensions.from_thread import BlockingPortal, check_cancelled, start_blocking_portal
from async_extensions.low_level import (
    cancel_shielded_checkpoint,
    checkpoint,
    checkpoint_if_cancelled,
)
from async_extensions.paths import Path
from async_extensions.processes import open_process, run_process
from async_extensions.resources import AsyncResource, async_close_forcefully
from async_extensions.runners import run
from async_extensions.signals import open_signal_receiver
from async_extensions.sleeping import sleep, sleep_forever
from async_extensions.standard import async_iter, async_next, iter_to_async_iter
from async_extensions.synchronization import CapacityLimiter, Condition, Event, Lock, Semaphore
from async_extensions.task_groups import TaskGroup, create_task_group
from async_extensions.task_statuses import TASK_STATUS_IGNORED, TaskStatus
from async_extensions.waiting import fail_after, move_on_after, wait_for

__all__ = (
    # blocking
    "run_blocking_in_process",
    "run_blocking_in_thread",
    # cancellation
    "CancelScope",
    "create_cancel_scope",
    "shield",
    # channels
    "MemoryChannel",
    "MemoryChannelFactory",
    "MemoryReceiveChannel",
    "MemorySendChannel",
    # collecting
    "collect",
    "collect_iterable",
    "collect_iterable_results",
    "collect_results",
    # current
    "current_async_library",
    # errors
    "AsyncLibraryNotFoundError",
    # files
    "AsyncFile",
    "open_file",
    "wrap_file",
    # from thread
    "BlockingPortal",
    "check_cancelled",
    "start_blocking_portal",
    # low-level
    "cancel_shielded_checkpoint",
    "checkpoint",
    "checkpoint_if_cancelled",
    # paths
    "Path",
    # processes
    "open_process",
    "run_process",
    # resources
    "AsyncResource",
    "async_close_forcefully",
    # runners
    "run",
    # signals
    "open_signal_receiver",
    # sleeping
    "sleep",
    "sleep_forever",
    # standard
    "async_iter",
    "async_next",
    "iter_to_async_iter",
    # synchronization
    "CapacityLimiter",
    "Condition",
    "Event",
    "Lock",
    "Semaphore",
    # task groups
    "TaskGroup",
    "create_task_group",
    # task statuses
    "TASK_STATUS_IGNORED",
    "TaskStatus",
    # waiting
    "fail_after",
    "move_on_after",
    "wait_for",
)
