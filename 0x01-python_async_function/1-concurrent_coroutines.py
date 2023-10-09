#!/usr/bin/env python3
""" Execute multiple coroutines at the same time with async """

import asyncio
from typing import List

# Import the wait_random coroutine from the previous file
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that spawns wait_random n times with the specified
      max_delay.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay in seconds.

    Returns:
        List[float]: A list of delays in ascending order.
    """
    # Create a list of tasks to execute wait_random concurrently
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    # Use asyncio.gather to run the tasks concurrently
    await asyncio.gather(*tasks)

    # Extract the result from each task (delays) and return them in ascending
    #  order
    return [task.result() for task in tasks]
