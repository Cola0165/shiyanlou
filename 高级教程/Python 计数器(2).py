from concurrent.futures import ThreadPoolExecutor
import threading
import time


class LockCounter:
    def __init__(self) -> None:
        self.count = 0
        self.lock = threading.Lock()

    def step(self):
        with self.lock:
            count = self.count
            count += 1
            time.sleep(0.1)
            self.count = count
        print(f'lock_counter: {self.count}')

    def size(self):
        count = 0
        with self.lock:
            count = self.count
        return count


if __name__ == '__main__':
    lock_counter = LockCounter()
    with ThreadPoolExecutor(max_workers=5) as exe:
        for i in range(0, 5):
            exe.submit(lock_counter.step)
    assert lock_counter.count == 5