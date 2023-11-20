from alert import showAlert


def responseHandler(self, response):
    if response.status_code == 200:
        json_response = response.json()
        return {
            'code': response.status_code,
            'json_obj': json_response}

    elif response.status_code == 404:
        showAlert(self, 'Не найдено', '404')

    elif response.status_code == 400:
        showAlert(self, 'Некорректный запрос', '400')

    return {'code': response.status_code}


def responseHandlerDelete(self, response):
    if response.status_code == 404:
        showAlert(self, 'Не найдено', '404')

    elif response.status_code == 400:
        showAlert(self, 'Некорректный запрос', '400')

    return {'code': response.status_code}


def responseHandlerCreate(self, response):
    if response.status_code == 201:
        json_response = response.json()
        showAlert(self, 'Создано с номером ' + str(json_response['id']), 'Ok')

    elif response.status_code == 404:
        showAlert(self, 'Не найдено', '404')

    elif response.status_code == 400:
        showAlert(self, 'Некорректный запрос', '400')

    return {'code': response.status_code}
