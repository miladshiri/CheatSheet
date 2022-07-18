import time
import asyncio 
from utils import print_execution_time, print_execution_time_async

# This task simulates both I/O operations as well as cpu-bound operations 
@print_execution_time
def task1():
    for i in range(10):
        print('task1')
        time.sleep(.3)
    
# This task simulates both I/O operations as well as cpu-bound operations 
@print_execution_time
def task2():
    for i in range(20):
        print('task2')
        time.sleep(.2)

# This task simulates I/O-bound operations 
@print_execution_time_async
async def task1_async():
    await asyncio.sleep(3)

# This task simulates I/O-bound operations     
@print_execution_time_async
async def task2_async():
    await asyncio.sleep(4)
    