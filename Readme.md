# Personal Project AWS - localstack

Here I put some tipes to use aws and [localstack](https://docs.localstack.cloud/overview/) to 
teste codes for data engeneering.

# S3

Criando um bucket
```
awslocal s3api create-bucket --bucket datalake-primario
```

Este [script](listar_buckets_s3.py) lista os buckets.

Utilize o [script](enviar_arquivos_s3.py) para enviar arquivos e o
[script](listar_arquivos_s3.py) para listar.


Verificar arquivos no bucket
```
awslocal s3api list-objects --bucket datalake-primario
```

# SQS

Criar fila

```
awslocal sqs create-queue --queue-name sample-queue
```

Enviar mensagem para a fila

```
awslocal sqs send-message --queue-url http://localhost:4566/00000000000/sample-queue --message-body 'test'
```

Este [script](read_sqs_message.py) ajudara a ler as mensagens e deletar caso precise.

Este [script](listar_sqs.py) lista as filas criadas.

# DynamodDb

Criar tabela
```
awslocal dynamodb create-table --table-name Music --attribute-definitions \
        AttributeName=Artist,AttributeType=S \
        AttributeName=SongTitle,AttributeType=S \
    --key-schema \
        AttributeName=Artist,KeyType=HASH \
        AttributeName=SongTitle,KeyType=RANGE \
--provisioned-throughput \
        ReadCapacityUnits=10,WriteCapacityUnits=5
```

Enviar objeto
```
awslocal dynamodb put-item \
    --table-name Music  \
    --item \
        '{"Artist": {"S": "No One You Know"}, "SongTitle": {"S": "Call Me Today"}, "AlbumTitle": {"S": "Somewhat Famous"}, "Awards": {"N": "1"}}'
```

Ver objetos

```
awslocal dynamodb scan --table-name Music
```