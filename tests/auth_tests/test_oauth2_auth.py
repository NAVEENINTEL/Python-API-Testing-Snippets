import pytest
from utils.api_utils import make_api_request_oauth2
from config.config import BASE_URL_PROD, ENDPOINT_USERS, CLIENT_ID, CLIENT_SECRET

def test_oauth2_auth(oauth2_session):
    url = BASE_URL_PROD + ENDPOINT_USERS
    response = make_api_request_oauth2(url, oauth2_session)
    assert response.status_code == 200
    # Add more assertions as needed
