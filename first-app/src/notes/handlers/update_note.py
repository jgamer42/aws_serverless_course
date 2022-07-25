import boto3
import datetime
from dotenv import load_dotenv
from utils import headers
from boto3.dynamodb.conditions import Attr
from botocore.exceptions import ClientError


def update_note(event: dict, context: object) -> dict:
    try:
        return {
            "statusCode": 200,
            "headers": headers.get_response_readers(),
            "body": "",
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": headers.get_response_readers(),
            "body": {"message": e},
        }
