# Form implementation generated from reading ui file 'library_client_gui_auth.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(399, 167)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.login_lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_lineEdit.sizePolicy().hasHeightForWidth())
        self.login_lineEdit.setSizePolicy(sizePolicy)
        self.login_lineEdit.setMinimumSize(QtCore.QSize(0, 35))
        self.login_lineEdit.setText("")
        self.login_lineEdit.setObjectName("login_lineEdit")
        self.verticalLayout.addWidget(self.login_lineEdit)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.password_lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password_lineEdit.sizePolicy().hasHeightForWidth())
        self.password_lineEdit.setSizePolicy(sizePolicy)
        self.password_lineEdit.setMinimumSize(QtCore.QSize(0, 35))
        self.password_lineEdit.setText("")
        self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.verticalLayout.addWidget(self.password_lineEdit)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        self.auth_button = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.auth_button.sizePolicy().hasHeightForWidth())
        self.auth_button.setSizePolicy(sizePolicy)
        self.auth_button.setMinimumSize(QtCore.QSize(0, 35))
        self.auth_button.setObjectName("auth_button")
        self.verticalLayout.addWidget(self.auth_button)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.auth_button.setText(_translate("MainWindow", "Авторизоваться"))
