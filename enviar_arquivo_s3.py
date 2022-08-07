import localstack_client.session as boto3
client = boto3.client('s3')

file_name = 'teste.txt'
bucket='datalake-primario'
object_name='/input/caso/teste.txt'

client.upload_file(file_name, bucket, object_name)