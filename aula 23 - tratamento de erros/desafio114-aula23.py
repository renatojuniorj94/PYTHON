"""
Crie um programa em Python que teste se o site Pudim está acessível
pelo computador usado.
"""
"""import urllib3
try:
    resposta = urllib3.request("open", "https://ge.globo.com/")
except resposta.status != 200:
    print('O site não está acessível no momento.')
else:
    print('Consegui acessar o site com sucesso!')

print(resposta.status)"""

#O código abaixo foi fornecido pelo chatGPT
import requests

import requests
print(requests.__version__)


def check_website(url):
    try:
        response = requests.get(url)
        # Verifica se o código de status está na faixa de sucesso (200-299)
        if response.status_code == 200:
            print(f"O site {url} está acessível.")
        else:
            print(f"O site {url} retornou um código de status {response.status_code}.")
    except requests.exceptions.RequestException as e:
        print(f"Não foi possível acessar o site {url}. Erro: {e}")


# Exemplo de uso
check_website("https://www.example.com")
