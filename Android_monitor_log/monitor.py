# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'monitor.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
import resource

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(465, 285)
        MainWindow.setFixedSize(465, 285)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 20, 301, 41))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(320, 20, 131, 41))
        self.pushButton.setObjectName("pushButton")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 70, 301, 41))
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 70, 131, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 140, 54, 12))
        self.label.setObjectName("label")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(110, 140, 89, 16))
        self.radioButton.setChecked (True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(200, 140, 89, 16))
        self.radioButton.setChecked (False)
        self.radioButton_2.setObjectName("radioButton_2")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(30, 170, 121, 20))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(30, 200, 131, 16))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(30, 230, 141, 16))
        self.checkBox_3.setObjectName("checkBox_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(250, 170, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(250, 210, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton (self.centralwidget)
        self.pushButton_5.setGeometry (QtCore.QRect (390, 240, 75, 23))
        self.pushButton_5.setObjectName ("pushButton_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.get_dut_sn)
        self.pushButton_2.clicked.connect(MainWindow.save_file)
        self.pushButton_3.clicked.connect(MainWindow.start_monitor)
        self.pushButton_4.clicked.connect(MainWindow.stop_monitor)
        self.pushButton_5.clicked.connect (MainWindow.help_contact)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "V-LogMonitor"))
        MainWindow.setWindowIcon (QIcon (":/pokeballs_green.ico"))
        self.pushButton.setText(_translate("MainWindow", "查看adb已连接设备"))
        self.pushButton_2.setText(_translate("MainWindow", "保存路径"))
        self.label.setText(_translate("MainWindow", "间隔时间:"))
        self.radioButton.setText(_translate("MainWindow", "5分钟"))
        self.radioButton_2.setText(_translate("MainWindow", "1小时"))
        self.checkBox.setText(_translate("MainWindow", "dumpsys meminfo"))
        self.checkBox_2.setText(_translate("MainWindow", "cat /proc/meminfo"))
        self.checkBox_3.setText(_translate("MainWindow", "cat /proc/slabinfo"))
        self.pushButton_3.setText(_translate("MainWindow", "开始监控"))
        self.pushButton_4.setText(_translate("MainWindow", "停止监控"))
        self.pushButton_5.setText (_translate ("MainWindow", "Help"))
