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
counter = 1
for each_page in response_iterator:
    for each_task in each_page['taskArns']:
        print(each_task)