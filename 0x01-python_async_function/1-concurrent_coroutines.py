#!/usr/bin/env python3
"""an asynchronous coroutine that takes in an integer argument"""
import asyncio
from random import uniform
from typing import List
from typing import AsyncGenerator
from _basic_async_syntax import wait_random


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """async function that waits for a random delay"""
    delays = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        delays.append(delay)
    return sorted(delays)
