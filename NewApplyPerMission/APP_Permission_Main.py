# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'APP_Permission_Main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(388, 320)
        MainWindow.setFixedSize (MainWindow.width (), MainWindow.height ())
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.checkBox_onlyapply = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_onlyapply.setGeometry(QtCore.QRect(20, 80, 131, 21))
        self.checkBox_onlyapply.setObjectName("checkBox_onlyapply")
        #self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit = QtWidgets.QTextEdit (self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 160, 341, 131))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.btn_addProject = QtWidgets.QPushButton(self.centralwidget)
        self.btn_addProject.setGeometry(QtCore.QRect(290, 30, 75, 23))
        self.btn_addProject.setObjectName("btn_addProject")
        self.btn_start = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start.setGeometry(QtCore.QRect(200, 80, 75, 23))
        self.btn_start.setObjectName("btn_start")
        self.btn_end = QtWidgets.QPushButton(self.centralwidget)
        self.btn_end.setGeometry(QtCore.QRect(290, 80, 75, 23))
        self.btn_end.setObjectName("btn_end")
        self.checkBox_mute = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_mute.setGeometry(QtCore.QRect(20, 100, 131, 21))
        self.checkBox_mute.setObjectName("checkBox_mute")
        self.checkBox_monkeylog = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_monkeylog.setGeometry(QtCore.QRect(20, 120, 131, 21))
        self.checkBox_monkeylog.setObjectName("checkBox_monkeylog")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        self.btn_addProject.clicked.connect(MainWindow.add_project)

        self.btn_start.clicked.connect(MainWindow.start_sh)
        self.btn_end.clicked.connect(MainWindow.end)
        self.checkBox_onlyapply.clicked.connect(MainWindow.only_apply)
        self.checkBox_mute.clicked.connect(MainWindow.mute_dut_script)
        self.checkBox_monkeylog.clicked.connect(MainWindow.disable_monkey_log)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "V-AppPermission"))
        MainWindow.setWindowIcon(QIcon(":/pokeballs.ico"))
        # MainWindow.setWindowOpacity(0.9)
        # MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.checkBox_onlyapply.setText(_translate("MainWindow", "仅执行授权"))
        self.btn_addProject.setText(_translate("MainWindow", "添加项目"))
        self.btn_start.setText(_translate("MainWindow", "执行"))
        self.btn_end.setText(_translate("MainWindow", "结束"))
        self.checkBox_mute.setText(_translate("MainWindow", "执行静音脚本"))
        self.checkBox_monkeylog.setText(_translate("MainWindow", "屏蔽Monkey日志输出"))


    def check_config(self):
        pass

    def set_default(self):
        pass

    def only_apply(self):
        if self.checkBox_onlyapply.isChecked ():
            self.checkBox_mute.setEnabled (False)
            self.checkBox_mute.setChecked (False)
            self.checkBox_monkeylog.setEnabled (False)
            self.checkBox_monkeylog.setChecked (False)
            return True
        else:
            self.checkBox_mute.setEnabled (True)
            self.checkBox_monkeylog.setEnabled (True)
            return False

    def mute_dut_script(self):
        if self.checkBox_mute.isChecked():
            return True
        else:
            return False

    def disable_monkey_log(self):
        if self.checkBox_monkeylog.isChecked():
            return True
        else:
            return False

    def add_project(self):
        pass