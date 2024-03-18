# Changelog

<!-- changelogging: start -->

## 3.1.0 (2024-03-19)

### Features

- Added `async_next_any_iter`.

## 3.0.1 (2024-03-18)

### Changes

- Type names are now used instead of instance representations in errors raised by
  `async_iter`, `async_next` and `async_iter_any_iter`.

## 3.0.0 (2024-03-18)

### Features

- Added `as_completed`, `as_completed_results` and `as_completed_tagged_results`.
- Added `NormalResult[T] = Result[T, NormalError]`.
- Added `normal_result_of` to catch errors and wrap them.
- Added `TaggedResult[T, E]` for results tagged with `int`.
- Added `NormalTaggedResult[T] = TaggedResult[T, NormalError]`.
- Added `normal_tagged_result_of`, akin to `normal_result_of` but attaching some tag.
- Added `async_iter_unchecked` and `async_next_unchecked` which do not check whether the
  argument has the appropriate type; also added `async_iter_any_iter` to convert `AnyIterable[T]`
  into `AsyncIterator[T]`.
- Exported `DEFAULT_BACKEND` and `DEFAULT_SHIELD`.
- Exported `Process` and `async_close`.

### Changes

- Renamed `MemorySendChannel` and `MemoryReceiveChannel` to
  `MemorySendStream` and `MemoryReceiveStream` respectively.

## 2.0.2 (2024-02-26)

No significant changes.

## 2.0.1 (2024-02-25)

No significant changes.

## 2.0.0 (2024-02-24)

### Internal

- Renamed most of the modules.
- Migrated to AnyIO 4.
- Dropped Python 3.7 support.

## 1.4.1 (2023-05-24)

### Fixes

- Fixed `final` import to be compatible with Python 3.7.

## 1.4.0 (2023-05-21)

### Internal

- Migrated to using `typing-aliases` library.

## 1.3.0 (2023-05-18)

### Features

- Added `TaskGroup` type to exports.

## 1.2.3 (2023-05-07)

### Fixes

- Fixed `async_next` wrongly handling `StopIteration` instead of `StopAsyncIteration`.

## 1.2.2 (2023-04-07)

### Fixes

- Fixed `async_iter` being an async function.

## 1.2.1 (2023-02-07)

### Changes

- Updated `run` function, now accepting `awaitable` and `backend` arguments.

## 1.2.0 (2023-01-29)

### Changes

- `attrs` and `iters` libraries are not used anymore.

## 1.1.1 (2023-01-29)

### Features

- Added `py.typed` marker.

## 1.1.0 (2023-01-29)

### Changes

- Updated `collect_results` and `collect_iterable_results` to *not* use `Result[T, E]` from `wraps`.

## 1.0.0 (2023-01-29)

Initial release.
