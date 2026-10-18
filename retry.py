"""Exponential backoff retry decorator."""
import functools
import time


def retry(tries=3, delay=0.5, backoff=2.0, exceptions=(Exception,)):
    """Retry a function with exponential backoff."""
    def deco(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            d = delay
            for attempt in range(tries):
                try:
                    return fn(*args, **kwargs)
                except exceptions:
                    if attempt == tries - 1:
                        raise
                    time.sleep(d)
                    d *= backoff
        return wrapper
    return deco
