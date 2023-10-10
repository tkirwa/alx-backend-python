#!/usr/bin/env python3
"""
Module: 2-measure_runtime.py
"""

import asyncio
from time import perf_counter
from typing import List

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that executes async_comprehension four times in parallel
    using asyncio.gather and measures the total runtime.

    Returns:
        float: The total runtime in seconds.
    """
    start_time = perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )
    end_time = perf_counter()
    total_runtime = end_time - start_time
    return total_runtime


# Testing the measure_runtime coroutine
if __name__ == "__main__":

    async def main():
        runtime = await measure_runtime()
        print(f"Total runtime: {runtime} seconds")

    asyncio.run(main())
