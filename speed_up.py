# concurrency

import asyncio
import aiohttp
import time


async def download_site(session, url: str):
    async with session.get(url) as response:
        print("Read {0} from {1}".format(response.content_length, url))


async def download_all_sites(sites:list[str]):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.ensure_future(download_site(session, url))
            tasks.append(task)
        
        await asyncio.gather(*tasks, return_exceptions=True)
        


sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
start_time = time.time()
asyncio.get_event_loop().run_until_complete(download_all_sites(sites))
duration = time.time() - start_time
print(f"Downloaded {len(sites)} in {duration} seconds")