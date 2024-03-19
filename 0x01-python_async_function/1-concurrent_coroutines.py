#!/usr/bin/env python3
"""an asynchronous coroutine that takes in an integer argument"""
import asyncio
import random
from typing import List
from _basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """async function that waits for a random delay"""
    tasks = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return results
