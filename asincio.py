import asyncio
import time
async def func1():
    time.sleep(3)
    print("func1")

async def func2():
    time.sleep(3)
    print("func2")

async def func3():
    time.sleep(3)
    print("func3")

async def main():
    taskl = asyncio.create_task(func1())
    await asyncio.sleep(4)


async def maina():
   k = await asyncio.gather(
       
       func1(),
       func2(),
       func3()
   )