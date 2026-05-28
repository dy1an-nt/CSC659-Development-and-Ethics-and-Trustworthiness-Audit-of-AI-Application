import threading
import time
import random

def mock_download(url: str, index: int) -> None:
    delay = random.uniform(0.05, 0.2)
    print(f"[Thread {index}] Starting download: {url}")
    time.sleep(delay)
    print(f"[Thread {index}] Finished: {url} (took {delay:.2f}s)")

def download_all(urls: list) -> None:
    threads = []
    for i, url in enumerate(urls):
        t = threading.Thread(target=mock_download, args=(url, i + 1))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print("\nAll downloads complete.")

image_urls = [
    "https://example.com/image1.png",
    "https://example.com/image2.jpg",
    "https://example.com/image3.gif",
    "https://example.com/image4.webp",
    "https://example.com/image5.png",
]

start = time.perf_counter()
download_all(image_urls)
total = time.perf_counter() - start
print(f"Total time: {total:.2f}s")
