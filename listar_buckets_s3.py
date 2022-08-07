import localstack_client.session as boto3
client = boto3.client('s3')
response = client.list_buckets()
print(response['Buckets'])
