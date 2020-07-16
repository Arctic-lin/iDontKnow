# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pushFile.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_pushfile(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(398, 300)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 380, 261))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_srcFile = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_srcFile.setObjectName("lineEdit_srcFile")
        self.gridLayout.addWidget(self.lineEdit_srcFile, 0, 1, 1, 1)
        self.btn_srcfile_one = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_srcfile_one.setObjectName("btn_srcfile_one")
        self.gridLayout.addWidget(self.btn_srcfile_one, 0, 2, 1, 1)
        self.btn_srcfile_more = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_srcfile_more.setObjectName("btn_srcfile_more")
        self.gridLayout.addWidget(self.btn_srcfile_more, 0, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 4)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.layoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 4)
        self.lineEdit_tofile = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_tofile.setObjectName("lineEdit_tofile")
        self.lineEdit_tofile.setText("/sdcard")
        self.gridLayout.addWidget(self.lineEdit_tofile, 1, 1, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.getData)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.btn_srcfile_one.clicked.connect(Dialog.chooseSrcFile)
        self.btn_srcfile_more.clicked.connect(Dialog.chooseToFile)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "文件目录:"))
        self.label_2.setText(_translate("Dialog", "目标目录:"))
        self.btn_srcfile_one.setText(_translate("Dialog", "单个文件"))
        self.btn_srcfile_more.setText(_translate("Dialog", "文件夹"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p>因ADB传输文件的特殊性,脚本在传输文件时,</p><p><span style=\" color:#ff0000;\">文件名若存在中文,将自动改名为拼音</span></p><p>1.文件目录：可选择单个文件或目录</p><p>2.目标目录:</p><p>i.仅输入/sdcard则为文件推送到sdcard根目录下</p><p>ii.输入/sdcard/xxx,若xxx不存在则自动创建该目录</p></body></html>"))
