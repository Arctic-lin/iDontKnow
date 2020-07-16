# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'installAPK.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_installAPK(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(319, 213)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 20, 301, 171))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_srcFile = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_srcFile.setObjectName("lineEdit_srcFile")
        self.gridLayout.addWidget(self.lineEdit_srcFile, 0, 1, 1, 1)
        self.btn_srcfile = QtWidgets.QPushButton(self.widget)
        self.btn_srcfile.setObjectName("btn_srcfile")
        self.gridLayout.addWidget(self.btn_srcfile, 0, 2, 1, 1)
        self.btn_multifile = QtWidgets.QPushButton(self.widget)
        self.btn_multifile.setObjectName("btn_multifile")
        self.gridLayout.addWidget(self.btn_multifile, 0, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 4)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.widget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 4)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.getData)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.btn_srcfile.clicked.connect(Dialog.chooseAPK)
        self.btn_multifile.clicked.connect(Dialog.chooseDir)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "文件目录:"))
        self.btn_srcfile.setText(_translate("Dialog", "单个文件"))
        self.btn_multifile.setText(_translate("Dialog", "目录"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">因ADB的特殊性,若APK包名存在中文时,</span></p><p><span style=\" color:#ff0000;\">将自动改名为拼音</span></p><p>单选文件时为单个安装</p><p>选择目录时为批量安装</p></body></html>"))
