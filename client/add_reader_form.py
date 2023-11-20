from PyQt6.QtWidgets import QLineEdit

from api.create import post
from settings import *
from add_form import AddForm


class AddReaderForm(AddForm):
    def __init__(self, main_window):
        super().__init__(ReaderTableName_, main_window)
        self.setWindowTitle('Добавление читателя')

    def __createJson(self):
        json = {}
        for attr_i in range(1, len(ReaderAttrs_)):
            attr_name = ReaderAttrs_[attr_i]
            field_text = self.findChild(QLineEdit, attr_name + '_line_edit').text()
            json[attr_name] = field_text
        return json

    def confirm(self):
        json = self.__createJson()
        post(self, ReaderTableName_, json, self.login_saved, self.password_saved, self.xsrf)
        self.close()
        self.mainWindow.refreshTableWid(ReaderTableName_)
