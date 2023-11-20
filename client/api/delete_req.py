from api.response_handler import responseHandlerDelete
from settings import *
import requests


def delete(self, table_name, id_: str, login, password, token):
    endpoint = API_URL + table_name + '/' + id_
    response = (requests.delete(
        endpoint,
        auth=(login, password),
        headers={"X-XSRF-TOKEN": token},
        cookies={"XSRF-TOKEN": token}
    ))

    responseHandlerDelete(self, response)
