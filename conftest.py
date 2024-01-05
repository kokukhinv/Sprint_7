import pytest
from data_generator import *
from staticdata import Links


@pytest.fixture()
def create_and_delete_courier():
    login_pass, response = register_new_courier_and_return_login_password()
    yield login_pass, response

    courier_login_data = {'login': login_pass[0], 'password': login_pass[1]}
    courier_id = requests.post(Links.main + Links.login, data=courier_login_data).json()['id']
    requests.delete(Links.main + Links.login + str(courier_id))
