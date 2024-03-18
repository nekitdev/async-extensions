from typing import Any, AsyncIterable, AsyncIterator, Iterable, TypeVar, Union, overload

from named import get_type_name
from typing_aliases import AnyIterable, is_async_iterable, is_instance, is_iterable

from async_extensions.types import no_default

__all__ = (
    "async_iter",
    "async_iter_unchecked",
    "async_next",
    "async_next_unchecked",
    "iter_to_async_iter",
    "async_iter_any_iter",
)

NOT_ASYNC_ITERABLE = "`{}` instance is not an async iterable"
not_async_iterable = NOT_ASYNC_ITERABLE.format

NOT_ASYNC_ITERATOR = "`{}` instance is not an async iterator"
not_async_iterator = NOT_ASYNC_ITERATOR.format

T = TypeVar("T")
U = TypeVar("U")


def async_iter(async_iterable: AsyncIterable[T]) -> AsyncIterator[T]:
    if is_instance(async_iterable, AsyncIterable):
        return async_iter_unchecked(async_iterable)

    raise TypeError(not_async_iterable(get_type_name(async_iterable)))


def async_iter_unchecked(async_iterable: AsyncIterable[T]) -> AsyncIterator[T]:
    return async_iterable.__aiter__()


@overload
async def async_next(async_iterator: AsyncIterator[T]) -> T: ...


@overload
async def async_next(async_iterator: AsyncIterator[T], default: U) -> Union[T, U]: ...


async def async_next(async_iterator: AsyncIterator[Any], default: Any = no_default) -> Any:
    if is_instance(async_iterator, AsyncIterator):
        return await async_next_unchecked(async_iterator)

    raise TypeError(not_async_iterator(get_type_name(async_iterator)))


@overload
async def async_next_unchecked(async_iterator: AsyncIterator[T]) -> T: ...


@overload
async def async_next_unchecked(async_iterator: AsyncIterator[T], default: U) -> Union[T, U]: ...


async def async_next_unchecked(
    async_iterator: AsyncIterator[Any], default: Any = no_default
) -> Any:
    try:
        return await async_iterator.__anext__()

    except StopAsyncIteration:
        if default is no_default:
            raise

        return default


async def iter_to_async_iter(iterable: Iterable[T]) -> AsyncIterator[T]:
    for item in iterable:
        yield item


NOT_ANY_ITERABLE = "`{}` instance is neither an async iterable nor an iterable"
not_any_iterable = NOT_ANY_ITERABLE.format


def async_iter_any_iter(iterable: AnyIterable[T]) -> AsyncIterator[T]:
    if is_iterable(iterable):
        return iter_to_async_iter(iterable)

    if is_async_iterable(iterable):
        return async_iter_unchecked(iterable)

    raise TypeError(not_any_iterable(get_type_name(iterable)))
