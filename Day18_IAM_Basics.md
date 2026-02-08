# Day 18 – IAM Basics

Today I worked on IAM (Identity and Access Management) and understood how AWS controls access to resources.

## What IAM is used for
IAM is used to manage who can log in to AWS and what actions they are allowed to perform. It helps control access to services and resources using permissions.

It answers two main questions:
- Who are you?
- What are you allowed to do?

## IAM Users
IAM users represent individual people or identities. Each user can have:
- Console login password
- Access keys for CLI or API usage

Created a test IAM user with limited permissions and console access.

## IAM Groups
Groups are used to manage permissions for multiple users at once. Instead of assigning permissions to each user separately, permissions can be attached to a group and users are added to that group.

Example I tried:
Created a group with S3 read-only policy and added the user to it.

## IAM Roles
Roles are different from users. They are not meant for people to log in. Roles are assumed by AWS services or applications.

Example use cases:
- EC2 instance accessing S3
- Lambda accessing DynamoDB

Important point: roles are temporary and assumed when needed.

## Policies
Policies are permission documents written in JSON format. They define:
- Effect (Allow or Deny)
- Action (what operation)
- Resource (on which service/resource)

I reviewed a managed policy and observed how actions and resources are listed.

## Permission Logic
IAM follows this rule:
- Explicit Deny always overrides Allow
- If there is no Allow, access is denied by default

This makes permission control strict by default.

## Hands-on Practice
What I did today:
- Created an IAM user with console access
- Attached S3 ReadOnly policy
- Logged in using that user
- Verified that S3 was accessible
- Verified that EC2 creation was not allowed

This helped confirm that policies are enforced correctly.

## Root Account Note
Root account has full access and should not be used for daily work. Best practice is to create an admin IAM user and use that instead.

## Key Takeaways
- IAM controls authentication and authorization in AWS
- Users are for people, roles are for services
- Groups simplify permission management
- Least privilege is the recommended approach
