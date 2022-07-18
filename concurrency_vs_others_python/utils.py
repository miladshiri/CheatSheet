import time 
from functools import wraps

def print_execution_time(func):
    def wrapper(*args, **kwargs):
        print('{} started'.format(func.__name__))
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print('{} ended'.format(func.__name__))
        message = 'Execution time for {} is: {}'.format(func.__name__, end - start)
        print(message)
    return wrapper

def print_execution_time_async(func):
    async def wrapper(*args, **kwargs):
        print('{} started'.format(func.__name__))
        start = time.time()
        await func(*args, **kwargs)
        end = time.time()
        print('{} ended'.format(func.__name__))
        message = 'Execution time for {} is: {}'.format(func.__name__, end - start)
        print(message)
    return wrapper