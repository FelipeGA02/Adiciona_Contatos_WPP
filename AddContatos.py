import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Função para obter as credenciais e fazer login
def obter_credenciais():
    SCOPES = ['https://www.googleapis.com/auth/contacts']
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    # Se não há credenciais válidas, faça o login
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        # Salve as credenciais para a próxima execução
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return creds

# Função para adicionar um novo contato
def adicionar_contato(service, nome, telefone):
    try:
        contact = {
            "names": [{"givenName": nome}],
            "phoneNumbers": [{"value": telefone}]
        }
        # Adicionando o contato
        service.people().createContact(body=contact).execute()
        print(f"Contato {nome} ({telefone}) adicionado com sucesso!")
    except HttpError as err:
        print(f'Ocorreu um erro: {err}')

# Função principal
def main():
    contatos = [
    "+55 31 97171-5402", "+55 31 99526-5999", "+55 31 99973-8412",
    "+55 31 99181-0745", "+55 31 99501-1914", "+55 31 99329-6193",
    "+55 31 99978-1549", "+55 31 98400-1136", "+55 31 99292-0271",
    "+55 31 97103-4401", "+55 31 99116-5156", "+55 31 99561-1124",
    "+55 82 98870-2788", "+55 31 98651-4561", "+55 31 99180-8617",
    "+55 31 98109-8151", "+55 31 97354-5497"
    ]
    nome_padrao = "Contato WhatsApp"
    
    creds = obter_credenciais()

    # Conectar ao Google Contacts API
    service = build('people', 'v1', credentials=creds)

    for i, numero in enumerate(contatos, start=1):
        nome = f"{nome_padrao} {i}"  # Adiciona um nome padrão, como "Contato WhatsApp 1"
        adicionar_contato(service, nome, numero)

if __name__ == '__main__':
    main()
