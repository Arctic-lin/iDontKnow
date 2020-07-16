# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'userAddCommond.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_useradd(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(260, 417)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(70, 360, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(30, 20, 201, 291))
        self.listWidget.setObjectName("listWidget")
        self.btn_add = QtWidgets.QPushButton(Dialog)
        self.btn_add.setGeometry(QtCore.QRect(140, 320, 41, 23))
        self.btn_add.setObjectName("btn_add")
        self.btn_delete = QtWidgets.QPushButton(Dialog)
        self.btn_delete.setGeometry(QtCore.QRect(190, 320, 41, 23))
        self.btn_delete.setObjectName("btn_delete")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.btn_add.clicked.connect(Dialog.addAdb)
        self.btn_delete.clicked.connect(Dialog.deleteAdb)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_add.setText(_translate("Dialog", "+"))
        self.btn_delete.setText(_translate("Dialog", "-"))
