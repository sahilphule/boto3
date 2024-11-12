import boto3
import json
import values

client = boto3.client("ecs", region_name = values.aws_region)
response = client.create_cluster(clusterName = values.ecs_properties["ecs-cluster-name"])
print(json.dumps(response, indent = 4))