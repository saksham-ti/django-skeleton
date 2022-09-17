from rest_framework.test import APIClient


def get_authenticated_client(user_data):
    client = APIClient()
    response = client.post('/api/v1/auth/login/', data=user_data, format='json')
    token = response.data.get('token')
    client.credentials(HTTP_AUTHORIZATION='Token ' + token)
    return client