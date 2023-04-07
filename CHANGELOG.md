# Changelog

<!-- changelogging: start -->

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
