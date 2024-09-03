import hashlib
import time

# Инициализация значений
collect_amount = 500  # Значение collectAmount
# collect_seq_no =     # Начальное значение collectSeqNo
secret_key = "7be2a16a82054ee58398c5edb7ac4a5a"  # Секретный ключ для хеширования
token = 'абракаддабра'
def getInfo():
    import requests

    url = "https://api.freedurov.bot/miniapps/api/user_game_level/GetGameInfo?"

    payload = {}
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
        'authorization': f'Bearer {token}',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://app.freedurov.bot',
        'priority': 'u=1, i',
        'referer': 'https://app.freedurov.bot/',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Microsoft Edge";v="128", "Microsoft Edge WebView2";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0'
    }

    response = requests.request("GET", url, headers=headers, data=payload).json()
    return response['data']['collectSeqNo']


def sbor_coin(collect_amount, hash_code, collect_seq_no):
    import requests

    url = f"https://api.freedurov.bot/miniapps/api/user_game/collectCoin?collectAmount={collect_amount}&hashCode={hash_code}&collectSeqNo={collect_seq_no}"

    payload = f"collectAmount={collect_amount}&hashCode={hash_code}&collectSeqNo={collect_seq_no}"
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
        'authorization': f'Bearer {token}',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://app.freedurov.bot',
        'priority': 'u=1, i',
        'referer': 'https://app.freedurov.bot/',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Microsoft Edge";v="128", "Microsoft Edge WebView2";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

collect_seq_no = getInfo()

# Запуск бесконечного цикла
while True:
    # Увеличиваем collectSeqNo на 1
    collect_seq_no += 1

    # Формируем строку для хеширования
    input_str = f"{collect_amount}{collect_seq_no}{secret_key}"

    # Вычисление MD5-хешкода
    hash_code = hashlib.md5(input_str.encode()).hexdigest()

    # Запись хешкода и значения collectSeqNo в глобальные переменные (для имитации в примере используются print)
    print(f"Collect Amount: {collect_amount}")
    print(f"Collect Seq No: {collect_seq_no}")
    print(f"Hash Code: {hash_code}")

    sbor_coin(collect_amount, hash_code, collect_seq_no)
    # Задержка в 3 минуты перед следующим циклом
    time.sleep(170)  # 180 секунд = 3 минуты
