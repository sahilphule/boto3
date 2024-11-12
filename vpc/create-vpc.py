import logging
import boto3
from botocore.exceptions import ClientError
import json
import values

logger = logging.getLogger()
logging.basicConfig(level = logging.INFO,
                    format = '%(asctime)s: %(levelName)s: %(message)s')
vpc_resource = boto3.resource("ec2", region_name = values.aws_region)

def create_custom_vpc(vpc_cidr_block):
    try:
        response = vpc_resource.create_vpc(CidrBlock = vpc_cidr_block,
                                           InstanceTenancy = 'default',
                                           TagSpecifications = [{
                                               'ResourceType': 'vpc',
                                               'Tags': [
                                                   {
                                                       'Key': 'Name',
                                                       'Value': values.vpc_properties["vpc-name"]
                                                   }
                                               ]
                                           }])
    except ClientError:
        logger.exception('could not create custom vpc')
        raise
    else:
        return response
    
if __name__ == '__main__':
    vpc_cidr_block = values.vpc_properties["vpc-cidr-block"]
    logger.info(f'creating a custom vpc...')
    custom_vpc = create_custom_vpc(vpc_cidr_block)
    logger.info(f'custom vpc is created with vpc id: {custom_vpc.id}')