# Утилиты для работы с API.

import time
import random
import requests


def create_user(email, password, name):
    # Создание пользователя через API.
    url = "https://stellarburgers.education-services.ru/api/auth/register"
    data = {
        "email": email,
        "password": password,
        "name": name
    }
    response = requests.post(url, json=data)
    return response


def delete_user(access_token):
    # Удаление пользователя через API.
    url = "https://stellarburgers.education-services.ru/api/auth/user"
    headers = {"Authorization": access_token}
    requests.delete(url, headers=headers)


def create_email():
    # Создание уникального email.
    timestamp = int(time.time())
    random_num = random.randint(1000, 9999)
    return f"test_user_{timestamp}_{random_num}@example.com"

