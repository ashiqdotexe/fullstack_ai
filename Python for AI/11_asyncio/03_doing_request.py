import asyncio, aiohttp
import json
async def fetch_url(session, url, idx):
    async with session.get(url) as response:
        data = await response.json()
        with open(f"E:/Practice Project/data science/fullstack_ai/Python for AI/11_asyncio/response_{idx}.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
            """
            : We Use *dump()* when we need to save a file in the local
            : We use *dumps()* when we need to store the json value in memory or 
              in any variable
            """
        print(f"Fetched {url} with status {response.status} and saved it")
async def main():
    urls = ["https://httpbin.org/delay/2"] * 3
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url, idx) for idx, url in enumerate(urls, 1)]
        await asyncio.gather(*tasks)
        # Here we are using "*tasks" for unpacking the whole tasks it can be like bello
        # asyncio.gather(t1,t2,t3)-> so we are unpacking three urls here"
asyncio.run(main())