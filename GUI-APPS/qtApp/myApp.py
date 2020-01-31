from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMessageBox
from PyQt5.QtWidgets import QMainWindow, QPushButton, QToolTip, QLCDNumber
from PyQt5.QtWidgets import QDesktopWidget, QAction, QLineEdit, QCheckBox
from PyQt5.QtWidgets import QProgressBar, QComboBox, QFontDialog, QStyleFactory
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import QCoreApplication, pyqtSlot, QTime, QTimer, Qt
import matplotlib.pyplot as plt
import sys


class Window(QMainWindow):
    def __init__(self, title, startPoint, width, height):
        super(Window, self).__init__()
        QToolTip.setFont(QFont("Decorative", 10, QFont.Bold))
        self.title = title
        self.left, self.top = startPoint
        self.width = width
        self.height = height

    def initUI(self, maxWidth, maxHeight):
        self.setWindowTitle("simple app")
        self.setToolTip("main window")
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setMinimumHeight(self.height)
        self.setMaximumHeight(maxHeight)
        self.setMinimumWidth(self.width)
        self.setMaximumWidth(maxWidth)

    def initAppIcon(self, iconPath):
        appIcon = QIcon(iconPath)
        self.setWindowIcon(appIcon)

    def initMainMenu(self):
        self.statusBar()
        self.mainMenu = self.menuBar()
        self.newMenu = self.mainMenu.addMenu("new")
        self.openMenu = self.mainMenu.addMenu("open")
        self.shareMenu = self.mainMenu.addMenu("share")
        # ---------------------------------------------
        exitBtn = QAction("Exit", self)
        exitBtn.setShortcut("ctrl+Q")
        exitBtn.triggered.connect(self.close)
        self.shareMenu.addAction(exitBtn)

    def initToolBar(self):
        self.toolBar = self.addToolBar("funcy-tools")
        self.func1 = QAction(QIcon("gallery/pyLogo.png"), "func1", self)
        self.func1.triggered.connect(self.close)
        self.toolBar.addAction(self.func1)

    def initIcon(self, iconPath, iconPos):
        icon = QIcon(iconPath)
        label = QLabel("label1", self)
        label.move(*iconPos)
        # icon modes {Active, Disabled, Selected}
        pixMap = icon.pixmap(50, QIcon.Active, QIcon.On)
        label.setPixmap(pixMap)
        label.setToolTip("Python 3 Logo")

    def shutdown(self, buttonPos):
        btn = QPushButton("Quit", self)
        btn.move(*buttonPos)
        btn.clicked.connect(self.quitAssert)
        btn.setToolTip("exit the application")

    def about(self, buttonPos):
        about = QPushButton("about", self)
        about.move(*buttonPos)
        about.setToolTip("about the program")
        about.clicked.connect(self.aboutInfo)

    def aboutInfo(self):
        info = QMessageBox.about(self, "About Me", "Developer: Loay Wael\n test application")

    def textField(self, boxPos):
        self.txtBox = QLineEdit(self)
        self.txtBox.move(*boxPos)
        self.txtBox.resize(300, 25)

    def quitAssert(self):
        choice = QMessageBox.question(self, "Shutdown Confirmation",
                                      "do you want to shutdown the application?",
                                      QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            QCoreApplication.instance().quit()
        else:
            pass

    def centerWindow(self):
        qRect = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qRect.moveCenter(centerPoint)
        self.move(qRect.topLeft())

    def refresh(self, buttonPos):
        btn = QPushButton("Refresh", self)
        btn.move(*buttonPos)
        btn.resize(300, 25)
        btn.clicked.connect(self.onClick)
        btn.setToolTip("refresh the application")

    def initComboBox(self, comPos):
        self.comBox = QComboBox(self)
        self.comBox.addItem("windows-xp")
        self.comBox.addItem("windows-Vista")
        self.comBox.addItem("windows-7")
        self.comBox.move(*comPos)
        self.comBox.activated[str].connect(self.styleChoice)

    @pyqtSlot()
    def onClick(self):
        print("refresh-button is clicked")
        txtVal = self.txtBox.text()
        print("you typed: ", txtVal)
        self.txtBox.setText("")

    def initCheckBox(self, chkPos):
        self.chkBox = QCheckBox("Enlarege-Window", self)
        self.chkBox.resize(200, 50)
        self.chkBox.move(*chkPos)
        # self.chkBox.toggle()
        self.chkBox.stateChanged.connect(self.enlargeWindow)

    def enlargeWindow(self, state):
        if state == Qt.Checked:
            self.setMaximumSize(800, 600)
            self.setGeometry(100, 100, 800, 600)
        else:
            self.setMaximumSize(400, 300)

    def initProgBar(self):
        self.downBtn = QPushButton("Download", self)
        self.downBtn.move(300, 200)
        self.downBtn.clicked.connect(self.getTicks)
        self.progBar = QProgressBar(self)
        self.progBar.setGeometry(100, 150, 300, 20)

    def changeFont(self):
        self.chgFontBtn = QPushButton("change font", self)
        self.chgFontBtn.move(100, 200)
        self.screen = QLabel("None to view", self)
        self.screen.resize(300, 30)
        self.screen.move(200, 250)
        self.chgFontBtn.clicked.connect(self.fontPicker)

    def fontPicker(self):
        font, valid = QFontDialog.getFont()
        if valid:
            self.screen.setText("empty data")
            self.screen.setFont(font)

    def getTicks(self):
        comp = 0
        while comp < 100:
            comp += 0.00001
            self.progBar.setValue(comp)

    def styleChoice(self, text):
        self.screen.setText(text)
        QApplication.setStyle(QStyleFactory.create(text))


myApp = QApplication(sys.argv)
window = Window("new window", (0, 0), 500, 500)
window.initUI(500, 500)
window.centerWindow()
window.initMainMenu()
window.about((100, 300))
window.initToolBar()
window.initAppIcon("gallery/pyLogo.png")
window.initIcon("gallery/pyLogo.png", (50, 425))
window.shutdown((400, 450))
window.initProgBar()
window.initComboBox((300, 300))
window.refresh((100, 50))
window.textField((100, 100))
window.initCheckBox((150, 350))
window.changeFont()


window.show()
# img = plt.imread("gallery/pyLogo.png")
# plt.imshow(img)
# plt.show()
myApp.exec_()
sys.exit(0)
