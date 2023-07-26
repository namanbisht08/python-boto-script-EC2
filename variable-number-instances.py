import boto3
import argparse

def initialize_ec2_client():
    access_key = 'your_access_key_here'
    secret_key = 'your_secret_key_here'
    region = 'us-east-1'
    return boto3.client('ec2', region_name=region, aws_access_key_id=access_key, aws_secret_access_key=secret_key)

def start_ec2_instance(instance_ids):
    ec2_client = initialize_ec2_client()
    try:
        response = ec2_client.start_instances(InstanceIds=instance_ids)
        for instance_id in instance_ids:
            print(f"Instance {instance_id} is starting.")
    except Exception as e:
        for instance_id in instance_ids:
            print(f"Error starting instance {instance_id}: {str(e)}")

def stop_ec2_instance(instance_ids):
    ec2_client = initialize_ec2_client()
    try:
        response = ec2_client.stop_instances(InstanceIds=instance_ids)
        for instance_id in instance_ids:
            print(f"Instance {instance_id} is stopping.")
    except Exception as e:
        for instance_id in instance_ids:
            print(f"Error stopping instance {instance_id}: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Start or stop EC2 instances.")
    parser.add_argument("action", choices=["start", "stop"], help="Action to perform (start or stop).")
    parser.add_argument("instance_ids", nargs="+", help="List of instance IDs to start or stop.")

    args = parser.parse_args()

    if args.action == "start":
        start_ec2_instance(args.instance_ids)
    elif args.action == "stop":
        stop_ec2_instance(args.instance_ids)
