# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mute.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_mute(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(316, 190)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(20, 20, 281, 151))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 3)
        self.rbtn_mute_only = QtWidgets.QRadioButton(self.widget)
        self.rbtn_mute_only.setChecked(True)
        self.rbtn_mute_only.setObjectName("rbtn_mute_only")
        self.gridLayout.addWidget(self.rbtn_mute_only, 1, 0, 1, 3)
        self.rbtn_mute_loop = QtWidgets.QRadioButton(self.widget)
        self.rbtn_mute_loop.setObjectName("rbtn_mute_loop")
        self.gridLayout.addWidget(self.rbtn_mute_loop, 2, 0, 1, 3)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 2)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 3, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 3, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.widget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 4, 1, 1, 3)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.getData)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.rbtn_mute_only.toggled.connect(Dialog.cho_only)
        self.rbtn_mute_loop.toggled.connect(Dialog.cho_loop)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "模式:"))
        self.label_3.setText(_translate("Dialog", "1.仅执行一次静音\n"
"2.循环执行,固定时间执行一次静音"))
        self.rbtn_mute_only.setText(_translate("Dialog", "仅执行一次"))
        self.rbtn_mute_loop.setText(_translate("Dialog", "循环执行"))
        self.label_2.setText(_translate("Dialog", "循环间隔:"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "300"))
        self.label_4.setText(_translate("Dialog", "秒"))
