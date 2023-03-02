import requests
import json


def get_file():
    """Запрос json-файла"""
    url = 'https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1677855931612&signature=5nrWIGfZVRtxWi-9I7q1HaMn8SoWxtbpxFYn7ztvtus&downloadName=operations.json'
    file = requests.get(url)

    return file.text


def get_json(file):
    """Перевод из json"""
    file = json.loads(file)

    return file
