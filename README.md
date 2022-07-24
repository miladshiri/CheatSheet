# CheatSheet
General things I have learned in software development 


## Clean/Good Code
* Use a popular conventions like PEP8 for Python
* Style conventions like:
    * Proper block indentation
    * Use blank line to separate methods 
    * Proper line width. For instance, 79 characters in PEP8 format

* Naming conventions in PEP8:
    * Long but clear names instead of using short and vague names
    * Functions: use lowercase letters and separate words with underscore
    * Classes: start each word with capital letter without any underscore between words

* Functions:
    * Should be small 
    * Do one task
    * Avoid having a lot of arguments 

* Classes:
    * Methods and properties should be consistent and related to one idea
    * Keep the number of methods and properties as low as possible
    * For generic tasks like a calculation create a separate function instead of writing
    the whole script inside the method
    * Using inheritance properly. For instance, when there are several classes with some similar methods or properties, create a parent class and leverage inheritance to build other classes. 

* Avoid making the code deep. For instance, avoid deep nested loops or conditions or even deep nested data structures.

* Commenting:
    * Basically if the names of files, functions, classes and variables are clear enough, 
    there is no need to write an explanation. However, it is usually difficult to encapsulate 
    the whole purpose in the name, So in that case leave a comment. 
    * Writing a short description about the script and its purpose at the top of the file
    * Writing a short description of what the function/class does in general, not the internal procedure. 
    * Avoid commenting useless code. Get rid of the useless code!
    * Use docstrings to add description for a function


* Find and remove dead code
* Avoid putting important information like passwords in the code. Use, for instance, environment variables. 
* Follow DRY principle! If you want to use a same piece of code over and over, turn it into a function or class. 
* Keep the length of scripts, functions or classes as low as possible. Avoid writing long scripts
and break them into smaller but coherent pieces.
* Use software architectures for the whole project, like MVC or MVT.
* Utilize design patterns
* Follow object oriented programming
* Handle all the errors and all the possibilities
* Use tests!
    * TDD: start the development with tests 
    * Use unit testing to test everything from small functions to APIs 
    * Integration testing for the connection between backend and frontend

* Use a version control. GIT or SVN. 
* Follow a workflow like GitHub flow or GitLab flow. For instance, create a production branch, a master branch and new branches for each feature or bug.  
* Use a devops platform like GitLab for collaboration, code review, CI/CD, etc. 
* Use CI/CD tools like GitLab or Jenkins 

## Object Oriented Programming (OOP) Rules
* Encapsulation: A class consists of data and methods bundled together.
* Abstraction: You don't need to know about the internal implementation details. Just use the class!.
* Inheritance: You can create another class with the same methods and properties of a parent class.
* Polymorphism: A method can accept different input shapes and does different things based on that.

## Async vs. Parallelism vs. Thread vs. Concurrent vs. Process
You can find the examples and comparisons in Python here: https://github.com/miladshiri/CheatSheet/tree/main/concurrency_vs_others_python
* Task and Multi-tasking: A CPU with one core can work only on one task at a time. Multitasking means doing 
several tasks simultaneously at a time.
* Thread vs. Process: Threads require less time for context switching as they are lighter than processes. 
Process are totally independent and have their own resources like memory while threads share the same resources. A process can hold several threads. 
* Thread and Multi-threading: A thread is the smallest set of tasks that can be executed independently from other threads. Multithreading means having different threads running at a time.
* Process and Multi-processing: Multi-processing means having several processes running in different cores in parallel. In a single-core cpu, we can have several processes running concurrently. 
* Parallelism vs. Concurrency: In parallelism, tasks are really executed simultaneously 
while in concurrency, the system continuously switches between different tasks to make it seem that all the tasks are running at the same time, but they are not actually. In a single-core cpu, you can 
only have concurrency and parallelism is possible with a multi-core cpu. Parallelism always decreases the overall execution time but concurrency can lead to a better performance when the code is also dependent on 
I/O operations such as reading from or writing to hard disk, rather than only processing operations. 
* Multithreading vs. Concurrency: Concurrency is a concept and multithreading is a way to achieve concurrency. 
* Multi-processing vs. Parallelism: Multi-processing can take place in both parallel and concurrent environments. 
* Parallel processing vs. Parallelism vs. Multiprocessing: Both can be happened only in a multi-core CPU through multiprocessing. Parallelism is about doing several tasks in parallel in different cores while parallel processing can be about only one big processing task running on different cores at the same time. For instance, processing the frames of a video can be done separately in parallel in different cores. On the other hand, multiprocessing means that you create different processes for doing different tasks. Those processes can be in either different cores or a same core. 
* Synchronous vs. Asynchronous: In synchronous environment, all lines of the code is executed one by one in order, while Asynchronous environment, different pieces can be executed without order.   
* AsyncIO vs. Threading: In AsyncIO, you can control when the program switches to another task with using await keyword, while in threading the system control the switching between the tasks. In case of dealing with I/O operations, to put the task into the back until the result is ready, AsyncIO is a better solution. When the code is a combination of processing and I/O operations, it is better to use threading. 


## Python 
* Global Interpreter Lock (GIL): GIL is a mechanism used in interpreter languages like Python to make sure that only one thread can execute at a time per process. Because if two threads try to access one variable at the same time, this causes deadlocks. The GIL is a single lock at the interpreter level that allows only one thread get access to the object/variable. 
* Memory management: Python uses reference counting for memory management. Python keeps track of the number of references that point to the object/variable. As soon as the counter reaches zero, the memory occupied by the object/variable is released. 

## ReactJS
* It's declarative, not imperative. 

## Git 
* Undo all the previous commits and get back to a certain commit
```
git reset --hard <commit>
git push --force
```

## SSH
* Start ssh-agent: ``` eval `ssh-agent -s` ```
* List of added keys: `ssh-add -l`
* Add a new private key: `ssh-add ~/.ssh/privatekey`

## AWS 
* Each region could include several connected availability zones (AZ), and each AZ could include several 
connected data centers
* Interacting with AWS: 1- Management Console, 2- CLI, and 3- SDK 
* IAM: Identity and Access Management  

### Amazon EC2
* It is like having virtual private servers but with customizable resources. 
* The three main categories of compute are virtual machines (VMs), containers, and serverless.
* AWS offers two container orchestration services – Amazon Elastic Container Service (ECS) and Amazon Elastic Kubernetes Service (EKS)

### Go serverless
* No servers to provision or manage/ Scales with usage/ You never pay for idle resources/ Availability and fault tolerance are built-in
* AWS has several serverless compute options, including AWS Fargate and AWS Lambda.

#### AWS Fargate
* for containers
*  abstracts the EC2 instance

#### AWS Lambda
* without having to manage any EC2 instances or containers. There are no servers to manage. 
* A Lambda function has three primary components – trigger, code, and configuration. 

