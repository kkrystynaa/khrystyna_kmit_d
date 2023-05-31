from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(373, 563)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setStyleSheet("background-color: #d7d7fa")
        self.RecordButton = QtWidgets.QPushButton(Form)
        self.RecordButton.setGeometry(QtCore.QRect(110, 420, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.RecordButton.setFont(font)
        self.RecordButton.setStyleSheet("QPushButton{\n"
                                        "background-color: #e3ffea;\n"
                                        "border-radius:15;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed{\n"
                                        "background-color: #ffffff;\n"
                                        "}")
        self.RecordButton.setObjectName("RecordButton")
        self.AuthButton = QtWidgets.QPushButton(Form)
        self.AuthButton.setGeometry(QtCore.QRect(110, 480, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.AuthButton.setFont(font)
        self.AuthButton.setStyleSheet("QPushButton{\n"
                                      "background-color: #e3ffea;\n"
                                      "border-radius:30;\n"
                                      "}\n"
                                      "QPushButton:pressed{\n"
                                      "background-color: #ffffff;\n"
                                      "}")
        self.AuthButton.setObjectName("AuthButton")
        self.RegButton = QtWidgets.QPushButton(Form)
        self.RegButton.setGeometry(QtCore.QRect(110, 480, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.RegButton.setFont(font)
        self.RegButton.setStyleSheet("QPushButton{\n"
                                      "background-color: #e3f6ea;\n"
                                      "border-radius:30;\n"
                                      "}\n"
                                      "QPushButton:pressed{\n"
                                      "background-color: #ffffff;\n"
                                      "}")
        self.RegButton.setObjectName("RegButton")
        self.LoginForm = QtWidgets.QLineEdit(Form)
        self.LoginForm.setGeometry(QtCore.QRect(120, 210, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        self.LoginForm.setFont(font)
        self.LoginForm.setStyleSheet("QLineEdit{\n"
                                     "border: 3px solid #e3ffea;\n"
                                     "border-radius: 10;\n"
                                     "}\n"
                                     "QLineEdit:focus{\n"
                                     "background: rgb(255, 255, 255);}")
        self.LoginForm.setText("")
        self.LoginForm.setObjectName("LoginForm")
        self.label_login = QtWidgets.QLabel(Form)
        self.label_login.setGeometry(QtCore.QRect(10, 210, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        self.label_login.setFont(font)
        self.label_login.setObjectName("label_login")
        self.PasswordForm = QtWidgets.QLineEdit(Form)
        self.PasswordForm.setGeometry(QtCore.QRect(120, 270, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        self.PasswordForm.setFont(font)
        self.PasswordForm.setStyleSheet("QLineEdit{\n"
                                        "border: 3px solid #e3ffea;\n"
                                        "border-radius: 10;\n"
                                        "}\n"
                                        "QLineEdit:focus{\n"
                                        "background: rgb(255, 255, 255);}")
        self.PasswordForm.setText("")
        self.PasswordForm.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PasswordForm.setClearButtonEnabled(True)
        self.PasswordForm.setObjectName("PasswordForm")
        self.label_password = QtWidgets.QLabel(Form)
        self.label_password.setGeometry(QtCore.QRect(10, 270, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")
        self.RecordResult = QtWidgets.QLabel(Form)
        self.RecordResult.setGeometry(QtCore.QRect(0, 330, 391, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RecordResult.sizePolicy().hasHeightForWidth())
        self.RecordResult.setSizePolicy(sizePolicy)
        self.RecordResult.setMinimumSize(QtCore.QSize(381, 71))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.RecordResult.setFont(font)
        self.RecordResult.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.RecordResult.setStyleSheet("color: #d45757")
        self.RecordResult.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.RecordResult.setText("")
        self.RecordResult.setTextFormat(QtCore.Qt.AutoText)
        self.RecordResult.setScaledContents(False)
        self.RecordResult.setAlignment(QtCore.Qt.AlignCenter)
        self.RecordResult.setIndent(0)
        self.RecordResult.setObjectName("RecordResult")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(-1, -1, 381, 191))
        self.frame.setStyleSheet("background-color: #ffffff")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.app_name = QtWidgets.QLabel(self.frame)
        self.app_name.setGeometry(QtCore.QRect(40, 20, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.app_name.setFont(font)
        self.app_name.setObjectName("app_name")
        self.app_icon = QtWidgets.QLabel(self.frame)
        self.app_icon.setGeometry(QtCore.QRect(100, 60, 181, 131))
        self.app_icon.setText("")
        self.app_icon.setPixmap(QtGui.QPixmap("icons/app icon.png"))
        self.app_icon.setObjectName("app_icon")
        self.CheckLogin = QtWidgets.QPushButton(Form)
        self.CheckLogin.setGeometry(QtCore.QRect(290, 210, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.CheckLogin.setFont(font)
        self.CheckLogin.setStyleSheet("QPushButton{\n"
                                      "background-color: #e3ffea;\n"
                                      "border-radius:15;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed{\n"
                                      "background-color: #ffffff;\n"
                                      "}")
        self.CheckLogin.setObjectName("CheckLogin")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Registration", "Registration"))
        self.RecordButton.setText(_translate("Form", "RECORD VOICE"))
        self.AuthButton.setText(_translate("Form", "SIGN UP"))
        self.label_login.setText(_translate("Form", "Login:"))
        self.label_password.setText(_translate("Form", "Password:"))
        self.app_name.setText(_translate("Form", "VOICE AUTHENTICATION"))
        self.CheckLogin.setText(_translate("Form", "CHECK"))
