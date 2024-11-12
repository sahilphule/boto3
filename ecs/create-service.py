import boto3
import json
import values

client = boto3.client("ecs", region_name = values.aws_region)
clusters = client.list_clusters()
cluster_name = clusters['clusterArns'][0]

response = client.create_service(cluster = values.ecs_properties["ecs-cluster-name"],
                serviceName = values.ecs_properties["ecs-service-name"],
                taskDefinition = values.ecs_properties["ecs-task-definition-family-name"],
                desiredCount = 1,
                networkConfiguration = {
                    'awsvpcConfiguration': {
                        'subnets': values.vpc_properties["vpc-subnets"],
                        'assignPublicIp': values.vpc_properties["assign-public-ip"],
                        'securityGroups': values.vpc_properties["vpc-sgs"]
                    }
                },
                launchType = values.ecs_properties["ecs-launch-type"],
            )

print(json.dumps(response, indent = 4, default = str))