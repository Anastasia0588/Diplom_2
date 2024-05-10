# Diplom_2 
## Задание 2: API
ручки API для [Stellar Burgers](https://stellarburgers.nomoreparties.site/)

[Документация API](https://code.s3.yandex.net/qa-automation-engineer/python-full/diploma/api-documentation.pdf?etag=3403196b527ca03259bfd0cb41163a89)

## Тесты
test_create_user.py - тесты создания пользователя  
test_login_user.py - тесты авторизации пользователя  
test_edit_user_data.py - тесты на создание заказа  
test_get_user_order.py - тесты получения заказов пользователя  

### Запустить тесты
запустить все тесты:
```bash
pytest -v tests
```
зпустить все тесты с генерацией отчетов  
```bash
pytest tests --alluredir=allure_results 
```