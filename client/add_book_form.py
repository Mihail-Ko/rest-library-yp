from PyQt6.QtWidgets import QLineEdit

from settings import *
from add_form import AddForm
from api.create import post


class AddBookForm(AddForm):
    def __init__(self, main_window):
        super().__init__(BookTableName_, main_window)
        self.setWindowTitle('Добавление книги')

    def __createJson(self):
        json = {}
        for attr_i in range(1, len(BookAttrs_)):
            attr_name = BookAttrs_[attr_i]
            field_text = self.findChild(QLineEdit, attr_name + '_line_edit').text()
            json[attr_name] = field_text
        return json

    def confirm(self):
        json = self.__createJson()
        post(self, BookTableName_, json, self.login_saved, self.password_saved, self.xsrf)
        self.close()
        self.mainWindow.refreshTableWid(BookTableName_)
