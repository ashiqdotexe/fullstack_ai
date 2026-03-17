import asyncio

async def serve():
    print(f"Tea is getting ready")
    await asyncio.sleep(2)
    print(f"Tea is ready")
asyncio.run(main=serve())