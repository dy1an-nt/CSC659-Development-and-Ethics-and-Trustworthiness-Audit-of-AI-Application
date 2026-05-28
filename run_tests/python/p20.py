import time
import functools

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        elapsed = end - start
        print(f"[TIMER] '{func.__name__}' executed in {elapsed:.6f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(0.1)
    return "done"

@timer
def sum_large(n):
    return sum(range(n))

result1 = slow_function()
result2 = sum_large(1_000_000)
print(f"Sum result: {result2}")
