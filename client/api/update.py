from api.response_handler import responseHandler
from settings import *
import requests


def put(self, table_name, json, login, password, token):
    endpoint = API_URL + table_name
    response = (requests.post(
        endpoint,
        auth=(login, password),
        headers={"X-XSRF-TOKEN": token},
        cookies={"XSRF-TOKEN": token},
        json=json
    ))

    responseHandler(self, response)
