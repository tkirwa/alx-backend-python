#!/usr/bin/env python3
"""
This script defines a function 'measure_time' to measure the average
 execution time
of the 'wait_n' coroutine for 'n' iterations with a specified 'max_delay'.
"""

import asyncio
import time
from typing import Callable

# Import the 'wait_n' coroutine from the previous module
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average execution time of 'wait_n' coroutine.

    Args:
        n (int): The number of iterations.
        max_delay (int): The maximum delay in seconds for 'wait_n'.

    Returns:
        float: The average execution time in seconds.
    """
    total_time = 0.0

    # Measure the execution time for 'n' iterations of 'wait_n'
    for _ in range(n):
        start_time = time.time()
        asyncio.run(wait_n(n=1, max_delay=max_delay))
        end_time = time.time()
        total_time += end_time - start_time

    # Calculate the average time per iteration
    average_time = total_time / n

    return average_time


if __name__ == "__main__":
    # Test the 'measure_time' function
    n = 5
    max_delay = 9
    average_time = measure_time(n, max_delay)
    print(average_time)
