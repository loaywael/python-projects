from PyQt5 import QtWidgets, QtCore, QtGui
from calcUI import Ui_MainWindow as MainUI


class Calculator(QtWidgets.QMainWindow, MainUI):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        MainUI.__init__(self)
        self.setupUi(self)
        self._clear()
        self.dotBtn.clicked.connect(lambda: self.writeToEqScreen('.'))
        self.zeroBtn.clicked.connect(lambda: self.writeToEqScreen('0'))
        self.oneBtn.clicked.connect(lambda: self.writeToEqScreen('1'))
        self.twoBtn.clicked.connect(lambda: self.writeToEqScreen('2'))
        self.threeBtn.clicked.connect(lambda: self.writeToEqScreen('3'))
        self.fourBtn.clicked.connect(lambda: self.writeToEqScreen('4'))
        self.fiveBtn.clicked.connect(lambda: self.writeToEqScreen('5'))
        self.sixBtn.clicked.connect(lambda: self.writeToEqScreen('6'))
        self.sevenBtn.clicked.connect(lambda: self.writeToEqScreen('7'))
        self.eightBtn.clicked.connect(lambda: self.writeToEqScreen('8'))
        self.nineBtn.clicked.connect(lambda: self.writeToEqScreen('9'))
        self.mulBtn.clicked.connect(lambda: self.writeToEqScreen('*'))
        self.divBtn.clicked.connect(lambda: self.writeToEqScreen('/'))
        self.addBtn.clicked.connect(lambda: self.writeToEqScreen('+'))
        self.subBtn.clicked.connect(lambda: self.writeToEqScreen('-'))
        self.remBtn.clicked.connect(lambda: self.writeToEqScreen('%'))
        self.rightParenthBtn.clicked.connect(lambda: self.writeToEqScreen(')'))
        self.leftParenthBtn.clicked.connect(lambda: self.writeToEqScreen('('))
        self.clrBtn.clicked.connect(self._clear)
        self.resultBtn.clicked.connect(self._calcResult)
        self.delBtn.clicked.connect(self._delete)

    def writeToEqScreen(self, *args):
        self.eqLbl.setText(self.eqLbl.text()+"".join(args))

    def _clear(self):
        self.eqLbl.setText("0")
        self.resLbl.setText("0")

    def _delete(self):
        self.eqLbl.setText(self.eqLbl.text()[:-1])

    def _cleanZeros(self, equation):
        if not equation.startswith('0'):
            return equation
        else:
            equation = equation[1:]
            return self._cleanZeros(equation)

    def _calcResult(self):
        text = self.eqLbl.text()
        if text:
            equation = self._cleanZeros(text)
            result = str(eval(equation))
            self.resLbl.setText(result)
            self.eqLbl.setText("0")
