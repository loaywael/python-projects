from submitForm import RegForm
from PyQt5 import QtCore, QtGui, QtWidgets


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    regForm = RegForm()
    regForm.show()
    sys.exit(app.exec_())
