#!/usr/bin/env python3
"""
Module: 0-async_generator.py
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Coroutine that yields random numbers between 0 and 10 asynchronously.
    It loops 10 times, waiting 1 second in each iteration.

    Yields:
        float: A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


# Testing the async_generator coroutine
if __name__ == "__main__":

    async def print_yielded_values():
        result = []
        async for i in async_generator():
            result.append(i)
        print(result)

    asyncio.run(print_yielded_values())
