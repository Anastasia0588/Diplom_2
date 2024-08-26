import pytest
import allure
from helper import register_user, delete_user


class TestCreateUser:

    @allure.title('Успешное создание уникального пользователя')
    def test_create_unic_user_success(self, generate_user):
        creds = generate_user
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
    def test_create_existed_user_fail(self, generate_user):
        response_1 = register_user(generate_user)
        response_2 = register_user(generate_user)

        assert response_2.status_code == 403
        assert response_2.reason == 'Forbidden'
        assert response_2.json()["success"] is False
        assert response_2.json()["message"] == "User already exists"

        access_token = response_1.json()['accessToken']
        delete_user(access_token)

    @allure.title('Создание пользователя с незаполненным обязательным полем')
    @pytest.mark.parametrize('missed_field', ['email', 'name', 'password'])
    def test_create_user_with_missed_field_fail(self, missed_field, generate_user):
        creds = generate_user
        del creds[missed_field]
        response = register_user(generate_user)
        assert response.status_code == 403
        assert response.reason == 'Forbidden'
        assert response.json()["success"] is False
        assert response.json()["message"] == "Email, password and name are required fields"
