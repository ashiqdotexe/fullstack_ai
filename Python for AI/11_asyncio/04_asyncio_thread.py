import asyncio,time
from concurrent.futures import ThreadPoolExecutor

def check_store(item):
    print(f"Checking {item}....")
    time.sleep(3)
    print(f"Item #{item} stored in Database")
async def main():
    items = ["Masala", "Ginger", "Cardamom"]
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        results = [loop.run_in_executor(pool, check_store, item) for item in items]
        await asyncio.gather(*results)
asyncio.run(main())