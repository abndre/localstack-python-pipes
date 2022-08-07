import localstack_client.session as boto3
client = boto3.client('s3')



file_name = 'teste.txt'
bucket='datalake-primario'
object_name='/input/caso/'

my_bucket = client.list_objects_v2(Bucket=bucket)
for obj in my_bucket['Contents']:
    print(obj['Key'])

if __name__ == '__main__':
    print("END")
