import pytest

from tests.data import *
from utils import get_authenticated_client

@pytest.mark.django_db
class TestUsers:
    pytestmark = pytest.mark.django_db

    def test_signup(self, client, db):
        response = client.post('/api/v1/auth/signup/', data=user_data, content_type=content_type)
        assert response.status_code == 201
        assert response.data == {'id': 1}

    def test_login(self, client, signup):
        response = client.post('/api/v1/auth/login/', data=user_data, content_type=content_type)
        assert response.status_code == 200
        assert 'token' in response.data

    def test_login_fail(self, client):
        response = client.post('/api/v1/auth/login/', data=user_data, content_type=content_type)
        assert response.status_code == 400
        assert 'token' not in response.data

    def test_logout_unauthorized(self, client):
        response = client.post('/api/v1/auth/logout/')
        assert response.status_code == 401

    def test_logout(self, client, django_user_model, signup):
        client = get_authenticated_client(user_data)
        response = client.post('/api/v1/auth/logout/', content_type=content_type)
        assert response.status_code == 204
