from PyQt6.QtWidgets import QLineEdit

from api.create import post
from settings import *
from add_form import AddForm


class AddBorrowingForm(AddForm):
    def __init__(self, main_window):
        super().__init__(BorrowingTableName_, main_window)
        self.setWindowTitle('Добавление выдачи')

    def __createJson(self):
        json = {}
        for attr_i in range(1, len(BorrowingAttrs_)):
            attr_name = BorrowingAttrs_[attr_i]
            field_text = self.findChild(QLineEdit, attr_name + '_line_edit').text()
            if attr_name == 'returned':
                if field_text.replace(' ', '') in ['Да', 'да', '1', '+']:
                    field_text = True
                else:
                    field_text = False
            json[attr_name] = field_text
            if attr_name in ['readerId', 'bookId']:
                if field_text.isdigit():
                    json[attr_name] = int(field_text)
        return json

    def confirm(self):
        json = self.__createJson()
        post(self, BorrowingTableName_, json, self.login_saved, self.password_saved, self.xsrf)
        self.close()
        self.mainWindow.refreshTableWid(BorrowingTableName_)
