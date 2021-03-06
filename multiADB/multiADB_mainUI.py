# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'multiADB_mainUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(544, 367)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_monkeyPreSet = QtWidgets.QPushButton(self.centralwidget)
        self.btn_monkeyPreSet.setGeometry(QtCore.QRect(230, 330, 101, 23))
        self.btn_monkeyPreSet.setObjectName("btn_monkeyPreSet")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(120, 240, 320, 83))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_downloadMode = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_downloadMode.setObjectName("btn_downloadMode")
        self.gridLayout.addWidget(self.btn_downloadMode, 0, 4, 1, 1)
        self.btn_mute = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_mute.setObjectName("btn_mute")
        self.gridLayout.addWidget(self.btn_mute, 0, 2, 1, 1)
        self.btn_singleADB = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_singleADB.setObjectName("btn_singleADB")
        self.gridLayout.addWidget(self.btn_singleADB, 1, 4, 1, 1)
        self.btn_pushFile = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_pushFile.setObjectName("btn_pushFile")
        self.gridLayout.addWidget(self.btn_pushFile, 1, 0, 1, 1)
        self.btn_fota = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_fota.setObjectName("btn_fota")
        self.gridLayout.addWidget(self.btn_fota, 0, 0, 1, 1)
        self.btn_installAPK = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_installAPK.setObjectName("btn_installAPK")
        self.gridLayout.addWidget(self.btn_installAPK, 1, 2, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 10, 501, 223))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_freshDdev = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_freshDdev.setObjectName("btn_freshDdev")
        self.gridLayout_2.addWidget(self.btn_freshDdev, 0, 0, 1, 1)
        self.btn_confimDev = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_confimDev.setObjectName("btn_confimDev")
        self.gridLayout_2.addWidget(self.btn_confimDev, 0, 1, 1, 1)
        self.btn_start = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_start.setObjectName("btn_start")
        self.gridLayout_2.addWidget(self.btn_start, 0, 2, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.layoutWidget1)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item_deviceId = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item_deviceId)
        item_status = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item_status)
        item_progress = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item_progress)
        self.gridLayout_2.addWidget(self.tableWidget, 1, 0, 1, 3)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.verticalHeader().setVisible(False)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btn_fota.clicked.connect(MainWindow.main_fotaTest)
        self.btn_mute.clicked.connect(MainWindow.main_mute)
        self.btn_downloadMode.clicked.connect(MainWindow.main_downloadMode)
        self.btn_pushFile.clicked.connect(MainWindow.main_pushfile)
        self.btn_installAPK.clicked.connect(MainWindow.main_installAPK)
        self.btn_singleADB.clicked.connect(MainWindow.main_usercho)
        self.btn_monkeyPreSet.clicked.connect(MainWindow.main_monkeyPreset)
        self.btn_freshDdev.clicked.connect(MainWindow.main_freshDev)
        self.btn_confimDev.clicked.connect(MainWindow.main_lockDev)
        self.btn_start.clicked.connect(MainWindow.main_run)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_monkeyPreSet.setText(_translate("MainWindow", "MonkeyPreSet"))
        self.btn_downloadMode.setText(_translate("MainWindow", "下载模式"))
        self.btn_mute.setText(_translate("MainWindow", "静音"))
        self.btn_singleADB.setText(_translate("MainWindow", "自定义"))
        self.btn_pushFile.setText(_translate("MainWindow", "传输文件"))
        self.btn_fota.setText(_translate("MainWindow", "FOTA测试"))
        self.btn_installAPK.setText(_translate("MainWindow", "安装应用"))
        self.btn_freshDdev.setText(_translate("MainWindow", "刷新设备"))
        self.btn_confimDev.setText(_translate("MainWindow", "锁定设备"))
        self.btn_start.setText(_translate("MainWindow", "执行"))
        item_deviceId = self.tableWidget.horizontalHeaderItem(0)
        item_deviceId.setText(_translate("MainWindow", "DeviceID"))
        item_status = self.tableWidget.horizontalHeaderItem(1)
        item_status.setText(_translate("MainWindow", "Status"))
        item_progress = self.tableWidget.horizontalHeaderItem(2)
        item_progress.setText(_translate("MainWindow", "Progress"))
