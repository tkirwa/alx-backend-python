import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and
      max_delay seconds.

    Args:
        max_delay (float, optional): The maximum delay in seconds.
        Defaults to 10.

    Returns:
        float: The random delay that was generated.
    """
    random_delay = random.random() * max_delay
    await asyncio.sleep(random_delay)
    return random_delay
