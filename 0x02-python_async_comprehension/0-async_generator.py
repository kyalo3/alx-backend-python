#!/usr/bin/env python3
""" coroutine called async_generator that takes no arguments """
import asyncio
from typing import AsyncGenerator
import random
from random import uniform


async def async_generator() -> AsyncGenerator[float, None]:
    """Coroutine that generates random numbers asynchronously."""
    for _ in range(10):
        await asyncio.sleep(1)  # Wait for 1 second asynchronously
        yield uniform(0, 10)
