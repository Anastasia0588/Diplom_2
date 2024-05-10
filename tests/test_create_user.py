import pytest
import requests
import allure

import urls
from helper import generate_user_creds, register_user, delete_user


class TestCreateUser:

    @allure.title('Успешное создание уникального пользователя')
    def test_create_unic_user_success(self):
        creds = generate_user_creds()
        response = register_user(creds)

        assert response.status_code == 200
        assert response.json()['success'] is True
        assert 'accessToken' in response.json()
        assert 'refreshToken' in response.json()
        assert response.json()['user']['email'] == creds['email']
        assert response.json()['user']['name'] == creds['name']

        access_token = response.json()['accessToken']
        delete_user(access_token)


    @allure.title('Создание пользователя, который уже зарегистрирован')
    def test_create_existed_user(self, user):
        response = requests.post(urls.register_url, data=user[0])

        assert response.status_code == 403
        assert response.reason == 'Forbidden'
        assert response.json()["success"] is False
        assert response.json()["message"] == "User already exists"

    @allure.title('Создание пользователя с незаполненным обязательным полем')
    @pytest.mark.parametrize('wrong_field', ['email', 'name', 'password'])
    def test_create_user_with_missed_field(self, missed_field):
        creds = generate_user_creds()
        del creds[missed_field]
        response = register_user(creds)

        assert response.status_code == 403
        assert response.reason == 'Forbidden'
        assert response.json()["success"] is False
        assert response.json()["message"] == "Email, password and name are required fields"















