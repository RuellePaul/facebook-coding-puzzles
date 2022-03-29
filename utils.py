import functools
from time import time


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        time_start = time()
        result = func(*args, **kwargs)
        print(f'Run in {(time() - time_start):.3f}s')
        return result

    return wrapper
