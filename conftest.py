import pytest

from helper import register_user, delete_user, generate_user_creds


@pytest.fixture(scope='function')
def user():
    user_data = generate_user_creds()
    response = register_user(user_data)
    access_token = response.json()['accessToken']
    yield user_data, access_token
    if response.status_code == 200:
        delete_user(access_token)
