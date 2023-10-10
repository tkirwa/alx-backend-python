# 0x02. Python - Async Comprehension

## Table of Contents
1. [Description](#description)
2. [Tasks](#tasks)
   - [Task 0: Async Generator](#task-0-async-generator)
   - [Task 1: Async Comprehensions](#task-1-async-comprehensions)
   - [Task 2: Run time for Four Parallel Comprehensions](#task-2-run-time-for-four-parallel-comprehensions)
3. [GitHub Repository](#github-repository)

---

## Description

This project consists of a series of tasks related to Python's asynchronous comprehensions. It focuses on creating and working with asynchronous generators and comprehensions. Each task is described below, along with code examples and requirements.

---

## Tasks

### Task 0: Async Generator

**Description**: Write a coroutine called `async_generator` that loops 10 times, asynchronously waits for 1 second in each iteration, and yields a random number between 0 and 10 using the `random` module.

**Requirements**:
- The coroutine should be documented with clear explanations.
- Proper type annotations should be used.
- The code should follow the specified style guidelines.

**Usage**:
```python
import asyncio

async_generator = __import__('0-async_generator').async_generator

async def print_yielded_values():
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

asyncio.run(print_yielded_values())
```

### Task 1: Async Comprehensions

**Description**: Import `async_generator` from the previous task and write a coroutine called `async_comprehension` that collects 10 random numbers using an async comprehension over `async_generator` and returns the 10 random numbers.

**Requirements**:
- The coroutine should be documented with clear explanations.
- Proper type annotations should be used.
- The code should follow the specified style guidelines.

**Usage**:
```python
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension

async def main():
    print(await async_comprehension())

asyncio.run(main())
```

### Task 2: Run time for Four Parallel Comprehensions

**Description**: Import `async_comprehension` from the previous file and write a `measure_runtime` coroutine that executes `async_comprehension` four times in parallel using `asyncio.gather`. Measure the total runtime and return it.

**Requirements**:
- The coroutine should be documented with clear explanations.
- Proper type annotations should be used.
- The code should follow the specified style guidelines.

**Usage**:
```python
import asyncio

measure_runtime = __import__('2-measure_runtime').measure_runtime

async def main():
    return await measure_runtime()

print(asyncio.run(main()))
```

---

## GitHub Repository

- **GitHub Repository**: [alx-backend-python](https://github.com/tkirwa/alx-backend-python)
- **Directory**: 0x02-python_async_comprehension

This README.md provides an overview of the project and its tasks, along with code examples and usage instructions. Each task is documented with specific requirements to be met, ensuring code quality and compliance with style guidelines.