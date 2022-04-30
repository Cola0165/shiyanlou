from concurrent.futures import ThreadPoolExecutor
from queue import Queue
from lock_counter import LockCounter
from image_download import download_img
import threading


class ImageDownloader:
    def __init__(self, worker_count, progress) -> None:
        self.queue = Queue(1024)
        self.event = threading.Event()
        self.worker_count = worker_count
        self.counter = LockCounter()
        self.progress = progress
        self.pool = ThreadPoolExecutor(max_workers=self.worker_count+2)

    def __consumer(self):
        while not self.event.is_set():
            if not self.queue.empty():
                url = self.queue.get()
                print(f"[consumer] get url:{url}")
                download_img(url)
                self.counter.step()
            else:
                print("[consumer] queue is empty, just wait")
                self.event.wait()

            if self.event.is_set():
                self.event.clear()

            if self.progress(self.counter.size()):
                print('done')
                self.event.set()
                break

    def post(self, url):
        print(f"[producer] put url:{url}")
        self.queue.put(url)
        self.event.set()

    def start(self):
        for i in range(0, self.worker_count):
            self.pool.submit(self.__consumer)


if __name__ == '__main__':
    urls = [
        "https://img-ask.csdnimg.cn/upload/1623844642974.jpg",
        "https://img-ask.csdn.net/upload/201510/22/1445491909_384819.jpg",
    ]

    downloader = ImageDownloader(3, lambda count: count == len(urls))
    downloader.start()
    for url in urls:
        downloader.post(url)