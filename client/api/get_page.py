from api.response_handler import responseHandler
from settings import *
import requests
import util


def getPage(self, table_name, page_n, login, password):
    endpoint = API_URL + table_name + '?page=' + str(page_n)
    response = (requests.get(endpoint, auth=(login, password)))
    responseHandled = responseHandler(self, response)
    rows = []
    if responseHandled['code'] == 200:
        table_attrs = util.getTableAttrs(table_name)
        for json_obj in responseHandled['json_obj']:
            row = []
            for attr in table_attrs:
                if attr == 'returned':
                    if json_obj[attr]:
                        json_obj[attr] = 'Да'
                    else:
                        json_obj[attr] = 'Нет'
                row.append(json_obj[attr])
            rows.append(row)
    return rows
