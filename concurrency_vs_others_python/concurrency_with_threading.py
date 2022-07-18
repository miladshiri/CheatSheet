from threading import Thread
import tasks 
from utils import print_execution_time 



@print_execution_time
def run_tasks():
    # Create different threads for the tasks
    task1_thread = Thread(target=tasks.task1)
    task2_thread = Thread(target=tasks.task2)

    # Start the threads
    task1_thread.start()
    task2_thread.start()

    # Wait for the threads to complete
    task1_thread.join()
    task2_thread.join()

if __name__ == '__main__':
    run_tasks()
    