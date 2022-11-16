# concurrency

import requests
import time

def download_site(url: str, session: requests.Session):
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")


def download_all_sites(sites:list[str]):
    with requests.Session() as session:
        for url in sites:
            download_site(url, session)


sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
start_time = time.time()
download_all_sites(sites)
duration = time.time() - start_time
print(f"Downloaded {len(sites)} in {duration} seconds")