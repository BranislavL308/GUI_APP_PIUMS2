# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindowUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButtonON = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonON.setObjectName("pushButtonON")
        self.gridLayout.addWidget(self.pushButtonON, 1, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tabTerminal = QtWidgets.QWidget()
        self.tabTerminal.setObjectName("tabTerminal")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tabTerminal)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textEdit = QtWidgets.QTextEdit(self.tabTerminal)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_2.addWidget(self.textEdit, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabTerminal, "")
        self.tabPlot = QtWidgets.QWidget()
        self.tabPlot.setObjectName("tabPlot")
        self.tabWidget.addTab(self.tabPlot, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.pushButtonOFF = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonOFF.setObjectName("pushButtonOFF")
        self.gridLayout.addWidget(self.pushButtonOFF, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuUART = QtWidgets.QMenu(self.menubar)
        self.menuUART.setObjectName("menuUART")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionStart = QtWidgets.QAction(MainWindow)
        self.actionStart.setObjectName("actionStart")
        self.actionStop = QtWidgets.QAction(MainWindow)
        self.actionStop.setObjectName("actionStop")
        self.menuUART.addAction(self.actionSettings)
        self.menuUART.addAction(self.actionStart)
        self.menuUART.addAction(self.actionStop)
        self.menubar.addAction(self.menuUART.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButtonON.setText(_translate("MainWindow", "LED ON"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTerminal), _translate("MainWindow", "Terminal"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabPlot), _translate("MainWindow", "Plot"))
        self.pushButtonOFF.setText(_translate("MainWindow", "LED OFF"))
        self.menuUART.setTitle(_translate("MainWindow", "UART"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionStart.setText(_translate("MainWindow", "Start"))
        self.actionStop.setText(_translate("MainWindow", "Stop"))
