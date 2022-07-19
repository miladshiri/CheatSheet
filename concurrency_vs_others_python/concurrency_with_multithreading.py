from threading import Thread
import tasks 
from utils import print_execution_time 


@print_execution_time
def run_cpu_tasks():
    # Create different threads for the tasks
    task1_thread = Thread(target=tasks.cpu_task, args=('task1',))
    task2_thread = Thread(target=tasks.cpu_task, args=('task2',))

    # Start the threads
    task1_thread.start()
    task2_thread.start()

    # Wait for the threads to complete
    task1_thread.join()
    task2_thread.join()


@print_execution_time
def run_io_cpu_tasks():
    # Create different threads for the tasks
    task1_thread = Thread(target=tasks.io_cpu_task, args=('task1',))
    task2_thread = Thread(target=tasks.io_cpu_task, args=('task2',))

    # Start the threads
    task1_thread.start()
    task2_thread.start()

    # Wait for the threads to complete
    task1_thread.join()
    task2_thread.join()


if __name__ == '__main__':
    run_cpu_tasks()
    run_io_cpu_tasks()
    