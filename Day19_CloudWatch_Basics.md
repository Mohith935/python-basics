# Day 19 – CloudWatch Basics

Today I explored AWS CloudWatch and learned how monitoring and alerting work for AWS resources.

## What CloudWatch Does
CloudWatch is used for monitoring AWS resources and applications. It collects metrics and logs, and allows setting alarms based on thresholds.

It helps in tracking performance and detecting issues early.

Main things CloudWatch handles:
- Metrics
- Logs
- Alarms
- Events

## Metrics
Metrics are numeric measurements collected over time.

For EC2, some default metrics available are:
- CPU utilization
- Network in/out
- Disk read/write operations
- Status checks

I opened CloudWatch metrics and viewed graphs for my EC2 instance CPU usage. The graphs are time-based and easy to filter.

## Logs
CloudWatch Logs store log data from applications and services.

Structure:
Log Group → Log Stream

Each service usually writes logs into a log group, and individual sources create log streams inside it.

I browsed existing log groups to understand how logs are organized, even though I did not configure custom logs yet.

## Alarms
CloudWatch alarms are created based on metric thresholds.

Example:
Trigger an alert if CPU usage goes above a certain percentage for a defined time period.

An alarm can:
- Send notification
- Trigger an automated action
- Be connected to auto scaling

## Hands-on Practice
Today I created a CloudWatch alarm for EC2 CPU usage.

Steps I followed:
- Selected EC2 CPUUtilization metric
- Set threshold greater than 70%
- Set evaluation period
- Created an SNS topic
- Added my email for notification
- Confirmed the subscription

This showed how alerts can be configured for resource monitoring.

## Key Learnings
- CloudWatch is central for AWS monitoring
- Metrics are collected automatically for many services
- Alarms help detect abnormal behavior
- SNS is used for sending alert notifications
- Monitoring should be configured early, not after failures

## Notes
CloudWatch is important for operations and reliability.
