import boto3

# Function to extract volume ID from volume ARN
def extract_volume_id(volume_arn):
    # Split the ARN using the colon ':' separator
    arn_parts = volume_arn.split(':')
    # The volume id is the last part of ARN after the 'volume/' prefix
    volume_id = arn_parts[-1].split('/')[-1]
    return volume_id

# Lambda function handler
def lambda_handler(event, context):
    # Extract the volume ARN from the event data
    volume_arn = event['resources'][0]
    # Extract the volume ID from the volume ARN
    volume_id = extract_volume_id(volume_arn)
    
    # Create an EC2 client
    ec2_client = boto3.client('ec2')
    
    # Modify the volume type to 'gp3'
    response = ec2_client.modify_volume(
        VolumeId=volume_id,  # Volume ID extracted from the ARN
        VolumeType='gp3'     # Set the volume type to 'gp3'
    )
