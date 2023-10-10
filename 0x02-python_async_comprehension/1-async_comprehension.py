#!/usr/bin/env python3
"""
Module: 1-async_comprehension.py
"""

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using an async comprehension
    over async_generator, and returns the 10 random numbers.

    Returns:
        List[float]: A list containing 10 random numbers.
    """
    return [i async for i in async_generator()]

# Testing the async_comprehension coroutine
if __name__ == "__main__":
    async def main():
        print(await async_comprehension())

    asyncio.run(main())
