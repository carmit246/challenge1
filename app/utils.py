import boto3
from boto3.dynamodb.conditions import Key, Key
import os

#dynamodb_host = os.environ['DYNAMODB_HOST']
#dynamodb_host = "localhost" #"54.216.66.226"
#dynamodb = boto3.resource('dynamodb',endpoint_url='http://' + dynamodb_host + ':8000')

# session = boto3.Session(aws_access_key_id="DUMMY_ACCESS_ID",
#                         aws_secret_access_key="DUMMY_SECRET_KEY")
# dynamodb = session.resource('dynamodb', region_name='us-west-2', endpoint_url='http://localhost:8000')

def get_secret():
  session = boto3.Session(aws_access_key_id="DUMMY_ACCESS_ID",
                        aws_secret_access_key="DUMMY_SECRET_KEY")
  dynamodb = session.resource('dynamodb', region_name='us-west-2', endpoint_url='http://localhost:8000')
  table = dynamodb.Table('devops-challenge')
  resp = table.get_item(
  Key={
    'codeName' : 'thedoctor'
  })                                     
  if 'Item' in resp:
    return(resp['Item'])
  else: return("devops-challenge does not exists!")

def create_table(): 
  session = boto3.Session(aws_access_key_id="DUMMY_ACCESS_ID",
                        aws_secret_access_key="DUMMY_SECRET_KEY")
  dynamodb = session.resource('dynamodb', region_name='local', endpoint_url='http://localhost:8000')
  table = dynamodb.create_table(
      TableName='devops-challenge',
      KeySchema=[
          {
              'AttributeName': 'codeName',
              'KeyType': 'HASH'
          },
      ],
      AttributeDefinitions=[
          {
              'AttributeName': 'codeName',
              'AttributeType': 'S'
          },
      ],
      ProvisionedThroughput={
          'ReadCapacityUnits': 3,
          'WriteCapacityUnits': 3,
      }
  )
  print("Table status:", table.table_status)
  
def insert_data(): 
  session = boto3.Session(aws_access_key_id="DUMMY_ACCESS_ID",
                        aws_secret_access_key="DUMMY_SECRET_KEY")
  dynamodb = session.resource('dynamodb', region_name='us-west-2', endpoint_url='http://localhost:8000')
  table = dynamodb.Table('devops-challenge')
  table.put_item(Item={
          'codeName': 'thedoctor',
          'secretCode': 'MySecret$'
      })

#if __name__ == '__main__':
  #create_table()
  #insert_data()
  #print(get_secret())