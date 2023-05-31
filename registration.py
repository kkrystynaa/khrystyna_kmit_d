import pymysql
import time
import sys
import os
from PyQt5 import QtWidgets, QtCore, QtGui
import record_proc
from reg import Ui_Form


class mywindow(QtWidgets.QMainWindow):
    number_of_samples = 1

    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon("icons/app icon.png"))
        self.ui.RecordButton.setEnabled(False)
        self.ui.AuthButton.setEnabled(False)
        self.ui.RecordButton.clicked.connect(self.Recording)
        self.ui.AuthButton.clicked.connect(self.Register)
        self.ui.CheckLogin.clicked.connect(self.CheckLogin)

    def Recording(self):
        name = self.ui.LoginForm.text()
        if (self.number_of_samples == 1):
            self.ui.RecordResult.setText("**")
            self.ui.RecordResult.adjustSize()
            record_proc.record_to_file('test.wav')
            record_proc.proc('samples' + '\\' + name + '.wav')
            self.ui.RecordResult.setText("REPEAT")
            self.ui.RecordResult.adjustSize()
            self.number_of_samples += 1
        else:
            self.ui.RecordResult.setText("**")
            self.ui.RecordResult.adjustSize()
            record_proc.record_to_file('test.wav')
            record_proc.proc('find_mfcc.wav')
            self.ui.RecordResult.setText("DONE")
            self.ui.RecordResult.adjustSize()
            self.ui.RecordButton.setEnabled(False)
            self.ui.AuthButton.setEnabled(True)

    def Register(self):
        try:
            name = self.ui.LoginForm.text()
            pas = record_proc.encrypt(self.ui.PasswordForm.text())
            con = pymysql.connect(
                host="localhost",
                user="admin",
                password="Qwerty123!@",
                database="dyplom"
            )
            dist = record_proc.find_distance('samples' + '\\' + name + '.wav', 'find_mfcc.wav')
            path = os.path.abspath(os.getcwd()) + '\samples' + '\\' + name + '.wav'
            dist = float(dist)
            with con:
                cur = con.cursor()
                sql = "INSERT INTO `users` (`username`,`audio_path`,`mfcc`) VALUES (%s,%s,%s)"
                cur.execute(sql, (name, path, dist))
                sql = "INSERT INTO `passwords` (`username`,`encrypted_password`) VALUES (%s,%s)"
                cur.execute(sql, (name, pas))
                con.commit()
            self.ui.RecordResult.setText("YOU ARE REGISTERED")
            self.ui.RecordResult.adjustSize()
            self.ui.LoginForm.setEnabled(False)
            self.ui.PasswordForm.setEnabled(False)
            self.ui.AuthButton.setEnabled(False)
            self.ui.CheckLogin.setEnabled(False)

        except:
            self.ui.RecordResult.setText("Unexpected error: ", sys.exc_info()[0])
            self.ui.RecordResult.adjustSize()

    def CheckLogin(self):
        name = self.ui.LoginForm.text()
        con = pymysql.connect(
            host="localhost",
            user="admin",
            password="Qwerty123!@",
            database="dyplom"
        )
        with con:
            cur = con.cursor()
            sql = "SELECT username FROM `users` WHERE `username`= %s"
            cur.execute(sql, (name))
            rows = cur.fetchall()
            if (len(rows)) == 0:
                self.ui.RecordResult.setText("LOGIN IS AVAILABLE")
                self.ui.RecordResult.adjustSize()
                self.ui.LoginForm.setEnabled(False)
                self.ui.CheckLogin.setEnabled(False)
                self.ui.RecordButton.setEnabled(True)

            else:
                self.ui.RecordResult.setText("LOGIN IS TAKEN")
                self.ui.RecordResult.adjustSize()


def main():
    app2 = QtWidgets.QApplication([])
    application2 = mywindow()
    application2.show()
    sys.exit(app2.exec())


if __name__ == "__main__":
    main()

