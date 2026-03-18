import asyncio, aiohttp

async def fetch_url(session, url):
    async with session.get(url) as response:
        print(f"Fetched {url} with status {response.status}")
async def main():
    urls = ["https://httpbin.org/delay/2"] * 3
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        await asyncio.gather(*tasks)
        # Here we are using "*tasks" for unpacking the whole tasks it can be like bello
        # asyncio.gather(t1,t2,t3)-> so we are unpacking three urls here"
asyncio.run(main())