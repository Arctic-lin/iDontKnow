# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\monitor_log\venv\Scripts\ui_memory.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
import resource



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(469, 563)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 10, 341, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.btn_dir = QtWidgets.QPushButton(self.centralwidget)
        self.btn_dir.setGeometry(QtCore.QRect(370, 10, 75, 31))
        self.btn_dir.setObjectName("btn_dir")
        self.btn_getpackage = QtWidgets.QPushButton(self.centralwidget)
        self.btn_getpackage.setGeometry(QtCore.QRect(180, 50, 111, 31))
        self.btn_getpackage.setObjectName("btn_getpackage")
        self.btn_analysis = QtWidgets.QPushButton(self.centralwidget)
        self.btn_analysis.setGeometry(QtCore.QRect(180, 500, 111, 31))
        self.btn_analysis.setObjectName("btn_analysis")
        self.listWidget_all = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_all.setGeometry(QtCore.QRect(20, 90, 191, 361))
        self.listWidget_all.setObjectName("listWidget_all")
        self.listWidget_local = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_local.setGeometry(QtCore.QRect(260, 90, 191, 361))
        self.listWidget_local.setObjectName("listWidget_local")
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setGeometry(QtCore.QRect(20, 460, 191, 23))
        self.btn_add.setObjectName("btn_add")
        self.btn_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delete.setGeometry(QtCore.QRect(260, 460, 191, 23))
        self.btn_delete.setObjectName("btn_delete")
        self.label_all_package = QtWidgets.QLabel(self.centralwidget)
        self.label_all_package.setGeometry(QtCore.QRect(20, 70, 111, 16))
        self.label_all_package.setObjectName("label_all_package")
        self.label_local_package = QtWidgets.QLabel(self.centralwidget)
        self.label_local_package.setGeometry(QtCore.QRect(390, 70, 111, 16))
        self.label_local_package.setObjectName("label_local_package")
        self.label = QtWidgets.QLabel (self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 240, 111, 81))
        self.label.setStyleSheet("image: url(:/b.ico)")
        self.label.setText("")
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(320, 520, 120, 10))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setValue(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.btn_getpackage.clicked.connect(MainWindow.get_dut_package)
        self.btn_dir.clicked.connect(MainWindow.get_dir)
        self.btn_analysis.clicked.connect(MainWindow.start_analysis)
        self.btn_add.clicked.connect(MainWindow.listWidget_add_item)
        self.btn_delete.clicked.connect(MainWindow.listWidget_local_delete)
        self.listWidget_all.doubleClicked.connect(MainWindow.listWidget_add_to_local)
        self.listWidget_local.doubleClicked.connect (MainWindow.listWidget_back_to_all)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "V-MemoryLeak"))
        MainWindow.setWindowIcon (QIcon (":/pokeballs_p.ico"))
        self.btn_dir.setText(_translate("MainWindow", "文件路径"))
        self.btn_getpackage.setText(_translate("MainWindow", "获取包名"))
        self.btn_analysis.setText(_translate("MainWindow", "开始分析"))
        self.btn_add.setText(_translate("MainWindow", "添加"))
        self.btn_delete.setText(_translate("MainWindow", "删除"))
        self.label_all_package.setText(_translate("MainWindow", "TextLabel"))
        self.label_local_package.setText(_translate("MainWindow", "TextLabel"))
        #self.label_arrow.setText (_translate ("MainWindow", "Test"))
        self.label_all_package.setText("待选择%s项"%str(self.listWidget_all.count()))
        self.label_local_package.setText("已选择%s项"%str(self.listWidget_local.count()))
