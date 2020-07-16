# -*- coding: utf-8 -*-
# @Time    : 2020/7/15 11:38
# @Author  : Arctic
# @FileName: debugg.py
# @Software: PyCharm
# @Purpose :
import logging
logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
from test import Ui_MainWindow
import sys
import subprocess
import re
import sip
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget,QDialog,QFileDialog,QTableWidgetItem,QMessageBox,QPushButton,QLabel
from PyQt5 import QtWidgets
from PyQt5 import QtCore,QtGui
from PyQt5.QtCore import pyqtSignal
from PyQt5.Qt import QThread

devList = []

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui = Ui_MainWindow()
        self.setupUi(self)
        self.rbtn_fota.clicked.connect(lambda : self.radioEvent(self.rbtn_fota))
        self.rbtn_pushFile.clicked.connect(lambda : self.radioEvent(self.rbtn_pushFile))
        self.rbtn_installAPk.clicked.connect(lambda : self.radioEvent(self.rbtn_installAPk))
        self.rbtn_mute.clicked.connect(lambda : self.radioEvent(self.rbtn_mute))
        self.rbtn_edlMode.clicked.connect(lambda : self.radioEvent(self.rbtn_edlMode))
        self.rbtn_userdefine.clicked.connect(lambda : self.radioEvent(self.rbtn_userdefine))
        self.rbtn_monkeyPreset.clicked.connect(lambda : self.radioEvent(self.rbtn_monkeyPreset))

    def radioEvent(self,btn):
        if self.widget.children():
            for i in self.widget.children():
                self.widget.children().remove(i)
                sip.delete(i)
        if btn == self.rbtn_fota:
            self.addFotaInterface()
        elif btn == self.rbtn_pushFile:
            self.addPushfileInterface()
        elif btn == self.rbtn_installAPk:
            self.addInstallInterface()
        elif btn == self.rbtn_mute:
            self.addMuteInterface()
        elif btn == self.rbtn_edlMode:
            self.addEdlModeInterface()
        elif btn == self.rbtn_userdefine:
            self.addUserDefineInterface()
        elif btn == self.rbtn_monkeyPreset:
            self.addMonkeyPresetInterface()
        logger.info(btn.text())

    def flashDev(self):
        logger.info("%s" % self.btn_flashDev.text())
        self.getDevSN = GetDevThread()
        devSN = self.getDevSN.getDevSN()
        self.tableWidget.clearContents()
        if devSN:
            self.tableWidget.setRowCount(len(devSN))
            for i in range(len(devSN)):
                if devSN[i][-1]:
                    newItem_deivceId = QTableWidgetItem(devSN[i][0])
                    if devSN[i][-1] == "device":
                        newItem_status = QTableWidgetItem("normal")
                    else:
                        newItem_status = QTableWidgetItem(devSN[i][-1])
                    self.tableWidget.setItem(i, 0, newItem_deivceId)
                    self.tableWidget.setItem(i, 1, newItem_status)
                    logger.info("检测到设备:%s,连接状态:%s" % (devSN[i][0], devSN[i][-1]))
        else:
            logger.info("未检测到连接设备")

    def lockDev(self):
        devList.clear()
        print(bool(self.tableWidget.rowCount()))


    def run(self):
        pass

    def addFotaInterface(self):
        layout = QtWidgets.QGridLayout()
        #========================控件信息============================#
        addLable_upGrade = QtWidgets.QLabel(u"UpGrade File:")
        addLable_downGrade = QtWidgets.QLabel(u"DownGrade File:")
        addLable_apkFile = QtWidgets.QLabel(u"APK File:")
        addLable_phoneDir = QtWidgets.QLabel(u"Phone Dir:")
        addLineEdit_upGrade = QtWidgets.QLineEdit()
        addLineEdit_downGrade = QtWidgets.QLineEdit()
        addLineEdit_apkFile = QtWidgets.QLineEdit()
        addLineEdit_phoneDir = QtWidgets.QLineEdit()
        addLineEdit_phoneDir.setPlaceholderText(r"/sdcard")
        addBtn_upGrade = QtWidgets.QPushButton(u"...")
        addBtn_downGrade = QtWidgets.QPushButton(u"...")
        addBtn_apkFile = QtWidgets.QPushButton(u"...")
        #========================添加控件============================#
        layout.addWidget(addLable_upGrade,1,0)
        layout.addWidget(addLineEdit_upGrade,1,1)
        layout.addWidget(addBtn_upGrade,1,2)
        layout.addWidget(addLable_downGrade,2,0)
        layout.addWidget(addLineEdit_downGrade,2,1)
        layout.addWidget(addBtn_downGrade,2,2)
        layout.addWidget(addLable_apkFile,3,0)
        layout.addWidget(addLineEdit_apkFile,3,1)
        layout.addWidget(addBtn_apkFile,3,2)
        layout.addWidget(addLable_phoneDir,4,0)
        layout.addWidget(addLineEdit_phoneDir,4,1,1,2)
        #=======================OK and Cancel======================#
        addBtn_upGrade.clicked.connect(lambda :self.chooseFiles(0,addLineEdit_upGrade))
        addBtn_downGrade.clicked.connect(lambda :self.chooseFiles(0,addLineEdit_downGrade))
        addBtn_apkFile.clicked.connect(lambda :self.chooseFiles(1,addLineEdit_apkFile))
        self.widget.setLayout(layout)

    def chooseFiles(self,intt,lineEdit):
        if intt == 0:
            file = QFileDialog.getOpenFileName(self, "选择文件", filter="Zip file (*.zip)")
        elif intt == 1:
            file = QFileDialog.getOpenFileName(self, "选择文件", filter="APK file (*.apk)")
        if file:
            lineEdit.setText(file[0])
            logger.info("%s" % file[0])

    def addPushfileInterface(self):
        layout = QtWidgets.QGridLayout()
        # ========================控件信息============================#
        addLable_srcFile = QtWidgets.QLabel(u"文件目录:")
        addLable_toFile = QtWidgets.QLabel(u"目标目录:")
        addLineEdit_srcFile = QtWidgets.QLineEdit()
        addLineEdit_toFile = QtWidgets.QLineEdit()
        addLineEdit_toFile.setPlaceholderText("/sdcard")
        addBtn_singleFile = QtWidgets.QPushButton(u"单个文件")
        addBtn_multiFile = QtWidgets.QPushButton(u"文件目录")
        addFrame = QtWidgets.QFrame()
        addFrame.setFrameShape(QtWidgets.QFrame.HLine)
        addFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        # ========================添加控件============================#
        layout.addWidget(addLable_srcFile, 1, 0)
        layout.addWidget(addLineEdit_srcFile, 1, 1,1,3)
        layout.addWidget(addLable_toFile, 4, 0)
        layout.addWidget(addLineEdit_toFile, 4, 1,1,3)
        layout.addWidget(addFrame,3,0,1,4)
        layout.addWidget(addBtn_singleFile, 2, 2)
        layout.addWidget(addBtn_multiFile, 2, 3)
        # =======================OK and Cancel======================#
        addBtn_singleFile.clicked.connect(lambda: self.pushChoose(0, addLineEdit_srcFile))
        addBtn_multiFile.clicked.connect(lambda: self.pushChoose(1, addLineEdit_srcFile))
        self.widget.setLayout(layout)

    def pushChoose(self,intt,lineEdit):
        if intt == 0:
            file = QFileDialog.getOpenFileName(self, "选择文件")
            if file:
                lineEdit.setText(file[0])
                logger.info("%s" % file[0])
            elif intt == 1:
                file = QFileDialog.getExistingDirectory(self, "选择文件")
                if file:
                    lineEdit.setText(file)
                    logger.info("%s" % file)

    def addInstallInterface(self):
        layout = QtWidgets.QGridLayout()
        # ========================控件信息============================#
        use_info=u'\n单个文件:仅安装一个应用\n' \
                 '文件目录:安装目录下的所以APK文件\n' \
                 'PS:\n因ADB的特殊性,安装APK会把源文件名中带有中文\n' \
                 '的包名改成拼音\n'
        addLable_des = QtWidgets.QLabel(use_info)
        addFrame = QtWidgets.QFrame()
        addFrame.setFrameShape(QtWidgets.QFrame.HLine)
        addFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        addFrame2 = QtWidgets.QFrame()
        addLable_scrFile = QtWidgets.QLabel(u"文件目录:")
        addLineEdit_srcFile = QtWidgets.QLineEdit()
        addBtn_singleFile = QtWidgets.QPushButton(u"单个文件")
        addBtn_multiFile = QtWidgets.QPushButton(u"文件目录")
        # ========================添加控件============================#
        layout.addWidget(addLable_des, 1, 0,1,0)
        layout.addWidget(addFrame,2,0,1,0)
        layout.addWidget(addLable_scrFile, 3, 0)
        layout.addWidget(addLineEdit_srcFile, 3, 1,1,3)
        layout.addWidget(addBtn_singleFile, 4, 2)
        layout.addWidget(addBtn_multiFile, 4, 3)
        # layout.addWidget(addFrame2,4,0)
        # =======================OK and Cancel======================#
        addBtn_singleFile.clicked.connect(lambda: self.installChoose(0, addLineEdit_srcFile))
        addBtn_multiFile.clicked.connect(lambda: self.installChoose(1, addLineEdit_srcFile))
        self.widget.setLayout(layout)

    def installChoose(self,intt,lineEdit):
        if intt == 0:
            file = QFileDialog.getOpenFileName(self, "选择文件",filter="APK file (*.apk)")
            if file:
                lineEdit.setText(file[0])
                logger.info("%s" % file[0])
        elif intt == 1:
            file = QFileDialog.getExistingDirectory(self, "选择文件")
            if file:
                lineEdit.setText(file)
                logger.info("%s" % file)

    def addMuteInterface(self):
        layout = QtWidgets.QGridLayout()
        # ========================控件信息============================#
        use_info = u'\n1.仅执行一次静音\n' \
                   '2.循环执行,循环间隔时间执行一次静音\n'
        addLable_des = QtWidgets.QLabel(use_info)
        addFrame = QtWidgets.QFrame()
        addFrame.setFrameShape(QtWidgets.QFrame.HLine)
        addFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        addRBtn_onlyOne = QtWidgets.QRadioButton(u"仅执行一次")
        addRBtn_loop = QtWidgets.QRadioButton(u"循环执行")
        addLable_loop = QtWidgets.QLabel(u"循环间隔:")
        addLineEdit_loop = QtWidgets.QLineEdit()
        addLable_second = QtWidgets.QLabel(u"秒")
        addLable_blank1 = QtWidgets.QLabel()
        addLable_blank2 = QtWidgets.QLabel(" "*30)
        # ========================添加控件============================#
        layout.addWidget(addLable_des, 1, 0,1,4)
        layout.addWidget(addFrame, 2, 0, 1, 0)
        layout.addWidget(addRBtn_onlyOne, 3, 0,1,4)
        layout.addWidget(addRBtn_loop, 4, 0,1,4)
        layout.addWidget(addLable_loop, 5, 0)
        layout.addWidget(addLineEdit_loop,5,1)
        layout.addWidget(addLable_second, 5, 2)
        layout.addWidget(addLable_blank2, 5, 3)
        layout.addWidget(addLable_blank1, 6, 0)
        # =======================OK and Cancel======================#
        addRBtn_loop.setChecked(True)
        need_disable = [addLable_second,addLineEdit_loop,addLable_loop]
        addRBtn_onlyOne.clicked.connect(lambda :self.disableMute(0,need_disable))
        addRBtn_loop.clicked.connect(lambda: self.disableMute(1,need_disable))
        addLineEdit_loop.setPlaceholderText("300")
        _reg = QtCore.QRegExp('[1-9][0-9]{1,4}')
        addLineEdit_loop.setValidator(QtGui.QRegExpValidator(_reg,self))
        self.widget.setLayout(layout)

    def disableMute(self,intt,listt):
        if intt == 0:
            for i in listt:
                i.setEnabled(False)
        elif intt == 1:
            for i in listt:
                i.setEnabled(True)

    def addEdlModeInterface(self):
        layout = QtWidgets.QGridLayout()
        # ========================控件信息============================#
        addRBtn_onlyOne = QtWidgets.QRadioButton(u"adb reboot")
        addRBtn_loop = QtWidgets.QRadioButton(u"adb reboot edl")
        # ========================添加控件============================#
        layout.addWidget(addRBtn_onlyOne, 2, 0, 1, 4)
        layout.addWidget(addRBtn_loop, 3, 0, 1, 4)
        # =======================OK and Cancel======================#
        addRBtn_onlyOne.setChecked(True)
        self.widget.setLayout(layout)

    def addUserDefineInterface(self):
        layout = QtWidgets.QGridLayout()
        # ========================控件信息============================#
        addCombox = QtWidgets.QPlainTextEdit()
        addCombox.setPlaceholderText("逐条输入adb指令并以\";\"分段\n例如:\nadb shell dumpsys meminfo;\n"
                                     "adb shell input kevent 3")
        # ========================添加控件============================#
        layout.addWidget(addCombox, 1, 0)
        # =======================OK and Cancel======================#
        self.widget.setLayout(layout)

    def addMonkeyPresetInterface(self):
        pass

class GetDevThread(QThread):
    def __init__(self):
        super().__init__()
    def getDevSN(self):
        devInfo = subprocess.check_output("adb devices", encoding="utf-8")
        devSN = re.findall("\n" + "(.*?)" + r"\t" + "(device|unauthorized|offline)", devInfo)
        return devSN

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())