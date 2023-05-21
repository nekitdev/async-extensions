from typing import Any, AsyncIterable, AsyncIterator, Iterable, TypeVar, Union, overload

from typing_aliases import is_instance

from async_extensions.types import no_default

__all__ = ("async_iter", "async_next", "iter_to_async_iter")

NOT_ASYNC_ITERABLE = "{} is not an async iterable"
NOT_ASYNC_ITERATOR = "{} is not an async iterator"

T = TypeVar("T")
U = TypeVar("U")


def async_iter(async_iterable: AsyncIterable[T]) -> AsyncIterator[T]:
    if is_instance(async_iterable, AsyncIterable):
        return async_iterable.__aiter__()

    raise TypeError(NOT_ASYNC_ITERABLE.format(repr(async_iterable)))


@overload
async def async_next(async_iterator: AsyncIterator[T]) -> T:
    ...


@overload
async def async_next(async_iterator: AsyncIterator[T], default: U) -> Union[T, U]:
    ...


async def async_next(async_iterator: AsyncIterator[Any], default: Any = no_default) -> Any:
    if is_instance(async_iterator, AsyncIterator):
        try:
            return await async_iterator.__anext__()

        except StopAsyncIteration:
            if default is no_default:
                raise

            return default

    raise TypeError(NOT_ASYNC_ITERATOR.format(repr(async_iterator)))


async def iter_to_async_iter(iterable: Iterable[T]) -> AsyncIterator[T]:
    for item in iterable:
        yield item
