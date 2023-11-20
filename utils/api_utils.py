import requests

def make_api_request_basic_auth(url, username, password):
    response = requests.get(url, auth=(username, password))
    return response

def make_api_request_bearer_token(url, token):
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.get(url, headers=headers)
    return response

def make_api_request_oauth2(url, oauth2_session):
    response = oauth2_session.get(url)
    return response
