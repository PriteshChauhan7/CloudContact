import json
import boto3
import uuid
from datetime import datetime

def lambda_handler(event, context):
    
    
    body = json.loads(event['body'])
    name = body['name']
    email = body['email']
    message = body['message']
    
    
    submission_id = str(uuid.uuid4())
    timestamp = datetime.now().isoformat()
    
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('CloudContact')
    table.put_item(Item={
        'id': submission_id,
        'name': name,
        'email': email,
        'message': message,
        'timestamp': timestamp
    })
    
    
    ses = boto3.client('ses', region_name='us-east-1')
    ses.send_email(
        Source='Priteshchauhan8265@gmail.com',
        Destination={'ToAddresses': ['Priteshchauhan8265@gmail.com']},
        Message={
            'Subject': {'Data': 'New CloudContact Submission!'},
            'Body': {'Text': {'Data': f'Name: {name}\nEmail: {email}\nMessage: {message}'}}
        }
    )
    
    
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({'message': 'Form submitted successfully!'})
    }