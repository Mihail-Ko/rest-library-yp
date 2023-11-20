import sys
from PyQt6.QtWidgets import QApplication
from auth import AuthWindow


def application():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    authWindow = AuthWindow()
    authWindow.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    application()
