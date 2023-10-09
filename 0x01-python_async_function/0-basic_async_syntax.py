#!/usr/bin/env python3

import asyncio
import random

# Define an asynchronous coroutine named wait_random
# It takes an optional integer argument max_delay with a default value of 10
# It returns a float representing the random delay


async def wait_random(max_delay: int = 10) -> float:
    # Generate a random float between 0 and max_delay (inclusive)
    wait_time = random.random() * max_delay

    # Pause the coroutine's execution for the generated wait_time
    await asyncio.sleep(wait_time)

    # Return the random delay as a float
    return wait_time
