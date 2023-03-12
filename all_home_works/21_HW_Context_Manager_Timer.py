import time


class Timer:

    def __init__(self):
        self.start_time = time.time()

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def elapsed_time(self):
        return time.time() - self.start_time

    def reset(self):
        self.start_time = time.time()
        return 'time has been reset'


with Timer() as t:
    time.sleep(1)
    for i in range(0, 10000000):
        pass
print(t.elapsed_time())  # ~1.4 second

with t:
    time.sleep(2)
print(t.elapsed_time())  # ~2 seconds

with Timer() as t2:
    time.sleep(1)
    t2.reset()
    time.sleep(1)
print(t2.elapsed_time())  # ~1 second

with t2:
    time.sleep(2)
print(t2.elapsed_time())  # ~2 seconds

with Timer() as t:
    time.sleep(1)
print(t.elapsed_time())  # ~1 as expected

time.sleep(3)

with t:
    time.sleep(2)
print(t.elapsed_time())  # expected ~2, but got ~6
