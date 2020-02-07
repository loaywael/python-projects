# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 860)
        MainWindow.setMinimumSize(QtCore.QSize(480, 860))
        MainWindow.setMaximumSize(QtCore.QSize(480, 860))
        MainWindow.setStyleSheet("background-color: rgb(57, 58, 62);\n"
"font: 14pt \"Segoe UI\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_13 = QtWidgets.QFrame(self.centralwidget)
        self.frame_13.setStyleSheet("border-width: 1px;\n"
"border: none;")
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem)
        self.eqLbl = QtWidgets.QLabel(self.frame_13)
        self.eqLbl.setMinimumSize(QtCore.QSize(0, 50))
        self.eqLbl.setStyleSheet("background-color: rgba(34, 203, 152, 0.05);\n"
"font: 14pt \"Segoe UI\";\n"
"color: rgb(34, 203, 152);\n"
"")
        self.eqLbl.setIndent(25)
        self.eqLbl.setObjectName("eqLbl")
        self.verticalLayout_3.addWidget(self.eqLbl)
        self.resLbl = QtWidgets.QLabel(self.frame_13)
        self.resLbl.setMinimumSize(QtCore.QSize(0, 125))
        self.resLbl.setStyleSheet("font: 75pt \"Segoe UI\" bold;\n"
"color: rgb(255, 255, 255);")
        self.resLbl.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.resLbl.setIndent(50)
        self.resLbl.setObjectName("resLbl")
        self.verticalLayout_3.addWidget(self.resLbl)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem1)
        self.frame = QtWidgets.QFrame(self.frame_13)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.leftParenthBtn = QtWidgets.QPushButton(self.frame)
        self.leftParenthBtn.setMinimumSize(QtCore.QSize(200, 50))
        self.leftParenthBtn.setStyleSheet("QPushButton{\n"
"    image: url(:/newPrefix/icons/recBTN.png);\n"
"    background-color: transparent;\n"
"    font: 24pt \"Segoe UI\";\n"
"    color:rgb(254, 176, 41);\n"
"    border-style: solid;\n"
" }\n"
" QPushButton:pressed {\n"
"    image: url(:/newPrefix/icons/oParenSelectBtn.png);\n"
"    background-color: transparent;\n"
"    font: 24pt \"Segoe UI\";\n"
"    color:rgb(254, 176, 41);\n"
"    border-style: solid;\n"
" }\n"
"")
        self.leftParenthBtn.setObjectName("leftParenthBtn")
        self.horizontalLayout.addWidget(self.leftParenthBtn)
        spacerItem3 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.rightParenthBtn = QtWidgets.QPushButton(self.frame)
        self.rightParenthBtn.setMinimumSize(QtCore.QSize(200, 50))
        self.rightParenthBtn.setSizeIncrement(QtCore.QSize(0, 0))
        self.rightParenthBtn.setBaseSize(QtCore.QSize(0, 0))
        self.rightParenthBtn.setAutoFillBackground(False)
        self.rightParenthBtn.setStyleSheet("QPushButton{\n"
"    image: url(:/newPrefix/icons/recBTN.png);\n"
"    background-color: transparent;\n"
"    font: 24pt \"Segoe UI\";\n"
"    color:rgb(254, 176, 41);\n"
"    border-style: solid;\n"
" }\n"
" QPushButton:pressed {\n"
"    image: url(:/newPrefix/icons/oParenSelectBtn.png);\n"
"    background-color: transparent;\n"
"    font: 24pt \"Segoe UI\";\n"
"    color:rgb(254, 176, 41);\n"
"    border-style: solid;\n"
" }\n"
"")
        self.rightParenthBtn.setIconSize(QtCore.QSize(20, 20))
        self.rightParenthBtn.setFlat(False)
        self.rightParenthBtn.setObjectName("rightParenthBtn")
        self.horizontalLayout.addWidget(self.rightParenthBtn, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout_3.addWidget(self.frame)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem5)
        self.frame_12 = QtWidgets.QFrame(self.frame_13)
        self.frame_12.setStyleSheet("font: 20pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.frame_10 = QtWidgets.QFrame(self.frame_12)
        self.frame_10.setStyleSheet("font: 24pt \"Segoe UI\";\n"
"color: rgb(254, 176, 41)")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame_10)
        self.frame_2.setMinimumSize(QtCore.QSize(50, 0))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.sevenBtn = QtWidgets.QPushButton(self.frame_2)
        self.sevenBtn.setMinimumSize(QtCore.QSize(60, 60))
        self.sevenBtn.setStyleSheet("QPushButton{\n"
"    image: url(:/newPrefix/icons/nBbtn.png);\n"
"    background-color: transparent;\n"
"    font: 24pt \"Segoe UI\";\n"
"    color:rgb(254, 176, 41);\n"
"    border-style: solid;\n"
" }\n"
" QPushButton:pressed {\n"
"    image: url(:/newPrefix/icons/OselectBtn.png);\n"
"    background-color: transparent;\n"
"    font: 24pt \"Segoe UI\";\n"
"    color:rgb(254, 176, 41);\n"
"    border-style: solid;\n"
" }\n"
"")
        self.sevenBtn.setObjectName("sevenBtn")
        self.horizontalLayout_2.addWidget(self.sevenBtn)
        self.eightBtn = QtWidgets.QPushButton(self.frame_2)
        self.eightBtn.setMinimumSize(QtCore.QSize(60, 60))
        self.eightBtn.setStyleSheet("QPushButton{\n"
"    image: url(:/newPrefix/icons/nBbtn.png);\n"
"    background-color: transparent;\n"
"    font: 24pt \"Segoe UI\";\n"
"    color:rgb(254, 176, 41);\n"
"    border-style: solid;\n"
" }\n"
" QPushButton:pressed {\n"
"    image: url(:/newPrefix/icons/OselectBtn.png);\n"
"    background-color: transparent;\n"
"    font: 24pt \"Segoe UI\";\n"
"    color:rgb(254, 176, 41);\n"
"    border-style: solid;\n"
" }\n"
"")
        self.eightBtn.setObjectName("eightBtn")
        self.horizontalLayout_2.addWidget(self.eightBtn)
        self.nineBtn = QtWidgets.QPushButton(self.frame_2)
        self.nineBtn.setMinimumSize(QtCore.QSize(60, 60))
        self.nineBtn.setStyleSheet("QPushButton{\n"
"    image: url(:/newPrefix/icons/nBbtn.png);\n"
"    background-color: transparent;\n"
"    font: 24pt \"Segoe UI\";\n"
"    color:rgb(254, 176, 41);\n"
"    border-style: solid;\n"
" }\n"
" QPushButton:pressed {\n"
"    image: url(:/newPrefix/icons/OselectBtn.png);\n"
"    background-color: transparent;\n"
"    font: 24pt \"Segoe UI\";\n"
"    color:rgb(254, 176, 41);\n"
"    border-style: solid;\n"
" }\n"
"")
        self.nineBtn.setObjectName("nineBtn")
        self.horizontalLayout_2.addWidget(self.nineBtn)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame_10)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.fourBtn = QtWidgets.QPushButton(self.frame_3)
        self.fourBtn.setMinimumSize(QtCore.QSize(60, 60))
        self.fourBtn.setStyleSheet("QPushButton{\n"
"    image: url(:/newPrefix/icons/nBbtn.png);\n"
"    background-color: transparent;\n"
"    font: 24pt \"Segoe UI\";\n"
"    color:rgb(254, 176, 41);\n"
"    border-style: solid;\n"
" }\n"
" QPushButton:pressed {\n"
"    image: url(:/newPrefix/icons/OselectBtn.png);\n"
"    background-color: transparent;\n"
"    font: 24pt \"Segoe UI\";\n"
"    color:rgb(254, 176, 41);\n"
"    border-style: solid;\n"
" }\n"
"")
        self.fourBtn.setObjectName("fourBtn")
        self.horizontalLayout_3.addWidget(self.fourBtn)
        self.fiveBtn = QtWidgets.QPushButton(self.frame_3)
        self.fiveBtn.setMinimumSize(QtCore.QSize(60, 60))
        self.fiveBtn.setStyleSheet("QPushButton{\n"
"    image: url(:/newPrefix/icons/nBbtn.png);\n"
"    background-color: transparent;\n"
"    font: 24pt \"Segoe UI\";\n"
"    color:rgb(254, 176, 41);\n"
"    border-style: solid;\n"
" }\n"
" QPushButton:pressed {\n"
"    image: url(:/newPrefix/icons/OselectBtn.png);\n"
"    background-color: transparent;\n"
"    font: 24pt \"Segoe UI\";\n"
"    color:rgb(254, 176, 41);\n"
"    border-style: solid;\n"
" }\n"
"")
        self.fiveBtn.setObjectName("fiveBtn")
        self.horizontalLayout_3.addWidget(self.fiveBtn)
        self.sixBtn = QtWidgets.QPushButton(self.frame_3)
        self.sixBtn.setMinimumSize(QtCore.QSize(60, 60))
        self.sixBtn.setStyleSheet("QPushButton{\n"
"    image: url(:/newPrefix/icons/nBbtn.png);\n"
"    background-color: transparent;\n"
"    font: 24pt \"Segoe UI\";\n"
"    color:rgb(254, 176, 41);\n"
"    border-style: solid;\n"
" }\n"
" QPushButton:pressed {\n"
"    image: url(:/newPrefix/icons/OselectBtn.png);\n"
"    background-color: transparent;\n"
"    font: 24pt \"Segoe UI\";\n"
"    color:rgb(254, 176, 41);\n"
"    border-style: solid;\n"
" }\n"
"")
        self.sixBtn.setObjectName("sixBtn")
        self.horizontalLayout_3.addWidget(self.sixBtn)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame_10)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.oneBtn = QtWidgets.QPushButton(self.frame_4)
        self.oneBtn.setMinimumSize(QtCore.QSize(60, 60))
        self.oneBtn.setStyleSheet("QPushButton{\n"
"    image: url(:/newPrefix/icons/nBbtn.png);\n"
"    background-color: transparent;\n"
"    font: 24pt \"Segoe UI\";\n"
"    color:rgb(254, 176, 41);\n"
"    border-style: solid;\n"
" }\n"
" QPushButton:pressed {\n"
"    image: url(:/newPrefix/icons/OselectBtn.png);\n"
"    background-color: transparent;\n"
"    font: 24pt \"Segoe UI\";\n"
"    color:rgb(254, 176, 41);\n"
"    border-style: solid;\n"
" }\n"
"")
        self.oneBtn.setObjectName("oneBtn")
        self.horizontalLayout_4.addWidget(self.oneBtn)
        self.twoBtn = QtWidgets.QPushButton(self.frame_4)
        self.twoBtn.setMinimumSize(QtCore.QSize(60, 60))
        self.twoBtn.setStyleSheet("QPushButton{\n"
"    image: url(:/newPrefix/icons/nBbtn.png);\n"
"    background-color: transparent;\n"
"    font: 24pt \"Segoe UI\";\n"
"    color:rgb(254, 176, 41);\n"
"    border-style: solid;\n"
" }\n"
" QPushButton:pressed {\n"
"    image: url(:/newPrefix/icons/OselectBtn.png);\n"
"    background-color: transparent;\n"
"    font: 24pt \"Segoe UI\";\n"
"    color:rgb(254, 176, 41);\n"
"    border-style: solid;\n"
" }\n"
"")
        self.twoBtn.setObjectName("twoBtn")
        self.horizontalLayout_4.addWidget(self.twoBtn)
        self.threeBtn = QtWidgets.QPushButton(self.frame_4)
        self.threeBtn.setMinimumSize(QtCore.QSize(60, 60))
        self.threeBtn.setStyleSheet("QPushButton{\n"
"    image: url(:/newPrefix/icons/nBbtn.png);\n"
"    background-color: transparent;\n"
"    font: 24pt \"Segoe UI\";\n"
"    color:rgb(254, 176, 41);\n"
"    border-style: solid;\n"
" }\n"
" QPushButton:pressed {\n"
"    image: url(:/newPrefix/icons/OselectBtn.png);\n"
"    background-color: transparent;\n"
"    font: 24pt \"Segoe UI\";\n"
"    color:rgb(254, 176, 41);\n"
"    border-style: solid;\n"
" }\n"
"")
        self.threeBtn.setObjectName("threeBtn")
        self.horizontalLayout_4.addWidget(self.threeBtn)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame_10)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.zeroBtn = QtWidgets.QPushButton(self.frame_5)
        self.zeroBtn.setMinimumSize(QtCore.QSize(150, 50))
        self.zeroBtn.setStyleSheet("QPushButton{\n"
"    image: url(:/newPrefix/icons/recZBtn.png);\n"
"    background-color: transparent;\n"
"    font: 24pt \"Segoe UI\";\n"
"    color:rgb(254, 176, 41);\n"
"    border-style: solid;\n"
" }\n"
" QPushButton:pressed {\n"
"    image: url(:/newPrefix/icons/oZerSelecBtn.png);\n"
"    background-color: transparent;\n"
"    font: 24pt \"Segoe UI\";\n"
"    color:rgb(254, 176, 41);\n"
"    border-style: solid;\n"
" }\n"
"")
        self.zeroBtn.setObjectName("zeroBtn")
        self.horizontalLayout_5.addWidget(self.zeroBtn)
        self.dotBtn = QtWidgets.QPushButton(self.frame_5)
        self.dotBtn.setMinimumSize(QtCore.QSize(60, 60))
        self.dotBtn.setStyleSheet("QPushButton{\n"
"    image: url(:/newPrefix/icons/nBbtn.png);\n"
"    background-color: transparent;\n"
"    font: 24pt \"Segoe UI\";\n"
"    color:rgb(254, 176, 41);\n"
"    border-style: solid;\n"
" }\n"
" QPushButton:pressed {\n"
"    image: url(:/newPrefix/icons/OselectBtn.png);\n"
"    background-color: transparent;\n"
"    font: 24pt \"Segoe UI\";\n"
"    color:rgb(254, 176, 41);\n"
"    border-style: solid;\n"
" }\n"
"")
        self.dotBtn.setObjectName("dotBtn")
        self.horizontalLayout_5.addWidget(self.dotBtn)
        self.verticalLayout.addWidget(self.frame_5)
        self.horizontalLayout_10.addWidget(self.frame_10)
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem6)
        self.frame_11 = QtWidgets.QFrame(self.frame_12)
        self.frame_11.setStyleSheet("font: 30pt \"Segoe UI\";\n"
"")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_6 = QtWidgets.QFrame(self.frame_11)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.mulBtn = QtWidgets.QPushButton(self.frame_6)
        self.mulBtn.setMinimumSize(QtCore.QSize(60, 60))
        self.mulBtn.setStyleSheet("QPushButton{\n"
"    image: url(:/newPrefix/icons/tBtn.png);\n"
"    background-color: transparent;\n"
"    font: 30pt \"Segoe UI\";\n"
"    color:rgb(255, 255, 255);\n"
"    border-style: solid;\n"
" }\n"
" QPushButton:pressed {\n"
"    image: url(:/newPrefix/icons/OselectBtn.png);\n"
"    background-color: transparent;\n"
"    font: 30pt \"Segoe UI\";\n"
"    color:rgb(254, 176, 41);\n"
"    border-style: solid;\n"
" }\n"
"")
        self.mulBtn.setObjectName("mulBtn")
        self.horizontalLayout_6.addWidget(self.mulBtn, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem7)
        self.divBtn = QtWidgets.QPushButton(self.frame_6)
        self.divBtn.setMinimumSize(QtCore.QSize(60, 60))
        self.divBtn.setStyleSheet("QPushButton{\n"
"    image: url(:/newPrefix/icons/tBtn.png);\n"
"    background-color: transparent;\n"
"    font: 30pt \"Segoe UI\";\n"
"    color:rgb(255, 255, 255);\n"
"    border-style: solid;\n"
" }\n"
" QPushButton:pressed {\n"
"    image: url(:/newPrefix/icons/OselectBtn.png);\n"
"    background-color: transparent;\n"
"    font: 30pt \"Segoe UI\";\n"
"    color:rgb(254, 176, 41);\n"
"    border-style: solid;\n"
" }\n"
"")
        self.divBtn.setObjectName("divBtn")
        self.horizontalLayout_6.addWidget(self.divBtn, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_2.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.frame_11)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.addBtn = QtWidgets.QPushButton(self.frame_7)
        self.addBtn.setMinimumSize(QtCore.QSize(60, 60))
        self.addBtn.setStyleSheet("QPushButton{\n"
"    image: url(:/newPrefix/icons/tBtn.png);\n"
"    background-color: transparent;\n"
"    font: 30pt \"Segoe UI\";\n"
"    color:rgb(255, 255, 255);\n"
"    border-style: solid;\n"
" }\n"
" QPushButton:pressed {\n"
"    image: url(:/newPrefix/icons/OselectBtn.png);\n"
"    background-color: transparent;\n"
"    font: 30pt \"Segoe UI\";\n"
"    color:rgb(254, 176, 41);\n"
"    border-style: solid;\n"
" }\n"
"")
        self.addBtn.setObjectName("addBtn")
        self.horizontalLayout_7.addWidget(self.addBtn, 0, QtCore.Qt.AlignHCenter)
        spacerItem8 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem8)
        self.subBtn = QtWidgets.QPushButton(self.frame_7)
        self.subBtn.setMinimumSize(QtCore.QSize(60, 60))
        self.subBtn.setStyleSheet("QPushButton{\n"
"    image: url(:/newPrefix/icons/tBtn.png);\n"
"    background-color: transparent;\n"
"    font: 30pt \"Segoe UI\";\n"
"    color:rgb(255, 255, 255);\n"
"    border-style: solid;\n"
" }\n"
" QPushButton:pressed {\n"
"    image: url(:/newPrefix/icons/OselectBtn.png);\n"
"    background-color: transparent;\n"
"    font: 30pt \"Segoe UI\";\n"
"    color:rgb(254, 176, 41);\n"
"    border-style: solid;\n"
" }\n"
"")
        self.subBtn.setObjectName("subBtn")
        self.horizontalLayout_7.addWidget(self.subBtn)
        self.verticalLayout_2.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.frame_11)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.remBtn = QtWidgets.QPushButton(self.frame_8)
        self.remBtn.setMinimumSize(QtCore.QSize(60, 60))
        self.remBtn.setStyleSheet("QPushButton{\n"
"    image: url(:/newPrefix/icons/tBtn.png);\n"
"    background-color: transparent;\n"
"    font: 30pt \"Segoe UI\";\n"
"    color:rgb(255, 255, 255);\n"
"    border-style: solid;\n"
" }\n"
" QPushButton:pressed {\n"
"    image: url(:/newPrefix/icons/OselectBtn.png);\n"
"    background-color: transparent;\n"
"    font: 30pt \"Segoe UI\";\n"
"    color:rgb(254, 176, 41);\n"
"    border-style: solid;\n"
" }\n"
"")
        self.remBtn.setObjectName("remBtn")
        self.horizontalLayout_8.addWidget(self.remBtn)
        spacerItem9 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem9)
        self.delBtn = QtWidgets.QPushButton(self.frame_8)
        self.delBtn.setMinimumSize(QtCore.QSize(60, 60))
        self.delBtn.setStyleSheet("QPushButton{\n"
"    image: url(:/newPrefix/icons/Obtn.png);\n"
"    background-color: transparent;\n"
"    font: 24pt \"Segoe UI\";\n"
"    color:rgb(255, 255, 255);\n"
"    border-style: solid;\n"
" }\n"
" QPushButton:pressed {\n"
"    image: url(:/newPrefix/icons/OselectBtn.png);\n"
"    background-color: transparent;\n"
"    font: 24pt \"Segoe UI\";\n"
"    color:rgb(254, 176, 41);\n"
"    border-style: solid;\n"
" }\n"
"")
        self.delBtn.setObjectName("delBtn")
        self.horizontalLayout_8.addWidget(self.delBtn)
        self.verticalLayout_2.addWidget(self.frame_8)
        self.frame_9 = QtWidgets.QFrame(self.frame_11)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.resultBtn = QtWidgets.QPushButton(self.frame_9)
        self.resultBtn.setMinimumSize(QtCore.QSize(60, 60))
        self.resultBtn.setStyleSheet("QPushButton{\n"
"    image: url(:/newPrefix/icons/Obtn.png);\n"
"    background-color: transparent;\n"
"    font: 30pt \"Segoe UI\";\n"
"    color:rgb(255, 255, 255);\n"
"    border-style: solid;\n"
" }\n"
" QPushButton:pressed {\n"
"    image: url(:/newPrefix/icons/OselectBtn.png);\n"
"    background-color: transparent;\n"
"    font: 30pt \"Segoe UI\";\n"
"    color:rgb(254, 176, 41);\n"
"    border-style: solid;\n"
" }\n"
"")
        self.resultBtn.setObjectName("resultBtn")
        self.horizontalLayout_9.addWidget(self.resultBtn)
        spacerItem10 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem10)
        self.clrBtn = QtWidgets.QPushButton(self.frame_9)
        self.clrBtn.setMinimumSize(QtCore.QSize(60, 60))
        self.clrBtn.setStyleSheet("QPushButton{\n"
"    image: url(:/newPrefix/icons/Obtn.png);\n"
"    background-color: transparent;\n"
"    font: 24pt \"Segoe UI\";\n"
"    color:rgb(255, 255, 255);\n"
"    border-style: solid;\n"
" }\n"
" QPushButton:pressed {\n"
"    image: url(:/newPrefix/icons/OselectBtn.png);\n"
"    background-color: transparent;\n"
"    font: 24pt \"Segoe UI\";\n"
"    color:rgb(254, 176, 41);\n"
"    border-style: solid;\n"
" }\n"
"")
        self.clrBtn.setObjectName("clrBtn")
        self.horizontalLayout_9.addWidget(self.clrBtn)
        self.verticalLayout_2.addWidget(self.frame_9)
        self.horizontalLayout_10.addWidget(self.frame_11)
        self.verticalLayout_3.addWidget(self.frame_12)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem11)
        self.verticalLayout_4.addWidget(self.frame_13)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.eqLbl.setText(_translate("MainWindow", "0"))
        self.resLbl.setText(_translate("MainWindow", "0"))
        self.leftParenthBtn.setText(_translate("MainWindow", "("))
        self.rightParenthBtn.setText(_translate("MainWindow", ")"))
        self.sevenBtn.setText(_translate("MainWindow", "7"))
        self.eightBtn.setText(_translate("MainWindow", "8"))
        self.nineBtn.setText(_translate("MainWindow", "9"))
        self.fourBtn.setText(_translate("MainWindow", "4"))
        self.fiveBtn.setText(_translate("MainWindow", "5"))
        self.sixBtn.setText(_translate("MainWindow", "6"))
        self.oneBtn.setText(_translate("MainWindow", "1"))
        self.twoBtn.setText(_translate("MainWindow", "2"))
        self.threeBtn.setText(_translate("MainWindow", "3"))
        self.zeroBtn.setText(_translate("MainWindow", "0"))
        self.dotBtn.setText(_translate("MainWindow", "."))
        self.mulBtn.setText(_translate("MainWindow", "*"))
        self.divBtn.setText(_translate("MainWindow", "/"))
        self.addBtn.setText(_translate("MainWindow", "+"))
        self.subBtn.setText(_translate("MainWindow", "-"))
        self.remBtn.setText(_translate("MainWindow", "%"))
        self.delBtn.setText(_translate("MainWindow", "X"))
        self.resultBtn.setText(_translate("MainWindow", "="))
        self.clrBtn.setText(_translate("MainWindow", "AC"))
import btnRes_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
