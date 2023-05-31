#import record_proc
import pymysql
import time
import sys
import os
from PyQt5 import QtWidgets, QtCore, QtGui
from reg import Ui_Form
import registration
import authentication


class StartWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(StartWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon("icons/app icon.png"))
        self.ui.RegButton.clicked.connect(self.reg_clicked)
        self.openreg = registration.mywindow()
        self.ui.AuthButton.clicked.connect(self.auth_clicked)
        self.openauth = authentication.mywindow()

    def reg_clicked(self):
        self.openreg.show()

    def auth_clicked(self):
        self.openauth.show()


def main():
    app = QtWidgets.QApplication([])
    application = StartWindow()
    application.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

