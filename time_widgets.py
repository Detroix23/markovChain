import time

def uptime_count(interval: float, start: float = time.monotonic()) -> None:
    while True:
        print(f"{(time.monotonic() - start):.2f}s")
        time.sleep(interval)