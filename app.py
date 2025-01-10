from credenciais.atualizarCredenciais import SecretAWS
import json
import sys
from datetime import datetime, time
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
from credenciais.atualizarCredenciais import SecretAWS
import requests

def main(credencials):
    url = "https://www.googleapis.com/calendar/v3/calendars/primary/events"
    now = datetime.utcnow()
    formatted_date = now.strftime("%Y-%m-%dT00:00:00Z")
    headers = {
        "Authorization": f"Bearer {credencials.token}",
        "Accept": "application/json"
    }
    params = {
        "timeMin": formatted_date
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()

def enviar_mensagem(message, instance, instance_key, sender_number):
    url = f"http://44.202.236.8:8080/message/sendText/{instance}"
    payload = {
        "number": sender_number,
        "text": message,
        "delay": 2000,
    }
    headers = {
        "apikey": instance_key,
        "Content-Type": "application/json"
    }
    response = requests.request("POST", url, json=payload, headers=headers)
    return response

def criar_mensagem(evento):
    inicio = datetime.fromisoformat(evento['start']['dateTime']).strftime('%H:%M')
    fim = datetime.fromisoformat(evento['end']['dateTime']).strftime('%H:%M')

    participantes = evento.get('attendees', [])
    participantes_lista = "\n".join([f"- {p['email']}" for p in participantes]) if participantes else "Nenhum participante."

    hangout_link = evento['hangoutLink'] if 'hangoutLink' in evento else "Não há link para a chamada"

    # Construindo a mensagem
    mensagem = (
        f"*Título*: {evento['summary']}\n"
        f"*De*: {inicio}\n"
        f"*Até*: {fim}\n"
        f"*Link da Chamada*: {hangout_link}\n"
        f"*Participantes*:\n{participantes_lista}"
    )
    return mensagem

def lambda_handler(event, context):
    try:
        s = SecretAWS()
        secret = s.get_secret()
        credencials = s.get_credentials(secret)
        teste = main(credencials)
        for evento in teste.get('items', []):
            msg = criar_mensagem(evento)
            enviar_mensagem(msg, event.get('instance'), event.get('apikey'), event.get('numero'))
        return {
            'statusCode': 200,
            'body': json.dumps('Hello from Lambda!')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(str(e))
        }
    
