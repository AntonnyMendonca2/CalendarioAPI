# CalendarioAPI

## Descrição
Este projeto é uma API para integração com o Google Calendar utilizando AWS Secrets Manager para gerenciar credenciais de forma segura.

## Estrutura do Projeto
- `hello_world/credenciais/atualizarCredenciais.py`: Script para obter e atualizar credenciais armazenadas no AWS Secrets Manager.
- `hello_world/credenciais/novasCredenciaisGCP.py`: Script para gerar novas credenciais do Google Calendar.

## Requisitos
- Python 3.6+
- Bibliotecas Python:
  - boto3
  - botocore
  - google-auth
  - google-auth-oauthlib
  - requests

## Instalação
1. Clone o repositório:
    ```sh
    git clone https://github.com/seu-usuario/CalendarioAPI.git
    cd CalendarioAPI
    ```

2. Crie um ambiente virtual e ative-o:
    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

## Configuração
1. Configure suas credenciais da AWS:
    - Siga as instruções em [AWS CLI Configuration](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html) para configurar suas credenciais da AWS.

2. Crie um segredo no AWS Secrets Manager com o nome `APICalendar` e adicione as seguintes chaves:
    - `ACCESS_TOKEN`
    - `REFRESH_TOKEN`
    - `CLIENT_ID`
    - `CLIENT_SECRET`

3. Baixe o arquivo `client_secret_*.json` do Google Cloud Console e coloque-o no diretório `hello_world/credenciais/`.

## Uso
### Atualizar Credenciais
Para obter e atualizar as credenciais armazenadas no AWS Secrets Manager, execute:
```sh
python hello_world/credenciais/atualizarCredenciais.py
```

### Gerar Novas Credenciais
Para gerar novas credenciais do Google Calendar, execute:
```sh
python hello_world/credenciais/novasCredenciaisGCP.py
```

### Adicionar Permissões do Secret Para o Lambda
no IAM da sua conta, vá para funções > clique na função lambda, em "políticas de permissão" adicione uma nova baseada no json abaixo, substitua as credenciais por suas credenciais.
```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "secretsmanager:GetSecretValue",
      "Resource": "arn:aws:secretsmanager:<REGION>:<ACCOUNT_ID>:secret:APICalendar-*" 
    }
  ]
}

```


## Logs
Os logs das operações serão armazenados no arquivo `credentials.log`.

## Referências
- [AWS SDK for Python (Boto3)](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [Google Auth Library for Python](https://google-auth.readthedocs.io/en/latest/)
- [Google Calendar API](https://developers.google.com/calendar)