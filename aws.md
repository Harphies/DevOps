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
