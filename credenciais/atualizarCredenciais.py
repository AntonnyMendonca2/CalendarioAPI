# Use this code snippet in your app.
# If you need more information about configurations
# or implementing the sample code, visit the AWS docs:
# https://aws.amazon.com/developer/language/python/

import boto3
from botocore.exceptions import ClientError
import json
from google.oauth2.credentials import Credentials
import requests

class SecretAWS():
    def __init__(self):
        self.secret_name = "APICalendar"
        self.region_name = "us-east-1"
        self.scopes = ['https://www.googleapis.com/auth/calendar']
        return

    def get_secret(self):
        """Get the secret from AWS Secrets Manager."""
        # Create a Secrets Manager client
        session = boto3.session.Session()
        client = session.client(
            service_name='secretsmanager',
            region_name=self.region_name
        )

        try:
            get_secret_value_response = client.get_secret_value(
                SecretId=self.secret_name
            )
        except ClientError as e:
            # For a list of exceptions thrown, see
            # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
            raise e

        secret =  json.loads(get_secret_value_response['SecretString'])
        return secret
        # Your code goes here.

    def update_secret(self, new_values):
        """Update the secret with new values."""
        client = boto3.client("secretsmanager", region_name=self.region_name)
        try:
            response = client.update_secret(
                SecretId=self.secret_name,
                SecretString=json.dumps(new_values)
            )
            print(f"Segredo atualizado com sucesso: {response}")
        except Exception as e:
            print(f"Erro ao atualizar o segredo: {e}")

    def get_credentials(self, secret):
        credentials = Credentials(
            token=secret.get('ACCESS_TOKEN'),
            refresh_token=secret.get('REFRESH_TOKEN'),
            client_id=secret.get('CLIENT_ID'),
            client_secret=secret.get('CLIENT_SECRET'),
            token_uri="https://oauth2.googleapis.com/token",
        )
        if credentials.expired:
            credentials.refresh(requests.Request())
            secret['ACCESS_TOKEN'] = credentials.token
            secret['REFRESH_TOKEN'] = credentials.refresh_token
            self.update_secret(secret)
        return credentials