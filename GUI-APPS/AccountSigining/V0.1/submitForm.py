#
from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.uic import loadUiType
from os import path, listdir, makedirs
from form import Ui_MainWindow


MainUI = Ui_MainWindow
# MainUI, _ = loadUiType("./regForm.ui")


class RegForm(QtWidgets.QMainWindow, MainUI):
    def __init__(self):
        MainUI.__init__(self)
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.signUpBtn.clicked.connect(self._saveData)
        self.logBtn.clicked.connect(self._logIn)
        self._userName = None
        self._userMail = None
        self.__isUserLogged = False
        self.__userPassword = None
        self.dbPath = "data/regFormDB.csv"
        self.__initDB()

    def __initDB(self):
        if not path.exists(self.dbPath):
            makedirs("data")
            with open(self.dbPath, "w") as db:
                db.write("User Name,User E-Mail,User Password\n")

    def __isNameValid(self):
        if self._userName.isidentifier():
            return True
        else:
            return False

    def __isMailValid(self):
        if "@" in self._userMail and "." in self._userMail:
            mailHead, mailDomain = self._userMail.split("@")
            hostServer, mailTail = mailDomain.split(".")
            if mailHead.isidentifier() and hostServer.isidentifier() and mailTail == "com":
                return True
        else:
            print("invalid e-mail")
            return False

    def __isPassValid(self):
        if len(self.__userPassword) > 7:
            return True
        else:
            print("short password, enter more than 7 characters")
            return False

    def __isPassCorrect(self, userPass):
        if self.__userPassword() == userPass:
            return True
        else:
            print("incorrect password!")
            return False

    def _saveData(self):
        self._getNewLogFields()
        self._resetNewLogFields()
        if self.__isUserLogged:
            with open(self.dbPath, "a") as f:
                print("Created New Account")
                f.write(f"{self._userName},{self._userMail},{self.__userPassword}\n")
                self.__isUserLogged = True
            # QtCore.QCoreApplication.instance().quit()

    def _resetNewLogFields(self):
        self.newNameTxt.setText("")
        self.newMailTxt.setText("")
        self.newPassTxt.setText("")

    def _resetLogFields(self):
        self.logMailTxt.setText("")
        self.logPassTxt.setText("")

    def __resetUserInfo(self):
        self._userName = None
        self._userMail = None
        self.__isUserLogged = False
        self.__userPassword = None

    def _getNewLogFields(self):
        self._userName = self.newNameTxt.text()
        self._userMail = self.newMailTxt.text()
        self.__userPassword = self.newPassTxt.text()
        if not self.__isNameValid() or not self.__isMailValid() or not self.__isPassValid():
            self.__resetUserInfo()
        else:
            self.__isUserLogged = True

    def _getLogFields(self):
        self._userMail = self.logMailTxt.text()
        self.__userPassword = self.logPassTxt.text()
        if not self.__isMailValid():
            self.__resetUserInfo()

    def __isLoggedDataCorrect(self):
        user = self.__getUser()
        if user and self.__userPassword == user[2]:
            self._userName, self._userMail, self.__userPassword = user
            return True
        else:
            return False

    def __getUser(self):
        with open(self.dbPath, "r") as f:
            users = f.readlines()
            if users:
                for user in users:
                    user = user.strip()
                    user = user.split(",")
                    if self._userMail == user[1]:
                        return user
            else:
                return None

    def _logIn(self):
        self._getLogFields()
        self._resetLogFields()
        if self.__isLoggedDataCorrect():
            self.__isUserLogged = True
            print("Logging In")
        else:
            print("Calling Wrong Entry Dialogue")


