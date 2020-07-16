# -*- coding: utf-8 -*-
# @Time    : 2020/6/28 20:59
# @Author  : Arctic
# @FileName: runFota.py
# @Software: PyCharm
# @Purpose :Fota Pre-Set

import sys
from fotaUI import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow,QApplication,QFileDialog,QTableWidgetItem,QMessageBox,QProgressBar
from PyQt5.Qt import QThread
from PyQt5.QtCore import pyqtSignal
import subprocess
import re


devid = []
upgrade = ""
downgrade = ""
testType = ""

class MyThread(QThread):
    sinOutStatus = pyqtSignal(str,str)
    sinOutProgress = pyqtSignal(str,int)
    def __init__(self,dev):
        super().__init__()
        self.dev = dev


    def rebootEdl(self):
        self.sinOutStatus.emit(self.dev,"初始化")
        self.sinOutProgress.emit(self.dev,10)
        subprocess.check_output("adb -s %s reboot edl"%self.dev)
        self.sinOutStatus.emit(self.dev,"进入下载模式完成")
        self.sinOutProgress.emit(self.dev,100)
    def fotaTest(self):
        #不灭屏
        self.sinOutStatus.emit(self.dev,"设置Never Sleep")
        self.sinOutProgress.emit(self.dev,0)
        print(self.dev)
        subprocess.call("adb -s %s shell settings put system screen_off_timeout 1"%self.dev)
        self.sinOutProgress.emit(self.dev,10)
        #执行静音脚本
        self.sinOutStatus.emit(self.dev,"设置静音")
        self.sinOutProgress.emit(self.dev,15)
        print(self.dev)
        for i in range(1,11):
            subprocess.call("adb -s %s shell media volume --stream %d --set 0"%(self.dev,i))
        self.sinOutProgress.emit(self.dev,25)
        #推送文件
        self.sinOutStatus.emit(self.dev,"推送Upgrade文件")
        self.sinOutProgress.emit(self.dev,30)
        print(self.dev)
        subprocess.call(r"adb -s %s push %s /sdcard/.downloaded/upgrade.zip" % (self.dev,upgrade),shell=True)
        self.sinOutProgress.emit(self.dev,50)
        print(self.dev)
        self.sinOutStatus.emit(self.dev,"推送Downgrade文件")
        self.sinOutProgress.emit(self.dev,55)
        subprocess.call(r"adb -s %s push %s /sdcard/.downloaded/downgrade.zip" % (self.dev, downgrade), shell=True)
        self.sinOutProgress.emit(self.dev,80)
        #安装apk
        self.sinOutStatus.emit(self.dev,"安装APK")
        subprocess.call("adb -s %s install -r %s" % (self.dev , r"./JrdFotaAutotest.apk"))
        self.sinOutProgress.emit(self.dev,100)
        self.sinOutStatus.emit(self.dev,"完成")

    def run(self):
        if testType == "rebootEdl":
            self.rebootEdl()
        elif testType == "fotaTest":
            self.fotaTest()

