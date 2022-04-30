from concurrent.futures import ThreadPoolExecutor
import time


class Counter:
    def __init__(self) -> None:
        self.count = 0

    def step(self):
        count = self.count
        count += 1
        time.sleep(0.1)
        self.count = count
        print(f'count: {self.count}')


if __name__ == '__main__':

    counter = Counter()
    for i in range(0, 5):
        counter.step()
    assert counter.count == 5

    with ThreadPoolExecutor(max_workers=5) as exe:
        for i in range(0, 5):
            exe.submit(counter.step)