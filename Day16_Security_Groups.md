# Day 16 – EC2 Security Groups

Today I focused on understanding EC2 security groups in detail and how they are used in real scenarios.

## What is a Security Group
A security group acts as a virtual firewall for an EC2 instance. It controls what traffic is allowed to reach the instance and what traffic can go out from it. Security groups are attached at the instance level.

By default:
- All inbound traffic is blocked
- All outbound traffic is allowed

## Inbound Rules
Inbound rules define who can access the EC2 instance.

Some common inbound examples:
- SSH on port 22 for server access
- HTTP on port 80 for web traffic
- HTTPS on port 443 for secure web traffic

If an inbound rule is not added, the connection will not reach the instance.

## Outbound Rules
Outbound rules define where the EC2 instance can send traffic.

Examples:
- Downloading packages from the internet
- Calling external APIs
- Sending logs to monitoring services

## Stateful Behavior
Security groups are stateful. This means:
- If inbound traffic is allowed, the response traffic is automatically allowed
- There is no need to explicitly open return ports

This is an important difference compared to NACLs.

## Common Ports
Some commonly used ports I reviewed:
- SSH: 22
- HTTP: 80
- HTTPS: 443
- RDP: 3389
- MySQL: 3306

## Hands-on Practice
I modified the security group of my EC2 instance to:
- Allow SSH (22) only from my IP
- Allow HTTP (80) from anywhere

I installed Apache on the EC2 instance and verified that the default Apache page was accessible using the public IP in a browser.

## Key Takeaways
- Security groups are stateful and instance-level
- Inbound rules are critical for access
- Opening SSH to the entire internet is unsafe
- Security groups are one of the main layers of EC2 security
