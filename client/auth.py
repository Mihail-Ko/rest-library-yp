import requests

from library_client_gui_auth import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from main_window import MainWindow
from api import get_token, check_auth


class AuthWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.auth_button.clicked.connect(self.auth_clicked)
        self.mainWindow = MainWindow()

    def start_main_window(self):
        self.mainWindow.show()
        self.mainWindow.initTables()
        self.close()

    def show_auth_fail(self, message='Неудачная попытка авторизации'):
        msg = QMessageBox(self)
        msg.setWindowTitle('Авторизация')
        msg.setStyleSheet("background-color: white")
        msg.setText(message)
        msg.show()

    def auth_clicked(self):
        login_line = self.login_lineEdit.text()
        password_line = self.password_lineEdit.text()
        try:
            token = get_token.getXsrf(login_line, password_line)
        except requests.exceptions.ConnectionError:
            self.show_auth_fail('Сервер недоступен')
            return
        if check_auth.checkAuth(login_line, password_line):
            self.mainWindow.initAuthVars(
                login_line,
                password_line,
                token)
            self.start_main_window()
        else:
            self.show_auth_fail()
