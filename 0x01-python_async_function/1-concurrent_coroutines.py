#!/usr/bin/env python3

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """
    Asynchronous routine that spawns wait_random n times with the specified
      max_delay.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay in seconds.

    Returns:
        list[float]: A list of delays in ascending order.
    """
    delays = []

    async def execute_wait_random():
        delay = await wait_random(max_delay)
        delays.append(delay)

    # Create a list of tasks to execute wait_random concurrently
    tasks = [execute_wait_random() for _ in range(n)]

    # Run the tasks concurrently
    await asyncio.gather(*tasks)

    return sorted(delays)
