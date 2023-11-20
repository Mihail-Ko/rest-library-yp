from alert import showAlert
from settings import *
import requests


def __parseStrResponse(text):
    text = text.replace('[', '').replace(']', '')
    str_list = []
    for string in text.split('","'):
        str_list.append(string.replace('"', ''))
    str_list = list(filter(None, str_list))
    for i in range(len(str_list)):
        str_list[i] = str_list[i].split(',')
    return str_list


def getStatistic(self, limit, login, password):
    endpoint = API_URL + 'statistic' + '?limit=' + str(limit)
    response = (requests.get(endpoint, auth=(login, password)))
    rows = []
    if response.status_code == 200:
        rows = __parseStrResponse(response.text)
    elif response.status_code == 400:
        showAlert(self, 'Некорректный запрос', '400')
    return rows


def getStatisticByPeriod(self, limit, period: str, login, password):
    endpoint = API_URL + 'statistic/period' + '?limit=' + str(limit) + '&date=' + period
    response = (requests.get(endpoint, auth=(login, password)))
    rows = []
    if response.status_code == 200:
        rows = __parseStrResponse(response.text)
    elif response.status_code == 400:
        showAlert(self, 'Некорректный запрос', '400')
    return rows
