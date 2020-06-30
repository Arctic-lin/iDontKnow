# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fota.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(418, 301)
        MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_start = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start.setGeometry(QtCore.QRect(148, 275, 125, 23))
        self.btn_start.setObjectName("btn_start")
        self.btn_flashDev = QtWidgets.QPushButton(self.centralwidget)
        self.btn_flashDev.setGeometry(QtCore.QRect(20, 275, 125, 23))
        self.btn_flashDev.setObjectName("btn_flashDev")
        self.btn_edl = QtWidgets.QPushButton(self.centralwidget)
        self.btn_edl.setGeometry(QtCore.QRect(278, 275, 125, 23))
        self.btn_edl.setObjectName("btn_edl")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(21, 11, 381, 257))
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 2, 1)
        self.btn_downFile = QtWidgets.QPushButton(self.widget)
        self.btn_downFile.setObjectName("btn_downFile")
        self.gridLayout.addWidget(self.btn_downFile, 2, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 2, 1, 1, 1)
        self.btn_upFile = QtWidgets.QPushButton(self.widget)
        self.btn_upFile.setObjectName("btn_upFile")
        self.gridLayout.addWidget(self.btn_upFile, 0, 2, 2, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(5)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.verticalHeader().setVisible(False)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item_deviceId = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item_deviceId)
        item_status = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item_status)
        item_progress = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item_progress)
        self.gridLayout_2.addWidget(self.tableWidget, 1, 0, 1, 1)
        self.btn_start.setEnabled(False)
        self.btn_edl.setEnabled(False)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btn_flashDev.clicked.connect(MainWindow.reflashDev)
        self.btn_start.clicked.connect(MainWindow.startFotaPreSet)
        self.btn_edl.clicked.connect(MainWindow.edlMode)
        self.btn_upFile.clicked.connect(MainWindow.selectUpFile)
        self.btn_downFile.clicked.connect(MainWindow.selectDownFile)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FOTA Stress Test"))
        MainWindow.setWindowIcon(QtGui.QIcon(r".\duck.ico"))
        self.btn_start.setText(_translate("MainWindow", "开始"))
        self.btn_flashDev.setText(_translate("MainWindow", "刷新设备"))
        self.btn_edl.setText(_translate("MainWindow", "进入下载模式"))
        self.label_2.setText(_translate("MainWindow", "Downgrade File ："))
        self.btn_downFile.setText(_translate("MainWindow", "..."))
        self.label.setText(_translate("MainWindow", "Upgrade File   ："))
        self.btn_upFile.setText(_translate("MainWindow", "..."))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item_deviceId = self.tableWidget.horizontalHeaderItem(0)
        item_deviceId.setText(_translate("MainWindow", "DeviceID"))
        item_status = self.tableWidget.horizontalHeaderItem(1)
        item_status.setText(_translate("MainWindow", "Status"))
        item_progress = self.tableWidget.horizontalHeaderItem(2)
        item_progress.setText(_translate("MainWindow", "Progress"))