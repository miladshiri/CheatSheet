import asyncio
import tasks 
from utils import print_execution_time_async

@print_execution_time_async
async def run_tasks():
    await asyncio.gather(tasks.task1_async(), tasks.task2_async())
    
if __name__ == '__main__':
    asyncio.run(run_tasks())
