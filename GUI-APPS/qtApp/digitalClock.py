from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QApplication
from PyQt5.QtWidgets import QLCDNumber
from PyQt5.QtCore import QTime, QTimer, pyqtSlot
import sys


class DigitalClock(QLCDNumber):
    def __init__(self):
        super(DigitalClock, self).__init__()
        self.setMinimumHeight(300)
        self.setMinimumWidth(900)
        self.initResetButton((100, 100))
        self.show()

    def initResetButton(self, btnPos):
        self.resetBtn = QPushButton("reset", self)
        self.resetBtn.move(*btnPos)
        self.resetBtn.setToolTip("reset the digital clock")


def main():
    myApp = QApplication(sys.argv)
    clk = DigitalClock()
    myApp.exec_()
    sys.exit(0)


if __name__ == "__main__":
    main()
