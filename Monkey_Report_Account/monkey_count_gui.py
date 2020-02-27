# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'monkey_count.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog,QApplication
import sys

class Ui_Form(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 150)
        self.lineEdit = QtWidgets.QLineEdit(MainWindow)
        self.lineEdit.setGeometry(QtCore.QRect(30, 30, 261, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(MainWindow)
        self.pushButton.setGeometry(QtCore.QRect(300, 30, 75, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 80, 131, 41))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.get_dir)
        self.pushButton_2.clicked.connect(MainWindow.start)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Dir"))
        self.pushButton_2.setText(_translate("MainWindow", "Analysis"))

    def get_dir(self):
        log_dir = QFileDialog.getExistingDirectory (self, "Choose Dir", "./")
        self.lineEdit.setText (log_dir)
        return log_dir

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ui_Form()
    window.show()
    sys.exit(app.exec_())