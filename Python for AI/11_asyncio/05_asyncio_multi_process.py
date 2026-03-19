import asyncio, time
from concurrent.futures import ProcessPoolExecutor

def encrpyt(passowrd):
    print(f"encrypted - {passowrd[::-1]}")

async def main():
    loop =  asyncio.get_running_loop()
    with ProcessPoolExecutor() as pool:
        loop.run_in_executor(pool, encrpyt, "sohan15")
if __name__ =="__main__":
    asyncio.run(main())

