# CheatSheet
General things I have learned in software development 


## Clean/Good Code
* Long but clear names instead of using short and vague names
* Functions:
    * Should be small 
    * Do one task
    * Avoid having a lot of arguments 

* Classes:
    * Methods and properties should be consistent and related to one idea
    * Keep the number of methods and properties as low as possible
    * For generic tasks like a calculation create a separate function instead of writing
    the whole script inside the method
    

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

