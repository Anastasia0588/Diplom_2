import pytest

from helper import register_user, delete_user, generate_user_creds


@pytest.fixture(scope='function')
def user():
    payload = generate_user_creds()
    response = register_user(payload)
    access_token = response.json()['accessToken']
    yield payload, access_token
    if response.status_code == 200:
        delete_user(access_token)


