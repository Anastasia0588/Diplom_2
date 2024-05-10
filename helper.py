import random
import string

import allure
import requests

import urls


def generate_user_creds(exclude_email=False, exclude_password=False, exclude_name=False):
    credentials = {}
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for _ in range(length))
        return random_string

    if not exclude_email:
        credentials['email'] = generate_random_string(10) + '@yandex.ru'

    if not exclude_password:
        credentials['password'] = generate_random_string(10)

    if not exclude_name:
        credentials['name'] = generate_random_string(10)

    return credentials

@allure.step('Регистрация пользователя')
def register_user(payload):
    response = requests.post(urls.register_url, data=payload)
    return response

@allure.step('Удаление пользователя')
def delete_user(access_token):
    requests.delete(urls.user_url, headers={"Authorization": access_token})