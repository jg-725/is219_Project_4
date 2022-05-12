"""This makes the test configuration setup"""
# pylint: disable=redefined-outer-name
import os
import pytest

from app import create_app
from app.auth import login_form
from app.auth import register_form


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
def new_user():
    user = login_form('jeff@email.com', 'Jeffrey')
    return user


@pytest.fixture()
def bad_user():
    user = login_form('jeff101@email.com', 'Password1')
    return user


@pytest.fixture()
def successful_registration():
    user = register_form('example@email.com', 'Password', 'Password')
    return user


@pytest.fixture()
def bad_email_register():
    user = register_form('example123@email.com', 'Password', 'Password')
    return user