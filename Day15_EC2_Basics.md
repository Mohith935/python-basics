# Day 15 – EC2 Basics

Today I started AWS and focused on understanding EC2 from both a conceptual and hands-on point of view.

## AWS Overview
AWS provides cloud infrastructure where we can create and manage resources on demand instead of maintaining physical servers. The main idea is pay-as-you-go and scalability.

## EC2 Basics
EC2 is a virtual server provided by AWS. While launching an instance, we need to choose:
- AMI (operating system)
- Instance type (CPU and memory)
- Key pair (for SSH access)
- Security group (firewall rules)

I used **Amazon Linux 2** with **t2.micro** since it is eligible for the free tier.

## Security Group
I configured a security group to:
- Allow SSH (port 22)
- Restrict access only to my IP

This helped me understand that security groups act like **stateful firewalls**.

## Connecting to EC2
I connected to the instance using SSH and verified that it is a real Linux machine by running:
- uname
- df
- free

This confirmed that EC2 behaves like a normal server.

## EC2 Lifecycle
I learned about the EC2 instance states:
- Pending
- Running
- Stopped
- Terminated

Stopping an instance stops billing for compute, while termination permanently deletes it.

## Key Takeaways
- EC2 is the core compute service in AWS
- Security groups control inbound and outbound traffic
- Key pairs are required for secure access
- Always stop instances when not in use to avoid charges
