import requests
import allure
import urls


class TestGetUserOrder:

    @allure.title('Получение заказа авторизованным пользователем')
    def test_get_user_order_with_auth_success(self, user, order):
        user_data, access_token = user
        response = requests.get(urls.orders_url, headers={"Authorization": access_token})

        assert response.status_code == 200
        assert response.json()["success"] is True
        assert len(response.json()["orders"]) == 1

    @allure.title('Получение заказа без авторизации')
    def test_get_user_order_without_auth_fail(self, user, order):
        response = requests.get(urls.orders_url)

        assert response.status_code == 401
        assert response.reason == 'Unauthorized'
        assert response.json()["success"] is False
        assert response.json()["message"] == "You should be authorised"
