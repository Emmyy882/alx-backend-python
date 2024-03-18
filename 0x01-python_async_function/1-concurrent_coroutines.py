#!/usr/bin/env python3
"""an aynchronous python script"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """spawn wait_random n times with the specified max_delay.
       wait_n should return the list of all the delays
    """
    delay = [wait_random(max_delay) for _ in range(n)]
    wait_time = await asyncio.gather(*delay)

    return sorted(wait_time)
