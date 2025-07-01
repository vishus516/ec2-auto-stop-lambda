import boto3
import  datetime

def lambda_handler(event, context):
    
    ec2 = boto3.client('ec2')

    #Working hours
    start_hours = 1
    end_hours = 2
    current_hours = datetime.datetime.now().hour + 5.5
    if current_hours >= start_hours and current_hours <= end_hours:
        print("Working hours")
        return
    instances = ec2.describe_instances(
        Filters=[
            {
                'Name': 'instance-state-name', 'Values': ['running']
            },
            {
                'Name': 'tag:AutoStop',
                'Values': [
                    'True'
                ]
            }             
        ]
    )
    instance_ids = []
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_ids.append(instance['InstanceId'])
    if instance_ids:
        print("Stopping instances")
        ec2.stop_instances(InstanceIds=instance_ids)
        print("Stopped instances: " + str(instance_ids))
    else:
        print("No instances to stop")        
