#import boto3
import localstack_client.session as boto3

# Create SQS client
sqs = boto3.client('sqs')

queue_url = 'http://localhost:4566/000000000000/sample-queue'

# Receive message from SQS queue
response = sqs.receive_message(
    QueueUrl=queue_url,
    AttributeNames=[
        'SentTimestamp'
    ],
    MaxNumberOfMessages=1,
    MessageAttributeNames=[
        'All'
    ],
    VisibilityTimeout=0,
    WaitTimeSeconds=0
)

message = response['Messages'][0]
receipt_handle = message['ReceiptHandle']

delete = True

if delete:
    # Delete received message from queue
    sqs.delete_message(
        QueueUrl=queue_url,
        ReceiptHandle=receipt_handle
    )
    print('Received and deleted message: %s' % message)

else:
    print('Received: %s' % message)

if __name__ == '__main__':
    print("END")
