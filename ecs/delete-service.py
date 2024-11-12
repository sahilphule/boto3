import boto3
import json
import values

client = boto3.client("ecs", region_name = values.aws_region)
clusters = client.list_clusters()
cluster_name = values.ecs_properties["ecs-cluster-name"]
paginator = client.get_paginator('list_services')

response_iterator = paginator.paginate(
    cluster = cluster_name,
    PaginationConfig = {
        'PageSize':100
    }
)

for each_page in response_iterator:
    for each_arn in each_page['serviceArns']:
        response = client.delete_service(
            cluster = cluster_name,
            service = each_arn,
            force = True)
        print(json.dumps(response, indent = 4, default = str))