import boto3
import json
import values

client = boto3.client("ecs", region_name = values.aws_region)
ec2 = boto3.resource('ec2')

response = client.run_task(
    taskDefinition = values.ecs_properties["ecs-task-definition-family-name"],
    launchType = values.ecs_properties["ecs-launch-type"],
    cluster = values.ecs_properties["ecs-cluster-name"],
    platformVersion = 'LATEST',
    count = 1,
    networkConfiguration = {
        'awsvpcConfiguration': {
            'subnets': values.vpc_properties["vpc-subnets"],
            'assignPublicIp': values.vpc_properties["assign-public-ip"],
            'securityGroups': values.vpc_properties["vpc-sgs"]
        }
    }
)

print(json.dumps(response, indent = 4, default = str))