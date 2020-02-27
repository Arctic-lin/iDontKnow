# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'APP_Permission_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from getconfigs import GetConfigs
from PyQt5.QtGui import QIcon


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.cfg = GetConfigs()
        Dialog.setObjectName("Dialog")
        Dialog.resize(287, 258)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.Add_Project_Name_Label = QtWidgets.QLabel(Dialog)
        self.Add_Project_Name_Label.setGeometry(QtCore.QRect(20, 10, 54, 20))
        self.Add_Project_Name_Label.setObjectName("Add_Project_Name_Label")
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setEnabled(True)
        self.checkBox.setGeometry(QtCore.QRect(20, 80, 201, 21))
        self.checkBox.setObjectName("checkBox")
        self.add_project_adb = QtWidgets.QTextEdit(Dialog)
        self.add_project_adb.setEnabled(False)
        self.add_project_adb.setGeometry(QtCore.QRect(20, 110, 251, 101))
        self.add_project_adb.setObjectName("add_project_adb")
        self.add_project_adb.setPlaceholderText("需添加的adb指令请用';'来区分步骤\n如input keyevent 3;slepp 3")
        self.ok_btn = QtWidgets.QPushButton(Dialog)
        self.ok_btn.setGeometry(QtCore.QRect(120, 220, 75, 23))
        self.ok_btn.setObjectName("ok_btn")
        self.cancel_btn = QtWidgets.QPushButton(Dialog)
        self.cancel_btn.setGeometry(QtCore.QRect(200, 220, 75, 23))
        self.cancel_btn.setObjectName("cancel_btn")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(70, 10, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setMaxLength (16)
        lineedit_rule = QtCore.QRegExp ("^\w+$")
        lineedit_vali = QtGui.QRegExpValidator (lineedit_rule, self.lineEdit)
        self.lineEdit.setValidator (lineedit_vali)
        self.checkBox_onlyapply = QtWidgets.QCheckBox(Dialog)
        self.checkBox_onlyapply.setGeometry(QtCore.QRect(20, 41, 131, 20))
        self.checkBox_onlyapply.setObjectName("checkBox_onlyapply")
        self.checkBox_mute = QtWidgets.QCheckBox(Dialog)
        self.checkBox_mute.setGeometry(QtCore.QRect(120, 40, 131, 21))
        self.checkBox_mute.setObjectName("checkBox_mute")
        self.checkBox_monkeylog = QtWidgets.QCheckBox(Dialog)
        self.checkBox_monkeylog.setGeometry(QtCore.QRect(20, 60, 131, 21))
        self.checkBox_monkeylog.setObjectName("checkBox_monkeylog")
        self.checkBox.raise_()
        self.Add_Project_Name_Label.raise_()
        self.add_project_adb.raise_()
        self.ok_btn.raise_()
        self.cancel_btn.raise_()
        self.lineEdit.raise_()
        self.checkBox_onlyapply.raise_()
        self.checkBox_mute.raise_()
        self.checkBox_monkeylog.raise_()

        self.retranslateUi(Dialog)
        self.checkBox_onlyapply.clicked.connect(Dialog.cfg_apply)
        self.checkBox_mute.clicked.connect(Dialog.cfg_mute)
        self.checkBox_monkeylog.clicked.connect(Dialog.cfg_monkeylog)
        self.checkBox.clicked.connect(Dialog.cfg_enable_adb)
        self.ok_btn.clicked.connect(Dialog.add_project_ok)
        self.cancel_btn.clicked.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "添加项目"))
        Dialog.setWindowIcon(QIcon("pokeballs.ico"))
        self.Add_Project_Name_Label.setText(_translate("Dialog", "项目名:"))
        self.checkBox.setWhatsThis(_translate("Dialog", "<html><head/><body><p>在授权脚本执行结束后是否需要顺便添加额外的adb指令?</p></body></html>"))
        self.checkBox.setText(_translate("Dialog", "是否添加的额外指令"))
        self.ok_btn.setText(_translate("Dialog", "OK"))
        self.cancel_btn.setText(_translate("Dialog", "Cancel"))
        self.checkBox_onlyapply.setText(_translate("Dialog", "仅执行授权"))
        self.checkBox_mute.setText(_translate("Dialog", "执行静音脚本"))
        self.checkBox_monkeylog.setText(_translate("Dialog", "屏蔽Monkey日志输出"))


    def cfg_apply(self):
        if self.child.checkBox_onlyapply.isChecked ():
            self.child.checkBox_monkeylog.setEnabled (False)
            self.child.checkBox_monkeylog.setChecked (False)
            self.child.checkBox_mute.setEnabled (False)
            self.child.checkBox_mute.setChecked (False)
            self.child.checkBox.setEnabled (False)
            self.child.checkBox.setChecked (False)
            return "1"
        else:
            self.child.checkBox_monkeylog.setEnabled (True)
            self.child.checkBox_mute.setEnabled (True)
            self.child.checkBox.setEnabled (True)
            return "0"


    def cfg_mute(self):
        if self.child.checkBox_mute.isChecked ():
            return "1"
        else:
            return "0"


    def cfg_monkeylog(self):
        if self.child.checkBox_monkeylog.isChecked ():
            return "1"
        else:
            return "0"


    def cfg_enable_adb(self):
        if self.child.checkBox.isChecked ():
            self.child.checkBox_onlyapply.setEnabled (False)
            self.child.add_project_adb.setEnabled (True)
        else:
            self.child.checkBox_onlyapply.setEnabled (True)
            self.child.add_project_adb.setEnabled (False)


    def add_project_ok(self):
        project_name = self.child.lineEdit.text ()
        if project_name == "":
            button = QMessageBox.warning (self, "Warning", "项目不能为空！", QMessageBox.Yes)
            if button == QMessageBox.Yes:
                return False
        elif project_name in self.cfg.getallsection ():
            button = QMessageBox.warning (self, "Warning", "新增项目已存在！", QMessageBox.Yes)
            if button == QMessageBox.Yes:
                return False
        else:
            self.cfg.commonconfig.add_section (project_name)
        if self.child.checkBox.isChecked ():
            if self.child.add_project_adb.toPlainText () == "":
                button = QMessageBox.warning (self, "Warning", "额外指令不能为空！", QMessageBox.Yes)
                if button == QMessageBox.Yes:
                    return False
            else:
                self.cfg.commonconfig.set (project_name, "NEED_ADB", "1")
                self.cfg.commonconfig.set (project_name, "adb_content", self.child.add_project_adb.toPlainText ())
        else:
            self.cfg.commonconfig.set (project_name, "NEED_ADB", "0")
        if self.child.checkBox_onlyapply.isChecked ():
            self.cfg.commonconfig.set (project_name, "ONLY_APPLY", "1")
        else:
            self.cfg.commonconfig.set (project_name, "ONLY_APPLY", "0")
        if self.child.checkBox_mute.isChecked ():
            self.cfg.commonconfig.set (project_name, "mute_dut", "1")
        else:
            self.cfg.commonconfig.set (project_name, "mute_dut", "0")
        if self.child.checkBox_monkeylog.isChecked ():
            self.cfg.commonconfig.set (project_name, "disable_switch", "1")
        else:
            self.cfg.commonconfig.set (project_name, "disable_switch", "0")
        with open (self.cfg.config_file, "w+") as f:
            self.cfg.commonconfig.write (f)
        QMessageBox.information (self, "Success", "成功添加项目%s" % project_name, QMessageBox.Yes)
        self.accept ()