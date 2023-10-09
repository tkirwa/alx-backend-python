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
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay

# The following code demonstrates how to use the wait_random coroutine.
if __name__ == "__main__":
    print(asyncio.run(wait_random()))
    print(asyncio.run(wait_random(5)))
    print(asyncio.run(wait_random(15)))
