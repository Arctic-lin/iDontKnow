# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fota.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_FOTA(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(366, 178)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(30, 20, 314, 140))
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_upgrade = QtWidgets.QLabel(self.widget)
        self.label_upgrade.setObjectName("label_upgrade")
        self.gridLayout.addWidget(self.label_upgrade, 0, 0, 1, 1)
        self.lineEdit_upgrade = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_upgrade.setObjectName("lineEdit_upgrade")
        self.gridLayout.addWidget(self.lineEdit_upgrade, 0, 1, 1, 1)
        self.btn_ugSelect = QtWidgets.QPushButton(self.widget)
        self.btn_ugSelect.setObjectName("btn_ugSelect")
        self.gridLayout.addWidget(self.btn_ugSelect, 0, 2, 1, 1)
        self.label_downgrade = QtWidgets.QLabel(self.widget)
        self.label_downgrade.setObjectName("label_downgrade")
        self.gridLayout.addWidget(self.label_downgrade, 1, 0, 1, 1)
        self.lineEdit_downgrade = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_downgrade.setObjectName("lineEdit_downgrade")
        self.gridLayout.addWidget(self.lineEdit_downgrade, 1, 1, 1, 1)
        self.btn_downSelect = QtWidgets.QPushButton(self.widget)
        self.btn_downSelect.setObjectName("btn_downSelect")
        self.gridLayout.addWidget(self.btn_downSelect, 1, 2, 1, 1)
        self.label_apkfile = QtWidgets.QLabel(self.widget)
        self.label_apkfile.setObjectName("label_apkfile")
        self.gridLayout.addWidget(self.label_apkfile, 2, 0, 1, 1)
        self.lineEdit_apk = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_apk.setObjectName("lineEdit_apk")
        self.gridLayout.addWidget(self.lineEdit_apk, 2, 1, 1, 1)
        self.btn_apk = QtWidgets.QPushButton(self.widget)
        self.btn_apk.setObjectName("btn_apk")
        self.gridLayout.addWidget(self.btn_apk, 2, 2, 1, 1)
        self.label_pushdir = QtWidgets.QLabel(self.widget)
        self.label_pushdir.setObjectName("label_pushdir")
        self.gridLayout.addWidget(self.label_pushdir, 3, 0, 1, 1)
        self.lineEdit_phonedir = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_phonedir.setInputMask("")
        self.lineEdit_phonedir.setText("/sdcard")
        self.lineEdit_phonedir.setPlaceholderText("")
        self.lineEdit_phonedir.setObjectName("lineEdit_phonedir")
        self.gridLayout.addWidget(self.lineEdit_phonedir, 3, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.widget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.getData)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.btn_ugSelect.clicked.connect(Dialog.choUpFile)
        self.btn_downSelect.clicked.connect(Dialog.choDoFile)
        self.btn_apk.clicked.connect(Dialog.choApkFile)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_upgrade.setText(_translate("Dialog", "Upgrade File:"))
        self.btn_ugSelect.setText(_translate("Dialog", "..."))
        self.label_downgrade.setText(_translate("Dialog", "Downgrade File:"))
        self.btn_downSelect.setText(_translate("Dialog", "..."))
        self.label_apkfile.setText(_translate("Dialog", "APK File:"))
        self.btn_apk.setText(_translate("Dialog", "..."))
        self.label_pushdir.setText(_translate("Dialog", "Phone Dir:"))
