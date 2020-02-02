#
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUiType
from os import path, listdir


MainUI, _ = loadUiType("regForm/regForm.ui")


class RegForm(QtWidgets.QMainWindow, MainUI):
    def __init__(self):
        MainUI.__init__(self)
        QtWidgets.QMainWindow.__init__(self)
        self.initDB()
        self.setupUi(self)
        self.submit.clicked.connect(self.saveData)

    def initDB(self):
        self.dbPath = "regForm/regFormDB.csv"
        if not path.exists(self.dbPath):
            with open(self.dbPath, "w") as db:
                db.write("User Name, User E-Mail, User Password\n")

    def saveData(self):
        self.userName = self.nameTxt.text()
        self.userMail = self.mailTxt.text()
        self.userPassword = self.passwordTxt.text()
        with open(self.dbPath, "a") as f:
            f.write(f"{self.userName}, {self.userMail}, {self.userPassword}\n")
        self.nameTxt.setText("")
        self.mailTxt.setText("")
        self.passwordTxt.setText("")
        # QtCore.QCoreApplication.instance().quit()
