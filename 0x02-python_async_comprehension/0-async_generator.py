#!/usr/bin/env python3
"""
Module: 0-async_generator.py
"""

from asyncio import sleep
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Coroutine that yields random numbers between 0 and 10 asynchronously.
    It loops 10 times, waiting 1 second in each iteration.

    Yields:
        float: A random number between 0 and 10.
    """
    for _ in range(10):
        await sleep(1)
        yield uniform(0, 10)
