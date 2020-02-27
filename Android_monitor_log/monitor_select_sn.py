# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'monitor_select_sn.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(428, 89)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(330, 20, 81, 241))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.checkBox = QtWidgets.QCheckBox (Dialog)
        self.checkBox.setGeometry(QtCore.QRect(40, 20, 71, 16))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_2.setGeometry(QtCore.QRect(130, 20, 71, 16))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_3.setGeometry(QtCore.QRect(210, 20, 71, 16))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox (Dialog)
        self.checkBox_4.setGeometry (QtCore.QRect (40, 50, 71, 16))
        self.checkBox_4.setObjectName ("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox (Dialog)
        self.checkBox_5.setGeometry (QtCore.QRect (130, 50, 71, 16))
        self.checkBox_5.setObjectName ("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox (Dialog)
        self.checkBox_6.setGeometry (QtCore.QRect (210, 50, 71, 16))
        self.checkBox_6.setObjectName ("checkBox_6")
        self.retranslateUi(Dialog)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.buttonBox.accepted.connect(Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    # def creat_check_box(self,dut_sn=[]):
    #     if dut_sn[0]:
    #          for i in range (len (dut_sn)):
    #              self.dutcheckBox = QtWidgets.QCheckBox ()
    #              self.dutcheckBox.setGeometry (QtCore.QRect (40 + i, 20, 71, 16))
    #              self.dutcheckBox.setObjectName ("dutcheckbox")



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.checkBox.setText (_translate ("Dialog", "CheckBox"))
        self.checkBox_2.setText (_translate ("Dialog", "CheckBox"))
        self.checkBox_3.setText (_translate ("Dialog", "CheckBox"))
        self.checkBox_4.setText (_translate ("Dialog", "CheckBox"))
        self.checkBox_5.setText (_translate ("Dialog", "CheckBox"))
        self.checkBox_6.setText (_translate ("Dialog", "CheckBox"))
