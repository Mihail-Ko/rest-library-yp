from settings import *
import requests


def getXsrf(login, password):
    endpoint = API_URL + 'book/'
    response = (requests.get(endpoint, auth=(login, password)))
    if response.status_code == 404:
        return response.cookies.get("XSRF-TOKEN")
