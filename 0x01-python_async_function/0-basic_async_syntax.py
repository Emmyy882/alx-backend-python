#!/usr/bin/env python3
"""A script that implements an asynchronous coroutine"""
import asyncio
import random


async def wait_random(max_delay: int = 10):
    """
    An asynchronous coroutine that waits for a random number of seconds
    between 0 and max_delay(included and float value).
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
