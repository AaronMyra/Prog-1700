# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\PROG1700_SourceCode\Visual_Studio_Code\w0235012-MyraA\GUI\Hello_World.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(319, 265)
        font = QtGui.QFont()
        font.setPointSize(16)
        MainWindow.setFont(font)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButtonHello = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonHello.setGeometry(QtCore.QRect(80, 90, 131, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonHello.setFont(font)
        self.pushButtonHello.setObjectName("pushButtonHello")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 91, 41))
        self.label.setObjectName("label")
        self.lineEditMessage = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditMessage.setGeometry(QtCore.QRect(120, 30, 151, 31))
        self.lineEditMessage.setObjectName("lineEditMessage")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 319, 36))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButtonHello.setText(_translate("MainWindow", "Say Hello"))
        self.label.setText(_translate("MainWindow", "Message: "))

