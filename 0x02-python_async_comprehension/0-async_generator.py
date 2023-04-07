#!/usr/bin/env python3
"""Task 0"""
import asyncio
import typing
import random


async def async_generator() -> Generator[float, None, None]:
    """
    The coroutine will loop 10 times
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
