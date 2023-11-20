from PyQt6.QtWidgets import QMessageBox


def showAlert(self, message, title='Ошибка'):
    msg = QMessageBox(self)
    msg.setWindowTitle(title)
    msg.setStyleSheet("background-color: white")
    msg.setText(message)
    msg.show()
