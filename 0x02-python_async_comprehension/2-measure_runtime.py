#!/usr/bin/env python3
""" Task 2"""
import asyncio
import time

async_comprehension = find('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    Measure async_comprehension four times in parallel using asyncio.gather
    '''
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.perf_counter()
    return end - start
