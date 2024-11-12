import boto3
import json
import values

client = boto3.client("ecs", region_name = values.aws_region)
response = client.register_task_definition(
        containerDefinitions = [
            {
                "name": values.ecs_properties["container-name"],
                "image": values.ecs_properties["container-image-name"],
                "cpu": 0,
                "portMappings": [],
                "essential": True,
                "environment": [],
                "mountPoints": [],
                "volumesFrom": [],
                # "logConfiguration": {
                #     "logDriver": "awslogs",
                #     "options": {
                #         "awslogs-group": "/ecs/AWSSampleApp",
                #         "awslogs-region": "ap-south-1",
                #         "awslogs-stream-prefix": "ecs"
                #     }
                # }
            }
        ],
        executionRoleArn = values.ecs_properties["ecs-task-execution-role-arn"],
        family = values.ecs_properties["ecs-task-definition-family-name"],
        networkMode = "awsvpc",
        requiresCompatibilities = [
            values.ecs_properties["ecs-launch-type"]
        ],
        cpu = "512",
        memory = "1024"
)

print(json.dumps(response, indent = 4, default = str))