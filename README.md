# Project Description

## Overview
The Cloud Engineering team is responsible for managing the AWS environment and ensuring compliance with organizational policies. To achieve this, AWS CloudWatch and AWS Lambda are utilized to govern resources based on defined policies. One specific use case involves triggering a Lambda function in response to the creation of an Amazon Elastic Block Store (EBS) volume. This is facilitated through Amazon CloudWatch Events, enabling monitoring and automated responses specifically for EBS volumes of type GP2, converting them to type GP3 as needed.

## Instructions

### 1. Create Lambda Function
- Create a Lambda function in the AWS Management Console or via AWS CLI/SDK. 
- Implement the necessary logic to handle the conversion of EBS volumes from type GP2 to GP3.

### 2. Configure CloudWatch Event
- Navigate to AWS CloudWatch Events service.
- Go to "Rules" and create a new rule.
- Specify the service name as EC2 and select the Event Type as "EBS volume Notification".
- Choose "Select Specific Event" and configure the rule accordingly.
- Add the Lambda function as the target for the rule.

### 3. Verify CloudWatch-Lambda Integration
- Create a dummy EBS volume in the AWS Management Console.
- Once the volume is created, check the log groups in CloudWatch to verify if the Lambda function is executed as expected.

### 4. Test Python Code
- Utilize the provided Python code to modify the EBS volume type from GP2 to GP3.
- Reference the boto3 documentation for the `modify_volume` method: [modify_volume](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_volume.html).

### 5. Grant Permissions to IAM Role
- Ensure that the IAM role associated with the Lambda function has the necessary permissions to interact with EBS volumes, CloudWatch Events, and other required AWS services.

## Additional Notes
- Regularly monitor and review the functionality of the Lambda function to ensure it continues to meet the desired requirements and policies.
- Document any changes or updates made to the Lambda function and associated configurations for future reference.
