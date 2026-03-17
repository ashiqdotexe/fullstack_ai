import asyncio
import time
# async never blocks any task.. It makes you wait but in non blocking way
async def with_async(name):
    print(f"Preparing {name} tea")
    await asyncio.sleep(3)
    print(f"Finished preparing {name} tea")
async def with_time(name):
    print(f"Preparing {name} tea")
    time.sleep(3)
    print(f"Finished preparing {name} tea")
async def main():
    start_1 = time.time()
    await asyncio.gather(
        with_async("masala"),
        with_async("ginger"),
        with_async("cardamom"),
    )
    end_1 = time.time()
    start_2 = time.time()
    await asyncio.gather(
        with_time("masala"),
        with_time("ginger"),
        with_time("cardamom"),
    )
    end_2 = time.time()
    print(f"Total time taken by async methond- {end_1-start_1:.2f} seconds")
    print(f"Total time taken by time methond- {end_2-start_2:.2f} seconds")
asyncio.run(main())