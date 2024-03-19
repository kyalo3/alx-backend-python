#!/usr/bin/env python3
"""an asynchronous coroutine that takes in an integer argument"""
import asyncio
import random
from random import uniform
from typing import List
from _basic_async_syntax import wait_random


async def wait_random(max_delay: int = 10) -> float:
    """async function that waits for a random delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

async def wait_n(n: int, max_delay: int) -> float:
    """async function that waits for a random delay"""
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(delays)
