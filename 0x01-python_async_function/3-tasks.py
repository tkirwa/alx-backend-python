#!/usr/bin/env python3
"""
This script defines a function 'task_wait_random' that creates an asyncio.
 Task for 'wait_random'.
"""

import asyncio

# Import the 'wait_random' coroutine from the previous module
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio.Task for the 'wait_random' coroutine with the specified
      'max_delay'.

    Args:
        max_delay (int): The maximum delay in seconds for 'wait_random'.

    Returns:
        asyncio.Task: An asyncio.Task object for 'wait_random'.
    """
    # Create an asyncio.Task for 'wait_random' with the specified 'max_delay'
    task = asyncio.create_task(wait_random(max_delay))

    return task


if __name__ == "__main__":
    # Test the 'task_wait_random' function
    max_delay = 5
    task = task_wait_random(max_delay)

    async def test(max_delay):
        await task
        print(task.__class__)

    asyncio.run(test(max_delay))
