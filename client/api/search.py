from settings import *
import requests
import util
from api.response_handler import responseHandler


def getOne(self, table_name, id_: str, login, password):
    endpoint = API_URL + table_name + '/' + id_
    response = (requests.get(endpoint, auth=(login, password)))

    responseHandled = responseHandler(self, response)
    if responseHandled['code'] == 200:
        table_attrs = util.getTableAttrs(table_name)
        obj = []
        json_obj = responseHandled['json_obj']
        for attr in table_attrs:
            if attr == 'returned':
                if json_obj[attr]:
                    json_obj[attr] = 'Да'
                else:
                    json_obj[attr] = 'Нет'
            obj.append(json_obj[attr])
        return {
            'code': responseHandled['code'],
            'object': obj}
    else:
        return {'code': responseHandled['code']}
