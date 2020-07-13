## Amazon web services (AWS) Certified Developer Associate

## List of AWS services

- EC2
- VPC
- IAM
- Route 53
- Elsastic Beanstak
- DynamoDB
- RDS
- Kinesis
- SNS
- Lambda
- AWS SDk
- Security
- S3
- API Gateways
- Cloud Formation
- Developer tools
  - Code Commit
  - Code Build
  - Code Deploy
  - Code Pipeline
  - Code Star
  - X-Ray

## Types of cloud

- Public : Provider data center
- Private : Your data center
- Hybrid : Combination of both

## AWS Services categories/ Buckets

- Compute
- Storage
- Database
- Networking and Content Delivery
- Security, Identity & Compliance

# Notes

- On premises IT -> Infrastructuree -> Platform -> Software as Services
- Cloud service broker: Bridge between two cloud providers.
- Policy: A set of permissions

## AWS CLI and SDK settings

- Create a AWS Account
- Download the AWS CLI for your OS in my case [Window] and install
- Create an IAM programatic user in order to use the AWS CLI against the AWS services.
- Run AWS configure in the CLI terminal to setup the access key and the secret Acess Key
- To check the access key setup earlier
  - Nagivate to system name: in my own case [C:\Users\taofe] use Gitbash and run the following commands
  - cd .aws
  - ls -al to have access to the config and the credential files.
  - cat credentials
  - cat configure

## AWS Commands

- aws --version
- aws help
- aws ec2 help

## identity and Access management (IAM)

- User
- Group
- Role
- Policy

## Virtual Private Cloud : A virtual network dedicated to your AWS Account

- Create a VPC in another region
  - Create the subnets and associate it with a VPC (We can create both Private and Public subnets)
    - Configure the settings of the subnet (like auto assign of public IP) for public subnets
  - Create Internet gateway in the subnet
    - Attach the Internet gateway to a Virtual Private Cloud
  - Create a NAT Gateway and associate it with a subnet
    - Allocate an Elastic IP
  - Create the Route table (Public and Private)
    - Associate a subnet to the route table
    - Edit the routes and add some default routes and associate it with a NAT gateway.
  - Create Network ACL
    - configire the inbound and outbound rules
  - Launch EC2 instances for all the servers
    - configure the seurity group and associate it with the VPC
  - Create a loadbalancer
    - Application Load balancer
    - Network Load balancer
    - Add a Load balancer to the Instances of the webser

## EC2: Elastic Compute Cloud

- Time-base scaling
- Scale on demand
- Instances Types
  - General purpose t2 micro
  - Compute Optimized
  - GPU Graphics
  - GPU Compute
  - Memory Optimized
  - Storage Optimized
- O/S's
  - Linux (Base Images Only)
    - Amazon Linux
    - Amazon Linux 2
    - SUSE Linux Enterprise Server
    - Red Hat Enterprise Linux
    - Ubuntu Server
  - Windows (Base Images Only)
    - Server 2016
    - Server 2012 R2
    - Server 2012
    - Server 2008
  - Sub-options for:
    - SQL Server Base
    - SQL Server Web
    - SQL Server Standard

## EC2 General Use

- select a region
- select Amazon machine Image
- use default VPC
- select a subnet
- Enable Auto Assign IP
- Optional IAM Role: In case we want the Instance to access other AWS services
- Shutdown behavior stop
- Protect against Accidental termination
- leave the network interface as default: allow it to auto assign IP
- Skip storage settings
- Add tags
- Configure the security group
- create a key pair for launch
- copy the public IPv4 address to clipboard (that is where the server will be accessed)
- Anything you want to be running will be placed in the Advanced Details: User data tab (ther web application we want to run).

## Amazon machine images:machines used

- Images can run instances

## Elastic IPs

- It allows to deal with the dynamic IP address and allow us to use the same IP address everytime.
- steps
  - Allocate an IP
  - Associate it with the running instance

## EC2 Load Balancer: Speed and efficiency.

- It allows us to distribute loads to web servers
- Steps:
  - Run mutltiple Instances with each instances running the same application.
  - Create Application Load Balancer
    - Name
    - scheme: internet-facing
    - ipv4
    - Listener protocol: http:80
    - Avalability zone region
    - Configure security groups
    - Configure routing
      - New target group
      - protocol:80
      - Register the Instances to use the Load balancer

