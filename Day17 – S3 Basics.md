# Day 17 – S3 Basics

Today I focused on understanding Amazon S3 and how it is used in real-world applications.

## What is S3
Amazon S3 is an object storage service used to store and retrieve data. Unlike a traditional file system, S3 does not use directories. Files are stored as objects inside buckets, and folders are only logical prefixes.

S3 is mainly used for storing static data rather than running applications or databases.

## Buckets and Objects
- A bucket is the top-level container in S3.
- Each bucket name must be globally unique.
- An object consists of the file data, metadata, and a unique key.

Buckets are created in a specific AWS region.

## Storage Classes
S3 provides multiple storage classes based on access frequency and cost:
- Standard for frequently accessed data
- Infrequent Access for data that is not used often
- One Zone-IA for lower cost with reduced redundancy
- Glacier for long-term archival
- Glacier Deep Archive for very rarely accessed data

Choosing the correct storage class depends on how often the data is accessed.

## Access Control
By default, S3 buckets are private. Public access must be explicitly enabled using bucket policies or ACLs.

AWS blocks public access by default to prevent accidental data exposure.

## Hands-on Practice
I created an S3 bucket and uploaded a sample file to it. I verified that the file could be downloaded successfully and then deleted it.

This helped me understand how objects are managed inside a bucket.

## Use Cases
Some common use cases for S3 include:
- Storing application logs
- Backups and archival
- Hosting static websites
- Storing datasets for analytics or machine learning

## Key Takeaways
- S3 is object storage, not a file system
- Buckets are region-specific and globally unique
- Data durability in S3 is very high
- Access control should be handled carefully to avoid public exposure
