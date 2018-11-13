
import json
import boto3

from decouple import config

session = boto3.Session(
            aws_access_key_id=config('AWS_ACCESS_KEY'),
            aws_secret_access_key=config('AWS_SECRET_KEY'),
            region_name=config('AWS_REGION_DEFAULT')
        )

sns = session.client('sns')

message = {}

response = sns.publish(
    TargetArn=config('AWS_SNS_ARN'),
    Message=json.dumps({'default': json.dumps(message)}),
    MessageStructure='json'
)