class GetDevThread(QThread):
    def __init__(self):
        super().__init__()
    def getDevSN(self):
        devInfo = subprocess.check_output("adb devices", encoding="utf-8")
        devSN = re.findall("\n" + "(.*?)" + r"\t" + "(device|unauthorized|offline)", devInfo)
        return devSN

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui = Ui_MainWindow()
        self.setupUi(self)
        self.pbar = QProgressBar()
        # self.thread = MyThread()
        # self.thread_status.sinOutStatus.connect(self.devStatus)
        # self.thread_status.sinOutProgress.connect(self.devProgress)

    def reflashDev(self):
        self.btn_start.setEnabled(True)
        self.btn_edl.setEnabled(True)
        #清除表格
        self.tableWidget.clearContents()
        #获取设备号
        # devInfo = subprocess.check_output("adb devices",encoding="utf-8")
        # devSN = re.findall("\n" + "(.*?)" + r"\t" + "(device|unauthorized|offline)", devInfo)
        self.getThread = GetDevThread()
        devSN = self.getThread.getDevSN()
        print(devSN)
        #添加到列表中
        # devid.clear()
        # for i in devSN:
        #     devid.append(i)

        #根据devSN将设备号及状态填入表格中
        if devSN:
            for i in range(len(devSN)):
                if devSN[i][-1]:
                    newItem_deivceId = QTableWidgetItem(devSN[i][0])
                    print(newItem_deivceId)
                    if devSN[i][-1] == "device":
                        newItem_status = QTableWidgetItem("normal")
                    else:
                        newItem_status = QTableWidgetItem(devSN[i][-1])
                    self.tableWidget.setItem(i,0,newItem_deivceId)
                    self.tableWidget.setItem(i,1,newItem_status)
        else:
            reply = QMessageBox.warning(self,"错误","未检测到设备",QMessageBox.Ok)
            return False

    def startFotaPreSet(self):
        self.btn_edl.setEnabled(False)
        self.btn_start.setEnabled(False)
        global testType
        testType = "fotaTest"
        global upgrade,downgrade
        upgrade,downgrade = self.lineEdit.text(),self.lineEdit_2.text()
        if self.checkDevStatus():
            threadpool=[]
            for i in range(5):
                if self.tableWidget.item(i, 0) != None:
                    text = self.tableWidget.item(i, 0).text()
                    self.th = MyThread(text)
                    self.th.sinOutStatus.connect(self.devStatus)
                    self.th.sinOutProgress.connect(self.devProgress)
                    threadpool.append(self.th)
                    # self.th.start()
                    # self.th.quit()
            for th in threadpool:
                th.start()
            for th in threadpool:
                QThread.exec(th)

    def edlMode(self):
        self.btn_start.setEnabled(False)
        global testType
        testType = "rebootEdl"
        if self.checkDevStatus():
            threadpool = []
            for i in range(5):
                if self.tableWidget.item(i,0) != None:
                    text = self.tableWidget.item(i,0).text()
                    th = MyThread(text)
                    th.sinOutStatus.connect(self.devStatus)
                    th.sinOutProgress.connect(self.devProgress)
                    threadpool.append(th)
            for th in threadpool:
                th.start()
            for th in threadpool:
                QThread.exec(th)


    def selectUpFile(self):
        upFileName = QFileDialog.getOpenFileName(self,"选择文件")
        self.lineEdit.setText(upFileName[0])

    def selectDownFile(self):
        downFileName = QFileDialog.getOpenFileName(self,"选择文件")
        self.lineEdit_2.setText(downFileName[0])

    def checkDevStatus(self):
        for i in range(5):
            if self.tableWidget.item(i,1) != None:
                text = self.tableWidget.item(i,1).text()
                if text != "normal":
                    a = QMessageBox.warning(self,"错误","存在至少一台设备未授权或连接不稳定",QMessageBox.Ok)
                    return False
        return True
    
    # def addProgressBar(self,_index=0,):
    #     qbar = QProgressBar()
    #     qbar.setValue(0)
    #     qbar.setStyleSheet("QProgressBar{color:black}")
    #     self.tableWidget.setCellWidget(_index,2,qbar)

    def devStatus(self,devid,devstate):
        for i in range(5):
            if self.tableWidget.item(i, 0) != None:
                text = self.tableWidget.item(i, 0).text()
                if text == devid:
                    newItem_deivceId = QTableWidgetItem(devstate)
                    self.tableWidget.setItem(i,1,newItem_deivceId)

    def devProgress(self,devid,int_value):
        for i in range(5):
            if self.tableWidget.item(i, 0) != None:
                text = self.tableWidget.item(i, 0).text()
                if text == devid:
                    qbar = QProgressBar()
                    qbar.setValue(int_value)
                    qbar.setStyleSheet("QProgressBar{color:black}")
                    self.tableWidget.setCellWidget(i, 2, qbar)
                    # self.pbar.setValue(int_value)
                    # self.pbar.setStyleSheet("QProgressBar{color:black}")
                    # self.tableWidget.setCellWidget(i, 2, self.pbar)

if __name__ == '__main__':
    import ctypes
    whnd = ctypes.windll.kernel32.GetConsoleWindow()
    if whnd != 0:
        ctypes.windll.user32.ShowWindow(whnd, 0)
        ctypes.windll.kernel32.CloseHandle(whnd)
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())