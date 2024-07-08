#!/usr/bin/env python3
"""
    This script demonstrates advanced asynchronous programming
    techniques in Python using asyncio.
    It defines a function that spawns multiple instances of another
    asynchronous function,
    wait_random, with a specified maximum delay, then collects
    and returns the durations of these waits.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns the wait_random function n times concurrently, each
    with a specified max_delay.
    Waits for all spawned tasks to complete and returns a list
    of the durations waited.

    Parameters:
    - n (int): Number of times to spawn wait_random.
    - max_delay (int): Maximum delay time in seconds for each spawned task.

    Returns:
    - List[float]: A list of floats representing the durations waited
    by each spawned task.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
