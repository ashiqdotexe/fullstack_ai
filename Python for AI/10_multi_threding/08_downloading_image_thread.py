import threading
import time
import requests
def download_image(url):
    print(f"Downloading image of url - {url}")
    response = requests.get(url)
    print(f"Downloaded image of size- {len(response.content)/1024} kb")

urls = [
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/svg"
]
start = time.time()
threads = []
[threads.append(threading.Thread(target=download_image, args=(url,))) for url in urls]
[t.start() for t in threads]
[t.join() for t in threads]
end = time.time()

print(f"Total time taken {end-start} seconds")