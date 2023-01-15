import boto3
import json

ec2_client = boto3.client('ec2')

response = ec2_client.run_instances(
    ImageId = 'ami-076e3a557efe1aa9c',
    InstanceType = 't2.micro',
    KeyName = 'training_mumbai_import',
    MinCount = 1,
    MaxCount = 1
)

instanceID = response['Instances'][0]['InstanceId']
print(f"Instance created (ID = {instanceID})")
print(f"Waiting for the instance (ID = {instanceID}) to move from Pending to Running state")
waiter = ec2_client.get_waiter('instance_running')
waiter.wait(InstanceIds=[instanceID])
print(f"Instance {instanceID} is running now.")
response = ec2_client.describe_instances(InstanceIds=[instanceID])
#print(json.dumps(response, indent=2, sort_keys=True, default=str))
publicIP = response['Reservations'][0]['Instances'][0]['NetworkInterfaces'][0]['Association']['PublicIp']
publicIPdns = response['Reservations'][0]['Instances'][0]['NetworkInterfaces'][0]['Association']['PublicDnsName']
26
print(f"Public IP Address = {publicIP}")
print(f"Public DNS Name = {publicIPdns}")

