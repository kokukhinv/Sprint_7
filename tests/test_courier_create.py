import allure
import pytest
import requests
from staticdata import Links, RegistrationData


class TestCourierCreation:
    @allure.title('Создание курьера с новыми данными')
    @allure.description('Проверка, что курьера можно создать')
    def test_create_new_courier_with_unique_creds(self, create_and_delete_courier):
        r = create_and_delete_courier[1]

        assert r.status_code == 201 and r.json()['ok'] is True

    @allure.title('Создание курьера с существующими данными')
    @allure.description('Проверка, что нельзя создать двух одинаковых курьеров')
    def test_create_new_courier_with_non_unique_creds(self, create_and_delete_courier):
        courier_data = {'login': create_and_delete_courier[0][0],
                        'password': create_and_delete_courier[0][1],
                        'firstName': create_and_delete_courier[0][2]}
        r = requests.post(Links.main + Links.courier, data=courier_data)

        assert r.status_code == 409 and r.json()['message'] == 'Этот логин уже используется. Попробуйте другой.'

    @allure.title('Создание курьера с неполными данными')
    @allure.description('Проверка, что, чтобы создать курьера, нужно передать в ручку все обязательные поля')
    @pytest.mark.parametrize('missed_data', [RegistrationData.no_login_data, RegistrationData.no_password_data])
    def test_create_new_courier_with_non_complete_creds(self, missed_data):
        r = requests.post(Links.main + Links.courier, data=missed_data)

        assert r.status_code == 400 and r.json()['message'] == 'Недостаточно данных для создания учетной записи'



