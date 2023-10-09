#!/usr/bin/env python3
"""
This script defines a function 'task_wait_n' that creates tasks for
 'task_wait_random' and returns the delays.
"""

import asyncio
from typing import List

# Import the 'task_wait_random' function from the previous module
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Create tasks for 'task_wait_random' and return the list of delays in
      ascending order.

    Args:
        n (int): The number of tasks to create.
        max_delay (int): The maximum delay in seconds for 'task_wait_random'.

    Returns:
        List[float]: A list of delays in ascending order.
    """
    # Create a list of tasks for 'task_wait_random' with the specified
    #  'max_delay'
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    # Use asyncio.as_completed to await the tasks as they complete
    completed_tasks = await asyncio.gather(*tasks)

    # Collect the results (delays) from the completed tasks in ascending order
    delays = sorted(completed_tasks)

    return delays

if __name__ == "__main__":
    # Test the 'task_wait_n' function
    n = 5
    max_delay = 6
    delays = asyncio.run(task_wait_n(n, max_delay))
    print(delays)
