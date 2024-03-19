#!/usr/bin/env python3
""" coroutine called async_generator that takes no arguments """
import asyncio
from typing import AsyncGenerator
import random
from random import uniform
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    return [i async for i in async_generator()][:10]


async def main():
    print(await async_comprehension())

asyncio.run(main())
