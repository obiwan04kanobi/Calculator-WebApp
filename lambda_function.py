"""
    this is the python code for lambda function to be used in "AWS LAMBDA".
    "test.json" is the JSON file to be used for testing of this python code.
"""


import json


# import the AWS SDK (for Python the package name is boto3)
import boto3
# import two packages to help us with dates and date formatting
from time import gmtime, strftime

# create a DynamoDB object using the AWS SDK
dynamodb = boto3.resource('dynamodb')
# use the DynamoDB object to select our table
table = dynamodb.Table('plus_minus_db')
# store the current time in a human readable format in a variable
now = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())


def lambda_handler(event, context):
    expression = event['expression']
    result = None

    try:
        result = str(eval(expression))
    except Exception as e:
        result = 'Error: Invalid Expression'

# write result and time to the DynamoDB table using the object we instantiated and save response in a variable
    response = table.put_item(
        Item={
            'ID': str(result),
            'LatestGreetingTime':now
            })

    return {
        'statusCode': 200,
        'body': json.dumps({
            'result': result
        })
    }
