import pytest

from helper import register_user, delete_user, generate_user_creds, ingredient_list, create_order


@pytest.fixture(scope='function')
def user():
    user_data = generate_user_creds()
    response = register_user(user_data)
    access_token = response.json()['accessToken']
    yield user_data, access_token
    if response.status_code == 200:
        delete_user(access_token)


@pytest.fixture(scope='function')
def order(user):
    user_data, access_token = user
    create_order(access_token)
