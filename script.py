import boto3
import sys

def initialize_ec2_client():
    access_key = 'your_access_key_here'
    secret_key = 'your_secret_key_here'
    region = 'us-east-1'
    return boto3.client('ec2', region_name=region, aws_access_key_id=access_key, aws_secret_access_key=secret_key)


def start_ec2_instance(instance_id):
    ec2_client = initialize_ec2_client()
    try:
        response = ec2_client.start_instances(InstanceIds=[instance_id])
        print(f"Instance {instance_id} is starting.")
    except Exception as e:
        print(f"Error starting instance {instance_id}: {str(e)}")


def stop_ec2_instance(instance_id):
    ec2_client = initialize_ec2_client()
    try:
        response = ec2_client.stop_instances(InstanceIds=[instance_id])
        print(f"Instance {instance_id} is stopping.")
    except Exception as e:
        print(f"Error stopping instance {instance_id}: {str(e)}")



if __name__ == "__main__":
    instance_id = sys.argv[2]

    if len(sys.argv) > 1 and sys.argv[1] == "start":
        start_ec2_instance(instance_id)
    elif len(sys.argv) > 1 and sys.argv[1] == "stop":
        stop_ec2_instance(instance_id)
    else:
        print("Please provide a valid argument (start or stop).")
