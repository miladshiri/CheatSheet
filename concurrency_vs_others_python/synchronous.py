import tasks 
from utils import print_execution_time 

@print_execution_time
def run_tasks():
    tasks.task1()
    tasks.task2()

if __name__ == '__main__':
    run_tasks()
