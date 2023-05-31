from PyQt5 import QtWidgets, QtCore, QtGui
import record_proc
import pymysql
import time
from auth import Ui_Form
import sys


class mywindow(QtWidgets.QMainWindow):
    number_of_attepts = 0

    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon("icons/app icon.png"))
        self.ui.RecordButton.clicked.connect(self.Recording)
        self.ui.AuthButton.clicked.connect(self.Login)
        self.ui.PasswordForm.setEnabled(False)

    def Recording(self):
        self.ui.RecordResult.setText("**")
        self.ui.RecordResult.adjustSize()
        record_proc.record_to_file('test.wav')
        record_proc.proc('try.wav')
        self.ui.RecordResult.setText("NOW LOG IN")
        self.ui.RecordResult.adjustSize()

    def Login(self):
        #con = pymysql.connect(host='localhost', user='root', password='1234', database='auth_users')
        con = pymysql.connect(
            host="localhost",
            user="admin",
            password="Qwerty123!@",
            database="dyplom"
        )
        with con:
            name = self.ui.LoginForm.text()
            cur = con.cursor()
            sql = "SELECT users.username,encrypted_password,audio_path,mfcc FROM `users` inner join `passwords` on users.username=passwords.username WHERE users.username= %s"
            cur.execute(sql, (name))
            rows = cur.fetchall()
            if (len(rows)) == 0:
                self.ui.RecordResult.setText("USER IS NOT FOUND")
                self.ui.RecordResult.adjustSize()
                return 0
        db_path = rows[0][2]
        db_dist = rows[0][3]
        if (self.number_of_attepts < 2):
            self.number_of_attepts += 1
            result_dist = record_proc.find_distance(db_path, 'try.wav')
            if (result_dist > db_dist * 1.15 or result_dist < db_dist * 0.85):
                print("Please, try again with voice.", self.number_of_attepts)
                self.ui.RecordResult.setText("TRY AGAIN")
                self.ui.RecordResult.adjustSize()
            else:
                self.ui.RecordResult.setText("LOGGED IN")
                self.ui.RecordResult.adjustSize()
                self.ui.LoginForm.setEnabled(False)
                self.ui.PasswordForm.setEnabled(False)
                self.ui.AuthButton.setEnabled(False)
                self.ui.RecordButton.setEnabled(False)
                return 0
        elif (self.number_of_attepts >= 2 and self.number_of_attepts < 5):
            self.ui.RecordButton.setEnabled(False)
            self.ui.PasswordForm.setEnabled(True)
            self.ui.RecordResult.setText("TRY WITH PASSWORD")
            self.ui.RecordResult.adjustSize()
            pas = record_proc.encrypt(self.ui.PasswordForm.text())
            if (rows[0][1] != pas):
                if (self.number_of_attepts == 2):
                    self.ui.RecordResult.setText("TRY AGAIN\nWITH PASSWORD")
                    self.ui.RecordResult.adjustSize()
                else:
                    self.ui.RecordResult.setText("TRY AGAIN")
                    self.ui.RecordResult.adjustSize()
            else:
                self.ui.RecordResult.setText("LOGGED IN")
                self.ui.RecordResult.adjustSize()
                self.ui.LoginForm.setEnabled(False)
                self.ui.PasswordForm.setEnabled(False)
                self.ui.AuthButton.setEnabled(False)
                return 0
            self.number_of_attepts += 1
        else:
            self.ui.RecordResult.setText("ACCESS DENIED")
            self.ui.RecordResult.adjustSize()
            self.ui.LoginForm.setEnabled(False)
            self.ui.PasswordForm.setEnabled(False)
            self.ui.AuthButton.setEnabled(False)


def main():
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
