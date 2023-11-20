from settings import *
import requests


def checkAuth(login, password):
    endpoint = API_URL + 'book/'
    response = (requests.get(endpoint, auth=(login, password)))
    if response.status_code == 404:
        return True
    else:
        if response.status_code != 401:
            print('code:', str(response.status_code))
        return False
