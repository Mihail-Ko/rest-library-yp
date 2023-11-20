from api.response_handler import responseHandler
from settings import *
import requests


def getBookBorrowing(self, page_n, endpoint_mode, login, password):
    endpoint = API_URL + 'book-borrowing/' + endpoint_mode + '?page=' + str(page_n)
    response = (requests.get(endpoint, auth=(login, password)))
    responseHandled = responseHandler(self, response)
    rows = []
    if responseHandled['code'] == 200:
        for json_obj in responseHandled['json_obj']:
            row = []
            for attr in BookBorrowingAttrs_:
                if attr == 'returned':
                    if json_obj[attr]:
                        json_obj[attr] = 'Да'
                    else:
                        json_obj[attr] = 'Нет'
                row.append(json_obj[attr])
            rows.append(row)
    return rows
