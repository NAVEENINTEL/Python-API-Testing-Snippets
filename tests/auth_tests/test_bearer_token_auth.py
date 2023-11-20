import pytest
from utils.api_utils import make_api_request_bearer_token
from config.config import BASE_URL_PROD, ENDPOINT_USERS, ACCESS_TOKEN

def test_bearer_token_auth():
    url = BASE_URL_PROD + ENDPOINT_USERS
    response = make_api_request_bearer_token(url, ACCESS_TOKEN)
    assert response.status_code == 200
    # Add more assertions as needed
