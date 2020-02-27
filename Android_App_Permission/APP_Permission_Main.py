# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'APP_Permission_Main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from getconfigs import GetConfigs
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon
import resource

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(388, 320)
        MainWindow.setFixedSize (MainWindow.width (), MainWindow.height ())
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cfg = GetConfigs ()
        self.section = self.cfg.getallsection ()
        self.checkBox_onlyapply = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_onlyapply.setGeometry(QtCore.QRect(20, 80, 131, 21))
        self.checkBox_onlyapply.setObjectName("checkBox_onlyapply")
        #self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit = QtWidgets.QTextEdit (self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 160, 341, 131))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(60, 30, 131, 22))
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 61, 20))
        self.label.setObjectName("label")
        self.btn_addProject = QtWidgets.QPushButton(self.centralwidget)
        self.btn_addProject.setGeometry(QtCore.QRect(290, 30, 75, 23))
        self.btn_addProject.setObjectName("btn_addProject")
        self.btn_check_default = QtWidgets.QPushButton(self.centralwidget)
        self.btn_check_default.setGeometry(QtCore.QRect(200, 30, 75, 23))
        self.btn_check_default.setObjectName("btn_check_default")
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
        self.comboBox.addItems (self.section)
        for i in range(len(self.section)):
            if self.cfg.getstr(self.section[i],"default_check") == "1":
                self.comboBox.setCurrentIndex(i)
                self.btn_check_default.setEnabled(False)
                if self.cfg.getstr (self.section[i], "MUTE_DUT") == "1":
                    self.checkBox_mute.setChecked (True)
                if self.cfg.getstr(self.section[i],"DISABLE_SWITCH") == "1":
                    self.checkBox_monkeylog.setChecked (True)
        if self.cfg.getstr(self.comboBox.currentText(),"only_apply") == "1":
            self.checkBox_onlyapply.setChecked(True)
            self.checkBox_monkeylog.setEnabled(False)
            self.checkBox_mute.setEnabled(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        self.btn_addProject.clicked.connect(MainWindow.add_project)
        self.btn_check_default.clicked.connect (MainWindow.set_default)
        self.btn_start.clicked.connect(MainWindow.start_sh)
        self.btn_end.clicked.connect(MainWindow.end)
        self.comboBox.currentIndexChanged.connect (MainWindow.check_config)
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
        self.label.setText(_translate("MainWindow", "项目:"))
        self.btn_addProject.setText(_translate("MainWindow", "添加项目"))
        self.btn_check_default.setText(_translate("MainWindow","默认"))
        self.btn_start.setText(_translate("MainWindow", "执行"))
        self.btn_end.setText(_translate("MainWindow", "结束"))
        self.checkBox_mute.setText(_translate("MainWindow", "执行静音脚本"))
        self.checkBox_monkeylog.setText(_translate("MainWindow", "屏蔽Monkey日志输出"))


    def check_config(self):
        # 检查Config文件中的各项值
        check_combox_text = self.comboBox.currentText ()
        if self.cfg.getstr (check_combox_text, "default_check") == "0":
            self.btn_check_default.setEnabled (True)
        elif self.cfg.getstr (check_combox_text, "default_check") == "1":
            self.btn_check_default.setEnabled (False)
        if self.cfg.getstr (check_combox_text, "only_apply") == "1":
            self.checkBox_onlyapply.setChecked (True)
            self.checkBox_mute.setEnabled (False)
            self.checkBox_monkeylog.setEnabled (False)
        else:
            self.checkBox_onlyapply.setChecked (False)
            self.checkBox_mute.setEnabled (True)
            self.checkBox_monkeylog.setEnabled (True)
        if self.cfg.getstr (check_combox_text, "mute_dut") == "1":
            self.checkBox_mute.setChecked (True)
        else:
            self.checkBox_mute.setChecked (False)
        if self.cfg.getstr (check_combox_text, "disable_switch") == "1":
            self.checkBox_monkeylog.setChecked (True)
        else:
            self.checkBox_monkeylog.setChecked (False)

    def set_default(self):
        check_combox_text = self.comboBox.currentText ()
        for i in self.section:
            if i == check_combox_text:
                self.cfg.commonconfig.set (i, "DEFAULT_CHECK", "1")
                with open (self.cfg.config_file, "w+") as f:
                    self.cfg.commonconfig.write (f)
            else:
                self.cfg.commonconfig.set (i, "DEFAULT_CHECK", "0")
                with open (self.cfg.config_file, "w+") as f:
                    self.cfg.commonconfig.write (f)
        QMessageBox.information (self, "Success", "成功设置%s为默认项目" % check_combox_text, QMessageBox.Yes)
        self.btn_check_default.setEnabled (False)

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