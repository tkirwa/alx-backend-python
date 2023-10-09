# Python Async (Python | Back-end)

This repository contains solutions and explanations for the tasks related to asynchronous programming in Python. The tasks cover essential concepts such as async and await syntax, executing asynchronous coroutines, running concurrent coroutines, measuring runtime, and creating asyncio tasks.

## Task 0: The Basics of Async

### Description

Write an asynchronous coroutine named `wait_random` that takes an integer argument `max_delay` (default value of 10) and waits for a random delay between 0 and `max_delay` (inclusive) seconds before returning the delay.

### Usage

```python
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random

print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
print(asyncio.run(wait_random(15)))
```

## Task 1: Execute Multiple Coroutines Concurrently

### Description

Write an async function called `wait_n` that takes two integer arguments, `n` and `max_delay`. This function will spawn `wait_random` `n` times with the specified `max_delay`. It should return a list of all the delays (float values) in ascending order, without using `sort()` because of concurrency.

### Usage

```python
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n

print(asyncio.run(wait_n(5, 5)))
print(asyncio.run(wait_n(10, 7)))
print(asyncio.run(wait_n(10, 0)))
```

## Task 2: Measure the Runtime

### Description

Create a `measure_time` function that measures the total execution time for `wait_n(n, max_delay)` with integer arguments `n` and `max_delay`. The function returns `total_time / n` as a float.

### Usage

```python
n = 5
max_delay = 9
print(measure_time(n, max_delay))
```

## Task 3: Tasks

### Description

Write a function `task_wait_random` that takes an integer `max_delay` and returns an `asyncio.Task`.

### Usage

```python
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random

async def test(max_delay: int) -> float:
    task = task_wait_random(max_delay)
    await task
    print(task.__class__)

asyncio.run(test(5))
```

## Task 4: Tasks (Part 2)

### Description

Take the code from `wait_n` and alter it into a new function `task_wait_n`. The code is nearly identical to `wait_n`, except `task_wait_random` is being called.

### Usage

```python
import asyncio
task_wait_n = __import__('4-tasks').task_wait_n

n = 5
max_delay = 6
print(asyncio.run(task_wait_n(n, max_delay)))
```

## Repository Information

- GitHub Repository: [alx-backend-python](https://github.com/tkirwa/alx-backend-python)
- Directory: `0x01-python_async_function`
- Files:
  - `0-basic_async_syntax.py`
  - `1-concurrent_coroutines.py`
  - `2-measure_runtime.py`
  - `3-tasks.py`
  - `4-tasks.py`
