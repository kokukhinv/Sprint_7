import allure
import pytest
import requests
from staticdata import Links, LoginData


class TestCourierLogin:
    @allure.title('Вход курьера с корректными данными')
    @allure.description('Проверка, что курьер может авторизоваться')
    def test_authentication(self, create_and_delete_courier):
        courier_data = {'login': create_and_delete_courier[0][0],
                        'password': create_and_delete_courier[0][1]
                        }
        r = requests.post(Links.main + Links.login, data=courier_data)

        assert r.status_code == 200 and r.json()['id']

    @allure.title('Вход курьера с некорректными данными')
    @allure.description('Проверка, что система вернёт ошибку, если неправильно указать логин или пароль')
    def test_login_with_incorrect_cred(self):
        courier_data = {'login': 'asdf7634543',
                        'password': 'sdfcvzxcvasd',
                        }
        r = requests.post(Links.main + Links.login, data=courier_data)

        assert r.status_code == 404 and r.json()['message'] == 'Учетная запись не найдена'

    @allure.title('Вход курьера с неполными данными')
    @allure.description('Проверка, что для авторизации нужно передать все обязательные поля')
    @pytest.mark.parametrize('missed_data', [LoginData.no_login_data, LoginData.no_password_data])
    def test_login_with_non_complete_creds(self, missed_data):
        r = requests.post(Links.main + Links.login, data=missed_data)

        assert r.status_code == 400 and r.json()['message'] == 'Недостаточно данных для входа'