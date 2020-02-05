from PyQt5 import QtWidgets, QtCore, QtGui
from calcUI import Ui_MainWindow as MainUI
from calcLogic import Calculator
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
