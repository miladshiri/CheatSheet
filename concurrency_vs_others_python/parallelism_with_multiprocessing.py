from multiprocessing import Process 
import tasks 
from utils import print_execution_time 


@print_execution_time
def run_cpu_tasks():
    # Create different processes for the tasks
    task3_process = Process(target=tasks.cpu_task, args=('task1',))
    task4_process = Process(target=tasks.cpu_task, args=('task2',))

    # Start the processes
    task3_process.start()
    task4_process.start()

    # Wait for the processes to complete
    task3_process.join()
    task4_process.join()

@print_execution_time
def run_io_cpu_tasks():
    # Create different processes for the tasks
    task3_process = Process(target=tasks.io_cpu_task, args=('task1',))
    task4_process = Process(target=tasks.io_cpu_task, args=('task2',))

    # Start the processes
    task3_process.start()
    task4_process.start()

    # Wait for the processes to complete
    task3_process.join()
    task4_process.join()

if __name__ == '__main__':
    run_cpu_tasks()
    run_io_cpu_tasks()
    