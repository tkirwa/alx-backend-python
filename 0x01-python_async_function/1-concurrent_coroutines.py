#!/usr/bin/env python3
"""
This script defines an asynchronous routine 'wait_n' that spawns 'wait_random'
coroutines 'n' times with the specified 'max_delay' and
 returns a list of delays.
"""

import asyncio
from typing import List

# Import the 'wait_random' coroutine from the previous module
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that spawns 'wait_random' coroutines 'n' times with
      the specified 'max_delay'.

    Args:
        n (int): The number of times to spawn 'wait_random' coroutines.
        max_delay (int): The maximum delay in seconds.

    Returns:
        List[float]: A list of delays in ascending order.
    """
    # Create a list of tasks to execute 'wait_random' concurrently
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    # Use asyncio.as_completed to await the tasks as they complete
    return [await task for task in asyncio.as_completed(tasks)]
