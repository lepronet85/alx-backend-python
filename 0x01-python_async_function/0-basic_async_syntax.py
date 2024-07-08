#!/usr/bin/env python3
'''
    This script demonstrates the basics of asynchronous
    programming in Python using asyncio.
    It defines an asynchronous function that waits for a
    randomly determined duration,
    then returns that duration once the wait is over.
'''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously waits for a random delay between 0 and
    max_delay (inclusive).
    Returns the actual delay waited upon completion.

    Parameters:
    - max_delay (int): Maximum delay time in seconds. Defaults to 10.

    Returns:
    - float: The actual delay waited in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
