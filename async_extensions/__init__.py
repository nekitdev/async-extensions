"""Asynchronous extensions."""

__description__ = "Asynchronous extensions."
__url__ = "https://github.com/nekitdev/async-extensions"

__title__ = "async_extensions"
__author__ = "nekitdev"
__license__ = "MIT"
__version__ = "1.4.1"

from async_extensions.blocking import run_blocking_in_process, run_blocking_in_thread
from async_extensions.cancel import CancelScope, create_cancel_scope, shield
from async_extensions.channel import (
    MemoryChannel,
    MemoryChannelFactory,
    MemoryReceiveChannel,
    MemorySendChannel,
)
from async_extensions.close import (
    AsyncCloseable,
    AsyncClosing,
    async_close,
    async_close_forcefully,
    async_closing,
)
from async_extensions.collect import (
    collect,
    collect_iterable,
    collect_iterable_results,
    collect_results,
)
from async_extensions.current import current_async_library
from async_extensions.errors import AsyncLibraryNotFoundError
from async_extensions.file import AsyncFile, open_file, wrap_file
from async_extensions.low_level import (
    cancel_shielded_checkpoint,
    checkpoint,
    checkpoint_if_cancelled,
)
from async_extensions.path import Path
from async_extensions.process import open_process, run_process
from async_extensions.run import run
from async_extensions.signal import open_signal_receiver
from async_extensions.sleep import sleep, sleep_forever
from async_extensions.standard import async_iter, async_next, iter_to_async_iter
from async_extensions.synchronization import CapacityLimiter, Condition, Event, Lock, Semaphore
from async_extensions.task_group import TaskGroup, create_task_group
from async_extensions.wait import fail_after, move_on_after, wait_for, wait_for_or_else

__all__ = (
    # blocking
    "run_blocking_in_process",
    "run_blocking_in_thread",
    # cancel
    "CancelScope",
    "create_cancel_scope",
    "shield",
    # channel
    "MemoryChannel",
    "MemoryChannelFactory",
    "MemoryReceiveChannel",
    "MemorySendChannel",
    # close
    "AsyncCloseable",
    "AsyncClosing",
    "async_close",
    "async_close_forcefully",
    "async_closing",
    # collect
    "collect",
    "collect_iterable",
    "collect_iterable_results",
    "collect_results",
    # current
    "current_async_library",
    # errors
    "AsyncLibraryNotFoundError",
    # file
    "AsyncFile",
    "open_file",
    "wrap_file",
    # low-level
    "cancel_shielded_checkpoint",
    "checkpoint",
    "checkpoint_if_cancelled",
    # path
    "Path",
    # process
    "open_process",
    "run_process",
    # run
    "run",
    # signal
    "open_signal_receiver",
    # sleep
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
    # task group
    "TaskGroup",
    "create_task_group",
    # wait
    "fail_after",
    "move_on_after",
    "wait_for",
    "wait_for_or_else",
)
