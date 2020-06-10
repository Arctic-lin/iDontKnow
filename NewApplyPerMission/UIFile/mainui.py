# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(394, 221)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 371, 201))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.checkbox_mute = QtWidgets.QCheckBox(self.widget)
        self.checkbox_mute.setObjectName("checkbox_mute")
        self.gridLayout.addWidget(self.checkbox_mute, 3, 2, 1, 1)
        self.pushButton_run = QtWidgets.QPushButton(self.widget)
        self.pushButton_run.setObjectName("pushButton_run")
        self.gridLayout.addWidget(self.pushButton_run, 2, 5, 1, 1)
        self.checkbox_onlyApply_2 = QtWidgets.QCheckBox(self.widget)
        self.checkbox_onlyApply_2.setObjectName("checkbox_onlyApply_2")
        self.gridLayout.addWidget(self.checkbox_onlyApply_2, 3, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 5, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.widget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 3, 1, 1, 1)
        self.checkbox_logOutput = QtWidgets.QCheckBox(self.widget)
        self.checkbox_logOutput.setObjectName("checkbox_logOutput")
        self.gridLayout.addWidget(self.checkbox_logOutput, 3, 4, 1, 1)
        self.pushButton_init = QtWidgets.QPushButton(self.widget)
        self.pushButton_init.setObjectName("pushButton_init")
        self.gridLayout.addWidget(self.pushButton_init, 0, 5, 1, 1)
        self.listView = QtWidgets.QListView(self.widget)
        self.listView.setObjectName("listView")
        self.gridLayout.addWidget(self.listView, 0, 0, 3, 5)
        self.line_3 = QtWidgets.QFrame(self.widget)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 3, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkbox_mute.setText(_translate("MainWindow", "静音"))
        self.pushButton_run.setText(_translate("MainWindow", "执行"))
        self.checkbox_onlyApply_2.setText(_translate("MainWindow", "仅授权"))
        self.checkbox_logOutput.setText(_translate("MainWindow", "屏蔽Log"))
        self.pushButton_init.setText(_translate("MainWindow", "初始化"))
