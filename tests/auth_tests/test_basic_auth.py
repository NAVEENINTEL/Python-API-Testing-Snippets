import pytest
from utils.api_utils import make_api_request_basic_auth
from config.config import BASE_URL_PROD, ENDPOINT_USERS, USERNAME, PASSWORD

def test_basic_auth():
    url = BASE_URL_PROD + ENDPOINT_USERS
    response = make_api_request_basic_auth(url, USERNAME, PASSWORD)
    assert response.status_code == 200
    # Add more assertions as needed
