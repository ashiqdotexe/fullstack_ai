import threading, asyncio, time

def keep_log():
    while True:
        time.sleep(1)
        print(f"Keeping log in every second")
async def main():
    await asyncio.sleep(3)
    print(f"Order is ready")

threading.Thread(target=keep_log, daemon=True).start()
asyncio.run(main=main())