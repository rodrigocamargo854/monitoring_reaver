import requests
import time

import os
from dotenv import load_dotenv

load_dotenv()  

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

url_alertablu = (
    "https://alertablu.blumenau.sc.gov.br/static/data/nivel_oficial.json?a=8372536"
)


def send_telegram_message(chat_id, token, message):
    base_url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(base_url)



import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


while True:
    try:
        response = requests.get(url_alertablu, verify=False)
        data = response.json()
        current_niveis_length = len(data["niveis"])
        last_nivel = data["niveis"][-1]["nivel"]

        print(last_nivel)


        if last_nivel:
            last_niveis_length = len(last_nivel["niveis"])

            if current_niveis_length > last_niveis_length:
                message = f"Houve uma atualização! Nível do rio: {last_nivel}"
                send_telegram_message(CHAT_ID, TELEGRAM_TOKEN, message)
                print(message)

        last_nivel = data
        time.sleep(300)

    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar dados: {e}")
        time.sleep(60)
