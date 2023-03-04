import requests
import json


def get_file(url):
    """Запрос json-файла"""
    file = requests.get(url)

    return file.text


def get_json(file):
    """Перевод из json"""
    file = json.loads(file)

    return file
