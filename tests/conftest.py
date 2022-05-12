"""This makes the test configuration setup"""
# pylint: disable=redefined-outer-name
import os
import pytest

from app import create_app
from app.auth import login_form
from app.auth import register_form
from app.auth import create_user_form, profile_form, security_form, csv_upload


@pytest.fixture()
def app():
    """This makes the app"""
    #os.environ['FLASK_ENV'] = 'testing'
    app = create_app()
    app.config['WTF_CSRF_ENABLED'] = False
    app.config.update({
        "TESTING": True,
    })

    yield app


@pytest.fixture()
def client(app):
    """This makes the http client"""
    return app.test_client()


@pytest.fixture()
def runner(app):
    """This makes the task runner"""
    return app.test_cli_runner()


@pytest.fixture()
def new_user(client):
    user = login_form('jeff@email.com', 'Jeffrey')
    return user


@pytest.fixture()
def bad_user(client):
    user = login_form('jeff101@email.com', 'Password1')
    return user


@pytest.fixture()
def successful_registration(client):
    user = register_form('jeff@email.com', 'Jeffrey', 'Jeffrey')
    return user


@pytest.fixture()
def bad_email_register(client):
    user = register_form('jeff123@email.com', 'Jeff', 'Jeff')
    return user

@pytest.fixture()
def create_user(client):
    user = create_user_form('bob@email.com', 'Marley', 'Marley', '1')
    return user

@pytest.fixture()
def security_user(client):
    user = security_form('john@email.com', 'Lennon', 'Lennon')
    return user

@pytest.fixture()
def upload_csv_file(client):
    input = csv_upload('sample.csv')
    return input


@pytest.fixture()
def bad_upload_csv_file(client):
    input = csv_upload('sample1.csv')
    return input

@pytest.fixture()
def profile_edit(client):
    input = profile_form('Hello, this is my profile!')
    return input

@pytest.fixture()
def input_value():
    input = 39
    return input