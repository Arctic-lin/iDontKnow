# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newMainUi.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(457, 297)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 431, 251))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 4, 0, 1, 3)
        self.line = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 1, 1, 1)
        self.checkBox_disableLog = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_disableLog.setObjectName("checkBox_disableLog")
        self.gridLayout.addWidget(self.checkBox_disableLog, 0, 2, 1, 1)
        self.pushButton_start = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_start.setObjectName("pushButton_start")
        self.gridLayout.addWidget(self.pushButton_start, 2, 1, 1, 1)
        self.pushButton_init = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_init.setObjectName("pushButton_init")
        self.gridLayout.addWidget(self.pushButton_init, 2, 0, 1, 1)
        self.pushButton_stop = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.gridLayout.addWidget(self.pushButton_stop, 2, 2, 1, 1)
        self.checkBox_onlyApply = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_onlyApply.setObjectName("checkBox_onlyApply")
        self.gridLayout.addWidget(self.checkBox_onlyApply, 0, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 1, 2, 1, 1)
        self.checkBox_mute = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_mute.setObjectName("checkBox_mute")
        self.gridLayout.addWidget(self.checkBox_mute, 0, 1, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 1, 0, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 3, 0, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout.addWidget(self.line_5, 3, 1, 1, 1)
        self.line_6 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout.addWidget(self.line_6, 3, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkBox_disableLog.setText(_translate("MainWindow", "屏蔽Monkey日志"))
        self.pushButton_start.setText(_translate("MainWindow", "执行"))
        self.pushButton_init.setText(_translate("MainWindow", "初始化"))
        self.pushButton_stop.setText(_translate("MainWindow", "结束执行"))
        self.checkBox_onlyApply.setText(_translate("MainWindow", "仅授权"))
        self.checkBox_mute.setText(_translate("MainWindow", "静音"))
