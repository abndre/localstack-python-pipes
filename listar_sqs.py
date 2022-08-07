import localstack_client.session as boto3
sqs = boto3.client('sqs')
response = sqs.list_queues()
print(response['QueueUrls'])

