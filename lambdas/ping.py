import os
import json
import logging
from uuid import uuid4
from boto3 import Session

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# S3 bucket
session = Session()
BUCKET = session.resource('s3').Bucket(os.environ['BUCKET'])
# dynamo table
DATA_TABLE = session.resource('dynamodb').Table(os.environ['DATA_TABLE'])

def _prepare_for_batch(items):
    for item in items:
        item['id'] = uuid4().hex  # Give it a unique id

        # Flatten data
        item['subClassTitle'] = item['subClass']['title']
        item['subClassCode'] = item['subClass']['code']
        del item['subClass']

        # Remove empty values
        yield {key: value for key, value in item.items() if value}


def main(event, context):
    logger.info(f"Event: {json.dumps(event)}")
    response = event

    # 1. Read s3 file
    obj = BUCKET.Object('mybasiq-transactions.json')
    body = json.loads(obj.get()['Body'].read())

    # 2. Do some changes
    # TODO: Some code here

    # 3. Write to DDB
    # Write each transaction into the table
    with DATA_TABLE.batch_writer() as batch:
        for transaction in _prepare_for_batch(body['transactions']):
            batch.put_item(Item=transaction)

    return "Done!"

if __name__ == '__main__':
    main({}, {})


