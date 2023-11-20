from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QSizePolicy
import util


class AddForm(QDialog):
    login_saved = ''
    password_saved = ''
    xsrf = ''

    def __init__(self, table_name, main_window):
        super().__init__()
        self.mainWindow = main_window

        layout = QVBoxLayout()

        attrs_list = util.getTableAttrs(table_name)
        attrs_ru_list = util.getTableAttrsRu(table_name)
        for attr_i in range(1, len(attrs_list)):
            attr_name = attrs_list[attr_i]
            attr_name_ru = attrs_ru_list[attr_i]

            label = QLabel(text=attr_name_ru + ':')
            label.setObjectName(attr_name + '_label')
            layout.addWidget(label)

            line_edit = QLineEdit()
            line_edit.setObjectName(attr_name + '_line_edit')
            line_edit.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum))
            line_edit.setMinimumSize(QSize(300, 30))
            layout.addWidget(line_edit)

        layout.addWidget(QLabel())  # <br>
        save_button = QPushButton('Сохранить')
        save_button.setSizePolicy(QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum))
        save_button.setMinimumSize(QSize(300, 30))
        save_button.clicked.connect(self.confirm)

        layout.addWidget(save_button)
        self.setLayout(layout)

    def initAuthVars(self, login, password, xsrf):
        self.login_saved = login
        self.password_saved = password
        self.xsrf = xsrf
