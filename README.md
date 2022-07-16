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
* Handle all the errors and all the possibilities
* Use tests!
    * TDD: start the development with tests 
    * Use unit testing to test everything from small functions to APIs 
    * Integration testing for the connection between backend and frontend

* Use a version control. GIT or SVN. 
* Use a devops platform like GitLab for collaboration, code review, CI/CD, etc. 
* Use CI/CD tools like GitLab or Jenkins 



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

