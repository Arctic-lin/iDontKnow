# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newMainUi.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(457, 297)
        MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 431, 251))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit.setPlaceholderText\
            (
             "第一次使用需勾选执行类型并插入一台手机\n"
             "点击初始化\n"
             "=====================================================\n"
             "仅授权:用于单纯授权\n"
             "MonkeyTest:执行授权&静音&屏蔽Log日志输出\n"
             "nohup:部分手机无法通过sh&将脚本挂在后台执行,可通过nohup\n"
             )
        self.gridLayout.addWidget(self.plainTextEdit, 4, 0, 1, 3)
        self.line = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 1, 1, 1)
        self.checkBox_nohup = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_nohup.setObjectName("checkBox_nohup")
        self.checkBox_nohup.setChecked(True)
        self.gridLayout.addWidget(self.checkBox_nohup, 0, 2, 1, 1)
        self.pushButton_start = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_start.setObjectName("pushButton_start")
        self.gridLayout.addWidget(self.pushButton_start, 2, 1, 1, 1)
        self.pushButton_start.setDisabled(True)
        self.pushButton_init = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_init.setObjectName("pushButton_init")
        self.gridLayout.addWidget(self.pushButton_init, 2, 0, 1, 1)
        self.pushButton_stop = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.gridLayout.addWidget(self.pushButton_stop, 2, 2, 1, 1)
        self.checkBox_onlyApply = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_onlyApply.setObjectName("checkBox_onlyApply")
        self.gridLayout.addWidget(self.checkBox_onlyApply, 0, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 1, 2, 1, 1)
        self.checkBox_monkeyTest = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_monkeyTest.setObjectName("checkBox_monkeyTest")
        self.gridLayout.addWidget(self.checkBox_monkeyTest, 0, 1, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 1, 0, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 3, 0, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout.addWidget(self.line_5, 3, 1, 1, 1)
        self.line_6 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout.addWidget(self.line_6, 3, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.checkBox_onlyApply.clicked.connect(MainWindow.checkBox_diable)
        self.checkBox_monkeyTest.clicked.connect(MainWindow.checkBox_diable)
        self.checkBox_nohup.clicked.connect(MainWindow.checkBox_diable)
        self.pushButton_init.clicked.connect(MainWindow.init_Device)
        self.pushButton_start.clicked.connect(MainWindow.start_Script)
        self.pushButton_stop.clicked.connect(MainWindow.end_Script)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "V-AppsPermission"))
        MainWindow.setWindowIcon(QtGui.QIcon(r"D:\Program\GithubProject\NewApplyPerMission\pokeballs.ico"))
        self.checkBox_nohup.setText(_translate("MainWindow", "nohup"))
        self.checkBox_nohup.setToolTip(_translate("MainWindow",
                                                  "<html><head/><body><p>部分手机无法通过sh后台执行,需用到nohup</p></body></html>"))
        self.pushButton_start.setText(_translate("MainWindow", "执行"))
        self.pushButton_init.setText(_translate("MainWindow", "初始化"))
        self.pushButton_stop.setText(_translate("MainWindow", "没用的按钮"))
        self.checkBox_onlyApply.setText(_translate("MainWindow", "仅授权"))
        self.checkBox_monkeyTest.setText(_translate("MainWindow", "Monkey测试"))

    #点击一个Checkbox就屏蔽其他Checkbox
    def checkBox_diable(self, MainWindow):
        if self.checkBox_onlyApply.isChecked():
            self.checkBox_monkeyTest.setEnabled(False)
            self.checkBox_monkeyTest.setChecked(False)
        elif self.checkBox_monkeyTest.isChecked():
            self.checkBox_onlyApply.setEnabled(False)
            self.checkBox_onlyApply.setChecked(False)
        else:
            self.checkBox_onlyApply.setEnabled(True)
            self.checkBox_monkeyTest.setEnabled(True)