## Route 53 DNS

- AWS managed Domain name system (DNS)
- Provides translation of names to IP addresses
- store names to IP mappings
- Answer resolution queries from client
- Ipv6 compliant
- within 60 seconds propagation
- Traffic management
- Route 53 Zones
- Create record sets
- Aliases
- traffic flow
- Route 53 Best practices

## Database and Storage services

## Simple Storage service

- S3 components
  - Bucket
    - objects are stored in buckets
  - Objects
    - entity stored in Amazon S3
    - Custom meta data
    - default meta data
  - Keys
    - Unique identifier for an object
    - Every object has one key
- Steps:
  - Create a bucket [public and private]
    - Name
    - region
    - upload the file and set the permission
    - bucket best practices
- Data replication : region replication of data in a bucket

  - for data replication for latency
  - copy to another region and reference it there.

- Glacier: for large file that doesn't require frequent access
  - data warehouse services
- Security
- Events : Ability to have something to occur whenever an activity occurs.
- Best practices of bucket in production

  - use IAM permission, no full control
  - Enable bucket enscryption for data at rest
    - Use S3 SSE-KMS for key management
    - use customer provided master key.
  - Enable access logging for S3 buckets.
  - Enable versioning
    - protect from overite and deletion
    - retrieve/ restore deleted objects or rollback
  - Back Up buckets

  ## Database(RDS/EC2)

  - Amazon Aurora : MySQL and PostgreSQL-compatible
  - MySQL
  - PostgreSQL : oracle compatible
  - MariaDB
  - Oracle
  - Microsoft SQL Server
    - SQL Server Express
    - SQL Server Web
    - SQL Server Enterprise edition
    - SQL Server Standard edition
  - RDS Interfaces
    - RDS console
    - AWS CLI
    - Progmatic Interface
      - AWS SDKs
      - Libraries
      - RDS API
  - RDS Security
    - Security Groups
      - DB security group
      - VPC security groups
      - EC2 security groups
  - IAM Permissions for the services not the data
  - RDS configuration
  - RDS Scaling
  - RDS Best practices
  - Database on EC2

## DynamoDB (Amazon NoSQL)

## Simple Queue Services (SQS)

- Standard Queue
- FIFO Queue
- message retension period
- visibility tmeout
- message size
- delivery delay (Queue setting)
- dead letter queue
- cost allocation tags
- server side encryption (SSE)
- Cloudwatch monitoring
- Queue creation
- Queue Interaction
- SQS Lambda Invocation
- SQS best practices

## Simple Notification System (SNS)

- Providers and consumers (Publish and subscribe)
- Publisher
  - SNS Topics
    - Lambda( code execution environment)
    - SQS
    - HTTP/S
    - Email
    - SMS
    - Mobile Push
      - Mbile push Notification services
        - Amazon (ADM)
        - APNS
        - Baidu
- Cloudwatch SNS
- SNS Topics (creation)
- SNS Email/SMS
- Filter policy
- SNS Lambda Invocation
- SNS Best practices

## Lambda: serverless compute

- Lambda Event Sources
- Lambda Scalability and Avalability
- Lambda Security
- Lambda function Lifecycle
  - Develop
  - Upload
  - Monitor and Troubleshoot
- Programming model (Node.js)
  - Handler
  - Context
  - Logging
  - Exceptions
- Lambda creation
  - runtime
  - Event
  - Logging
- Lambda best practices

## Elastic Beanstalk: For Large Rapid application development

- Application lifecycle
  - Create an application
  - Elastic Beanstalk launches an environment
  - Manage environment
- EB Development stack
- EB Database
- EB Platform updates
- EB Best Practices

## Kinesis: Realtime data procesing and Analysis services

- capture, process, ans store video streams for analytics and machine leaning
- serverless
- Build real-time application
- shards
- partition keys
- Kinesis Streams
- kinesis Firehose
- kinesis analytics

## API Gateway: Build, deploy and manage

- Creating a fully managed API that scales
- API Gateway creation and Integration with Lambda
- API Gateway creation with HTTP Integration
- API Gateway Security

## CloudFormation: Replicating/ duplicate existing environment

- cloudformation templates
- cloudformation stacks
- cloudformation best practices
