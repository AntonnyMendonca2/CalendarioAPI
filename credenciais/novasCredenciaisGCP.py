from google_auth_oauthlib.flow import InstalledAppFlow
import requests
import logging

logging.basicConfig(filename='credentials.log', level=logging.INFO, format='%(asctime)s - %(message)s')
SCOPES = ['https://www.googleapis.com/auth/calendar']
CLIENT_SECRETS_FILE = 'client_secret_875442515862-e0430qbqij237p473legg5dens5luh2c.apps.googleusercontent.com.json'
flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
credentials = flow.run_local_server(port=0)
logging.info(f'Token: {credentials.token}')
logging.info(f'Refresh Token: {credentials.refresh_token}')