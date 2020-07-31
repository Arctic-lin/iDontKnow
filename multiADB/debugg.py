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
import os
from pypinyin import lazy_pinyin
from PyQt5.QtWidgets import QMainWindow,QApplication,QFileDialog,QTableWidgetItem,QMessageBox,QProgressBar
from PyQt5 import QtWidgets
from PyQt5 import QtCore,QtGui
from PyQt5.QtCore import pyqtSignal
from PyQt5.Qt import QThread
import time

devList = []

class MyThread(QThread):
    sinOutStatus = pyqtSignal(str,str)
    sinOutProgress = pyqtSignal(str,int)

    def __init__(self,testType,dev,*args):
        super().__init__()
        self.dev = dev
        self.testType = testType
        self.args = args

    def shellCmd(self,*args,need_stdout=0):
        adb_progress = r".\lib\adb\adb.exe"
        cmd_line = [adb_progress] + ["-s",self.dev] + list(args)
        cmd_line_str = " ".join(cmd_line)
        logger.info('cmd:{}'.format(cmd_line_str))
        proc = subprocess.Popen(cmd_line_str,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        stdout, stderr = proc.communicate()
        proc.wait()
        if need_stdout == 0:
            return stdout
        elif need_stdout == 1:
            return stderr
        elif need_stdout == 2:
            return stdout,stderr

    def isFileExistsInADB(self,phoneDir):
        if phoneDir == r"/sdcard" or r"/sdcard/":
            return True
        else:
            proc = self.shellCmd("shell ls -a %s" % phoneDir, need_stdout=2)
            if "No such file" in proc[1]:
                return False
            elif proc[0]:
                return True

    def mkdirDocument(self,phoneDir):
        if self.isFileExistsInADB(phoneDir):
            return logger.info("%s - PhoneDir is Exists,No need to creat"%self.dev)
        else:
            logger.info("%s - Creat File:%s..." % (self.dev,phoneDir))
            mkdir = self.shellCmd("shell mkdir %s" % phoneDir)
            if self.isFileExistsInADB(phoneDir):
                return logger.info("%s - Creat Success..."%self.dev)

    #FOTA test
    def fotaTest(self):
        ######args0 = upgradeFile
        ######args1 = downgradeFile
        ######args2 = APkFile
        ######args3 = PhoneDir
        self.sinOutStatus.emit(self.dev,"设置Never Sleep")
        self.sinOutProgress.emit(self.dev,5)
        # subprocess.call("adb -s %s shell settings put system screen_off_timeout 1" % self.dev)
        self.shellCmd("shell settings put system screen_off_timeout 1")
        self.sinOutProgress.emit(self.dev, 10)
        # 执行静音脚本
        self.sinOutStatus.emit(self.dev, "设置静音")
        self.sinOutProgress.emit(self.dev, 15)
        for i in range(1, 11):
            # subprocess.call("adb -s %s shell media volume --stream %d --set 0" % (self.dev, i))
            self.shellCmd("shell media volume --stream %d --set 0"%(i))
        self.sinOutProgress.emit(self.dev, 25)
        # 推送文件
        self.sinOutStatus.emit(self.dev, "推送Upgrade文件")
        self.sinOutProgress.emit(self.dev, 30)
        # subprocess.call(r"adb -s %s push %s %s/upgrade.zip" % (self.dev, self.args[0] , self.args[3]), shell=True)
        self.shellCmd("push %s %s/upgrade.zip"%(self.args[0],self.args[3]))
        self.sinOutProgress.emit(self.dev, 50)
        self.sinOutStatus.emit(self.dev, "推送Downgrade文件")
        self.sinOutProgress.emit(self.dev, 55)
        # subprocess.call(r"adb -s %s push %s %s/downgrade.zip" % (self.dev, self.args[1] ,self.args[3]), shell=True)
        self.shellCmd("push %s %s/downgrade.zip" % (self.args[1], self.args[3]))
        self.sinOutProgress.emit(self.dev, 80)
        # 安装apk
        self.sinOutStatus.emit(self.dev, "安装APK")
        # subprocess.call("adb -s %s install -r %s" % (self.dev, self.args[2]))
        self.shellCmd("install -r %s"%(self.args[2]))
        self.sinOutProgress.emit(self.dev, 100)
        self.sinOutStatus.emit(self.dev, "完成")

    #pushFile
    def pushTest(self):
        #args0 = 0 or 1 来判断单个文件还是整个文件
        #args1 = dir
        #args2 = phoneDir
        self.sinOutStatus.emit(self.dev, "检查PhoneDir是否存在")
        self.sinOutProgress.emit(self.dev, 5)
        # self.mkdirDocument(self.args[1])
        self.sinOutStatus.emit(self.dev, "推送文件")
        self.sinOutProgress.emit(self.dev, 30)
        self.shellCmd("push -p %s %s"%(self.args[0],self.args[1]))
        self.sinOutStatus.emit(self.dev, "完成")
        self.sinOutProgress.emit(self.dev, 100)

    #install apk
    def installAPK(self):
        #args0 = src dir
        self.sinOutStatus.emit(self.dev, "安装文件")
        self.sinOutProgress.emit(self.dev, 5)
        apkList=[]
        for root, dirs, files in os.walk(self.args[0]):
            for i in files:
                if ".apk" in i:
                    apkList.append(os.path.join(self.args[0], i))
        count_progress=100//len(apkList)
        first = 0
        for i in apkList:
            first += count_progress
            self.sinOutStatus.emit(self.dev, "%s" % (os.path.split(i)[1]))
            self.shellCmd("install -r %s"%i)
            self.sinOutProgress.emit(self.dev,first)
        self.sinOutStatus.emit(self.dev, "完成")
        self.sinOutProgress.emit(self.dev, 100)

    #Mute
    def Mute(self):
        #args0 = loop
        #args1 = looptime
        self.sinOutStatus.emit(self.dev, "静音")
        self.sinOutProgress.emit(self.dev, 5)
        if self.args[0] == 0:
            count_ = 10
            for i in range(1, 11):
                # subprocess.call("adb -s %s shell media volume --stream %d --set 0" % (self.dev, i))
                self.shellCmd("shell media volume --stream %d --set 0"%(i))
                self.sinOutProgress.emit(self.dev, count_)
                count_ +=10
        self.sinOutStatus.emit(self.dev, "完成")

    #Reboot
    def rebootDev(self):
        #args0 = reboot type
        self.sinOutStatus.emit(self.dev, "重启")
        self.sinOutProgress.emit(self.dev, 20)
        if self.args[0] == 0:
            self.shellCmd("reboot")
        elif self.args[0] == 1:
            self.shellCmd("reboot edl")
        self.sinOutProgress.emit(self.dev, 100)
        self.sinOutStatus.emit(self.dev, "完成")

    #Monkey
    def monkey(self):
        #args[0]=src
        #args[1]=apk
        self.sinOutStatus.emit(self.dev, "Monkey文件")
        self.sinOutProgress.emit(self.dev, 20)
        self.shellCmd("push %s %s"%(self.args[0],"/sdcard/MonkeySource"))
        # self.sinOutStatus.emit(self.dev, "安装APK")
        # self.shellCmd("install -r %s"%(self.args[1]))
        # self.sinOutProgress.emit(self.dev, 80)
        self.sinOutStatus.emit(self.dev, "完成")
        self.sinOutProgress.emit(self.dev, 100)

    def test(self):
        print(self.testType,self.dev,self.args)
        self.sinOutStatus.emit(self.dev, "设置Never Sleep")
        self.sinOutProgress.emit(self.dev, 5)

    def checkTestTyep(self):
        if self.testType == "FOTA":
            self.fotaTest()
        elif self.testType =="PushFile":
            self.pushTest()
        elif self.testType =="InstallAPK":
            self.installAPK()
        elif self.testType =="Mute":
            self.Mute()
        elif self.testType =="Reboot":
            self.rebootDev()
        elif self.testType =="Userdefine":
            pass
        elif self.testType =="Monkey":
            self.monkey()

    def run(self):
        self.checkTestTyep()


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
        self.btn_run.setEnabled(False)

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
        self.btn_lockDev.setEnabled(True)
        self.btn_run.setEnabled(False)
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
        if self.tableWidget.rowCount():
            for i in range(self.tableWidget.rowCount()):
                devSingleId = self.tableWidget.item(i,0).text()
                devSingleStatus = self.tableWidget.item(i,1).text()
                if devSingleStatus == "unauthorized":
                    QMessageBox.warning(self, "错误", "%s is %s"% (devSingleId,devSingleStatus), QMessageBox.Ok)
                    return False
                elif devSingleStatus == "offline":
                    QMessageBox.warning(self, "错误", "%s is %s" % (devSingleId, devSingleStatus), QMessageBox.Ok)
                    return False
                else:
                    devList.append(devSingleId)
                    self.tableWidget.item(i,1).setText("Lock")
        else:
            QMessageBox.warning(self, "错误", "未检测到设备", QMessageBox.Ok)
            return False
        self.btn_lockDev.setEnabled(False)
        self.btn_run.setEnabled(True)

    def run(self):
        if self.tableWidget.rowCount():
            thread_pool=[]
            for i in range(self.tableWidget.rowCount()):
                devSingleId = self.tableWidget.item(i, 0).text()
                #FOTA测试
                if self.rbtn_fota.isChecked():
                    testType = "FOTA"
                    upgrade = self.addLineEdit_upGrade.text()
                    dograde = self.addLineEdit_downGrade.text()
                    apkgrade = self.addLineEdit_fota_apkFile.text()
                    if not self.addLineEdit_fota_phoneDir.text():
                        self.addLineEdit_fota_phoneDir.setText("/sdcard")
                    phonedir = self.addLineEdit_fota_phoneDir.text()
                    self.th = MyThread(testType,devSingleId,upgrade,dograde,apkgrade,phonedir)
                    self.th.sinOutStatus.connect(self.devStatus)
                    self.th.sinOutProgress.connect(self.devProgress)
                    thread_pool.append(self.th)

                #pushFile
                if self.rbtn_pushFile.isChecked():
                    testType = "PushFile"
                    src = self.addLineEdit_push_srcFile.text()
                    if not self.addLineEdit_push_toFile.text():
                        self.addLineEdit_push_toFile.setText("/sdcard")
                    phonedir = self.addLineEdit_push_toFile.text()
                    getname = self.getName(src)
                    self.reName(0,src,getname)
                    self.th = MyThread(testType,devSingleId,src,phonedir)
                    self.th.sinOutStatus.connect(self.devStatus)
                    self.th.sinOutProgress.connect(self.devProgress)
                    thread_pool.append(self.th)

                #installAPK
                if self.rbtn_installAPk.isChecked():
                    testType = "InstallAPK"
                    src = self.addLineEdit_ins_srcFile.text()
                    getname = self.getName(src)
                    self.reName(0, src, getname)
                    self.th = MyThread(testType, devSingleId, src)
                    self.th.sinOutStatus.connect(self.devStatus)
                    self.th.sinOutProgress.connect(self.devProgress)
                    thread_pool.append(self.th)

                #Mute
                if self.rbtn_mute.isChecked():
                    testType = "Mute"
                    if self.addRBtn_onlyOne.isChecked():
                        loop=0
                        looptime=300
                    elif self.addRBtn_loop.isChecked():
                        loop=1
                        if not self.addLineEdit_loop.text():
                            self.addLineEdit_loop.setText("300")
                        looptime=self.addLineEdit_loop.text()
                    self.th = MyThread(testType,devSingleId, loop, int(looptime))
                    self.th.sinOutStatus.connect(self.devStatus)
                    self.th.sinOutProgress.connect(self.devProgress)
                    thread_pool.append(self.th)

                #Reboot
                if self.rbtn_edlMode.isChecked():
                    testType = "Reboot"
                    if self.addRbtn_reboot.isChecked():
                        reboot = 0
                    elif self.addRbtn_rebootEDL.isChecked():
                        reboot = 1
                    self.th = MyThread(testType, devSingleId, reboot)
                    self.th.sinOutStatus.connect(self.devStatus)
                    self.th.sinOutProgress.connect(self.devProgress)
                    thread_pool.append(self.th)

                #Monkey
                if self.rbtn_monkeyPreset.isChecked():
                    testType = "Monkey"
                    src = r".\lib\monkeySource"
                    apk = r".\lib\monkeySource\DataFiller.apk"
                    self.th = MyThread(testType, devSingleId, src ,apk)
                    self.th.sinOutStatus.connect(self.devStatus)
                    self.th.sinOutProgress.connect(self.devProgress)
                    thread_pool.append(self.th)
            for th in thread_pool:
                th.start()
            for th in thread_pool:
                QThread.exec(th)

    def reName(self, testType, src, getName):
        if getName[0] == getName[1]:
            return logger.info("No need change File name")
        if testType == 0:
            if isinstance(getName[0], list):
                for i in range(len(getName[0])):
                    logger.info("Change %s to %s" % (getName[0][i], getName[1][i]))
                    srcPath = os.path.join(src,getName[0][i])
                    rePath = os.path.join(src,getName[1][i])
            elif isinstance(getName[0],str):
                logger.info("Change %s to %s" % (getName[0], getName[1]))
                srcPath = src
                splitSrc = os.path.split(src)
                rePath = os.path.join(splitSrc[0],getName[1])
            os.rename(srcPath,rePath)
        elif testType == 1:
            for i in range(len(getName[0])):
                logger.info("Change back %s to %s" % (getName[1][i], getName[0][i]))
                if isinstance(getName[0],list):
                    srcPath = os.path.join(src,getName[0][i])
                    rePath = os.path.join(src,getName[1][i])
                elif isinstance(getName[0], str):
                    srcPath = src
                    splitSrc = os.path.split(src)
                    rePath = os.path.join(splitSrc[0], getName[1])
                os.rename(rePath,srcPath)

    def getName(self, scr):
        old = []
        new = []
        new_new = []
        a = 0
        if os.path.isdir(scr):
            for i in os.listdir(scr):
                old.append(i)
                i = i.replace(" ", "")
                changeCNtoPinyin = lazy_pinyin(i)
                joinChange = ''.join(changeCNtoPinyin)
                new.append(joinChange)
            for i in new:
                if i not in new_new:
                    new_new.append(i)
                else:
                    a += 1
                    k = i.split(".")
                    h = k[0] + str(a) + "." + k[1]
                    new_new.append(h)
            return old, new_new
        else:
            old = os.path.split(scr)[-1]
            new = ''.join(lazy_pinyin(old))
            return old, new

    def devStatus(self,devid,devstate):
        if self.tableWidget.rowCount():
            for i in range(self.tableWidget.rowCount()):
                if self.tableWidget.item(i, 0) != None:
                    text = self.tableWidget.item(i, 0).text()
                    if text == devid:
                        newItem_deivceId = QTableWidgetItem(devstate)
                        self.tableWidget.setItem(i,1,newItem_deivceId)

    def devProgress(self,devid,int_value):
        if self.tableWidget.rowCount():
            for i in range(self.tableWidget.rowCount()):
                if self.tableWidget.item(i, 0) != None:
                    text = self.tableWidget.item(i, 0).text()
                    if text == devid:
                        qbar = QProgressBar()
                        qbar.setValue(int_value)
                        qbar.setStyleSheet("QProgressBar{color:black}")
                        self.tableWidget.setCellWidget(i, 2, qbar)

    def addFotaInterface(self):
        layout = QtWidgets.QGridLayout()
        #========================控件信息============================#
        self.addLable_upGrade = QtWidgets.QLabel(u"UpGrade File:")
        self.addLable_downGrade = QtWidgets.QLabel(u"DownGrade File:")
        self.addLable_apkFile = QtWidgets.QLabel(u"APK File:")
        self.addLable_phoneDir = QtWidgets.QLabel(u"Phone Dir:")
        self.addLineEdit_upGrade = QtWidgets.QLineEdit()
        self.addLineEdit_downGrade = QtWidgets.QLineEdit()
        self.addLineEdit_fota_apkFile = QtWidgets.QLineEdit()
        self.addLineEdit_fota_phoneDir = QtWidgets.QLineEdit()
        self.addLineEdit_fota_phoneDir.setPlaceholderText(r"/sdcard")
        self.addBtn_upGrade = QtWidgets.QPushButton(u"...")
        self.addBtn_downGrade = QtWidgets.QPushButton(u"...")
        self.addBtn_fota_apkFile = QtWidgets.QPushButton(u"...")
        #========================添加控件============================#
        layout.addWidget(self.addLable_upGrade,1,0)
        layout.addWidget(self.addLineEdit_upGrade,1,1)
        layout.addWidget(self.addBtn_upGrade,1,2)
        layout.addWidget(self.addLable_downGrade,2,0)
        layout.addWidget(self.addLineEdit_downGrade,2,1)
        layout.addWidget(self.addBtn_downGrade,2,2)
        layout.addWidget(self.addLable_apkFile,3,0)
        layout.addWidget(self.addLineEdit_fota_apkFile,3,1)
        layout.addWidget(self.addBtn_fota_apkFile,3,2)
        layout.addWidget(self.addLable_phoneDir,4,0)
        layout.addWidget(self.addLineEdit_fota_phoneDir,4,1,1,2)
        #=======================OK and Cancel======================#
        self.addBtn_upGrade.clicked.connect(lambda :self.chooseFiles(0,self.addLineEdit_upGrade))
        self.addBtn_downGrade.clicked.connect(lambda :self.chooseFiles(0,self.addLineEdit_downGrade))
        self.addBtn_fota_apkFile.clicked.connect(lambda :self.chooseFiles(1,self.addLineEdit_fota_apkFile))
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
        self.addLable_srcFile = QtWidgets.QLabel(u"文件目录:")
        self.addLable_toFile = QtWidgets.QLabel(u"目标目录:")
        self.addLineEdit_push_srcFile = QtWidgets.QLineEdit()
        self.addLineEdit_push_toFile = QtWidgets.QLineEdit()
        self.addLineEdit_push_toFile.setPlaceholderText("/sdcard")
        # self.addBtn_push_singleFile = QtWidgets.QPushButton(u"单个文件")
        self.addBtn_push_multiFile = QtWidgets.QPushButton(u"文件目录")
        self.addFrame = QtWidgets.QFrame()
        self.addFrame.setFrameShape(QtWidgets.QFrame.HLine)
        self.addFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        # ========================添加控件============================#
        layout.addWidget(self.addLable_srcFile, 1, 0)
        layout.addWidget(self.addLineEdit_push_srcFile, 1, 1,1,3)
        layout.addWidget(self.addLable_toFile, 4, 0)
        layout.addWidget(self.addLineEdit_push_toFile, 4, 1,1,3)
        layout.addWidget(self.addFrame,3,0,1,4)
        # layout.addWidget(self.addBtn_push_singleFile, 2, 2)
        layout.addWidget(self.addBtn_push_multiFile, 2, 3)
        # =======================OK and Cancel======================#
        # self.addBtn_push_singleFile.clicked.connect(lambda: self.pushChoose(0, self.addLineEdit_push_srcFile))
        self.addBtn_push_multiFile.clicked.connect(lambda: self.pushChoose(1, self.addLineEdit_push_srcFile))
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
        # use_info=u'\n单个文件:仅安装一个应用\n' \
        #          '文件目录:安装目录下的所以APK文件\n' \
        #          'PS:\n因ADB的特殊性,安装APK会把源文件名中带有中文\n' \
        #          '的包名改成拼音\n'
        use_info = u'\n' \
                   '文件目录:安装目录下的所以APK文件\n' \
                   'PS:\n因ADB的特殊性,安装APK会把源文件名中带有中文\n' \
                   '的包名改成拼音\n'
        self.addLable_des = QtWidgets.QLabel(use_info)
        self.addFrame = QtWidgets.QFrame()
        self.addFrame.setFrameShape(QtWidgets.QFrame.HLine)
        self.addFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        addFrame2 = QtWidgets.QFrame()
        self.addLable_ins_scrFile = QtWidgets.QLabel(u"文件目录:")
        self.addLineEdit_ins_srcFile = QtWidgets.QLineEdit()
        # self.addBtn_ins_singleFile = QtWidgets.QPushButton(u"单个文件")
        self.addBtn_ins_multiFile = QtWidgets.QPushButton(u"文件目录")
        # ========================添加控件============================#
        layout.addWidget(self.addLable_des, 1, 0,1,0)
        layout.addWidget(self.addFrame,2,0,1,0)
        layout.addWidget(self.addLable_ins_scrFile, 3, 0)
        layout.addWidget(self.addLineEdit_ins_srcFile, 3, 1,1,3)
        # layout.addWidget(self.addBtn_ins_singleFile, 4, 2)
        layout.addWidget(self.addBtn_ins_multiFile, 4, 3)
        # layout.addWidget(addFrame2,4,0)
        # =======================OK and Cancel======================#
        # self.addBtn_ins_singleFile.clicked.connect(lambda: self.installChoose(0, self.addLineEdit_ins_srcFile))
        self.addBtn_ins_multiFile.clicked.connect(lambda: self.installChoose(1, self.addLineEdit_ins_srcFile))
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
        self.addLable_des = QtWidgets.QLabel(use_info)
        self.addFrame = QtWidgets.QFrame()
        self.addFrame.setFrameShape(QtWidgets.QFrame.HLine)
        self.addFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.addRBtn_onlyOne = QtWidgets.QRadioButton(u"仅执行一次")
        self.addRBtn_loop = QtWidgets.QRadioButton(u"循环执行")
        self.addLable_loop = QtWidgets.QLabel(u"循环间隔:")
        self.addLineEdit_loop = QtWidgets.QLineEdit()
        self.addLable_second = QtWidgets.QLabel(u"秒")
        self.addLable_blank1 = QtWidgets.QLabel()
        self.addLable_blank2 = QtWidgets.QLabel(" "*30)
        # ========================添加控件============================#
        layout.addWidget(self.addLable_des, 1, 0,1,4)
        layout.addWidget(self.addFrame, 2, 0, 1, 0)
        layout.addWidget(self.addRBtn_onlyOne, 3, 0,1,4)
        layout.addWidget(self.addRBtn_loop, 4, 0,1,4)
        layout.addWidget(self.addLable_loop, 5, 0)
        layout.addWidget(self.addLineEdit_loop,5,1)
        layout.addWidget(self.addLable_second, 5, 2)
        layout.addWidget(self.addLable_blank2, 5, 3)
        layout.addWidget(self.addLable_blank1, 6, 0)
        # =======================OK and Cancel======================#
        self.addRBtn_loop.setChecked(True)
        need_disable = [self.addLable_second,self.addLineEdit_loop,self.addLable_loop]
        self.addRBtn_onlyOne.clicked.connect(lambda :self.disableMute(0,need_disable))
        self.addRBtn_loop.clicked.connect(lambda: self.disableMute(1,need_disable))
        self.addLineEdit_loop.setPlaceholderText("300")
        _reg = QtCore.QRegExp('[1-9][0-9]{1,4}')
        self.addLineEdit_loop.setValidator(QtGui.QRegExpValidator(_reg,self))
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
        self.addRbtn_reboot = QtWidgets.QRadioButton(u"adb reboot")
        self.addRbtn_rebootEDL = QtWidgets.QRadioButton(u"adb reboot edl")
        # ========================添加控件============================#
        layout.addWidget(self.addRbtn_reboot, 2, 0, 1, 4)
        layout.addWidget(self.addRbtn_rebootEDL, 3, 0, 1, 4)
        # =======================OK and Cancel======================#
        self.addRbtn_reboot.setChecked(True)
        self.widget.setLayout(layout)

    def addUserDefineInterface(self):
        layout = QtWidgets.QGridLayout()
        # ========================控件信息============================#
        self.addCombox = QtWidgets.QPlainTextEdit()
        self.addCombox.setPlaceholderText("逐条输入adb指令并以\";\"分段\n例如:\nadb shell dumpsys meminfo;\n"
                                     "adb shell input kevent 3")
        # ========================添加控件============================#
        layout.addWidget(self.addCombox, 1, 0)
        # =======================OK and Cancel======================#
        self.widget.setLayout(layout)

    def addMonkeyPresetInterface(self):
        layout = QtWidgets.QGridLayout()
        # ========================控件信息============================#
        # self.addBtn_monkeyPreset = QtWidgets.QPushButton()
        # self.addBtn_monkeyPreset.setText("Run")
        self.addPokeLabel = QtWidgets.QLabel()
        self.addPokeLabel.setText("PokeBall")
        # ========================添加控件============================#
        layout.addWidget(self.addPokeLabel, 1, 0)
        # =======================OK and Cancel======================#
        self.widget.setLayout(layout)

class GetDevThread(QThread):
    def __init__(self):
        super().__init__()

    def shellCmd(self,*args):
        adb_progress = r".\lib\adb\adb.exe"
        cmd_line = [adb_progress] + list(args)
        cmd_line_str = " ".join(cmd_line)
        print('cmd:{}'.format(cmd_line_str))
        proc = subprocess.Popen(cmd_line_str,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        stdout, stderr = proc.communicate()
        proc.wait()
        return stdout

    def getDevSN(self):
        devInfo = self.shellCmd("devices")
        devDecode = devInfo.decode("utf-8")
        devSN = re.findall("\n" + "(.*?)" + r"\t" + "(device|unauthorized|offline)", devDecode)
        # print(devSN)
        return devSN

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())