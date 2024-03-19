#!/usr/bin/env python3
"""an asynchronous coroutine that takes in an integer argument"""
import asyncio
import random
from typing import List


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """async function that waits for a random delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(*tasks)
    return sorted(delays)
