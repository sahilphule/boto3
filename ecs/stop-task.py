import boto3
import json
import values

client = boto3.client("ecs", region_name = values.aws_region)
paginator = client.get_paginator('list_tasks')

response_iterator = paginator.paginate(
    PaginationConfig = {
        'PageSize':100
    }
)

response = client.stop_task(
    cluster = values.ecs_properties["ecs-cluster-name"],
    # task = values.ecs_properties["ecs-task-definition-family-name"],
    task = '',
    reason='string'
)

# for each_page in response_iterator:
#     for each_task in each_page['taskArns']:
#         response = client.stop_task(task = each_task, cluster = values.ecs_properties["ecs-cluster-name"])

print(json.dumps(response, indent = 4, default = str))