import logging
import boto3
from botocore.exceptions import ClientError
import json
import values

logger = logging.getLogger()
logging.basicConfig(level = logging.INFO,
                    format = '%(asctime)s: %(levelname)s: %(message)s')
vpc_client = boto3.client("ec2", region_name = values.aws_region)

def delete_vpc(vpc_id):
    try:
        response = vpc_client.delete_vpc(VpcId=vpc_id)
    except ClientError:
        logger.exception('could not delete the vpc')
        raise
    else:
        return response

if __name__ == '__main__':
    vpc_id = ''
    vpc = delete_vpc(vpc_id)
    logger.info(f'VPC {vpc_id} is deleted successfully.')