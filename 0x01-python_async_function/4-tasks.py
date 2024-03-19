#!/usr/bin/env python3
"""an asynchronous coroutine that takes in an integer argument"""
import asyncio
import lists
import random
from _basic_async_syntax import wait_random


def task_wait_n(n: int, max_delay: int) -> List(float):
    """
    Return asyncio.Task.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    completed, pending = asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)
    return [task.result() for task in completed]
