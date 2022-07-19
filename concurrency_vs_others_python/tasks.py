import time
import asyncio 
from utils import print_execution_time, print_execution_time_async

# This function simulates a cpu intensive task 
@print_execution_time
def cpu_task(message=''):
    for i in range(10):
        print(message)
        s = 1
        for i in range(10000000):
            s *= i
        
# This function simulates both I/O operations as well as cpu-bound operations 
@print_execution_time
def io_cpu_task(message=''):
    for i in range(10):
        print(message)
        s = 1
        for i in range(1000):
            s *= i
        time.sleep(.3)

# This function simulates I/O-bound operations 
@print_execution_time
def io_task():
    time.sleep(3)

# This function simulates I/O-bound operations in the async mode 
@print_execution_time_async
async def io_task_async():
    await asyncio.sleep(3)
