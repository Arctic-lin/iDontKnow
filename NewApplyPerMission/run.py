# -*- coding: utf-8 -*-
# @Time    : 2020/6/4 11:57
# @Author  : Arctic
# @FileName: debug.py
# @Software: PyCharm
# @Purpose :
import sys
from newMainUi import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.Qt import QThread
from PyQt5.QtCore import pyqtSignal
import subprocess
import re

checkBox_Status = {"onlyApply": 0 , "nohup":0 , "monkeyTest" : 0 }
run_script = {"start":0}
dev = []

class Thread_run(QThread):
    sinOut = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def __del__(self):
        self.work = False

    def getDevSN(self):
        # self.sinOut.emit("检测设备中...")
        devInfo = subprocess.check_output("adb devices", encoding="utf-8")
        devSN = re.findall("\n" + "(.*?)" + r"\tdevice", devInfo)
        return devSN
    # 推送脚本并执行
    def pushNrun(self):
        subprocess.call("adb wait-for-device")
        dev_id = self.getDevSN()
        if dev_id :
            if dev_id[0] not in dev:
                dev.append(dev_id[0])
                self.sinOut.emit("clear")
                devId = subprocess.check_output("adb shell getprop ro.serialno", encoding="utf-8").strip("\n")
                fingerPrint = subprocess.check_output \
                    ("adb shell getprop ro.build.version.incremental", encoding="utf-8").strip("\n")
                self.sinOut.emit("clear")
                self.sinOut.emit("Device:%s\nVersion:%s" % (devId, fingerPrint))
                self.sinOut.emit("推送脚本中...")
                subprocess.call(r"adb push main.sh /data/local/tmp")
                if checkBox_Status["monkeyTest"] == 1:
                    subprocess.call(r"adb push Mute.sh /data/local/tmp")
                self.sinOut.emit("推送完成")
                # QThread.sleep(1)
                self.sinOut.emit("脚本后台执行完成,请更换下一台手机")
                subprocess.check_output("adb shell < main.txt",encoding="utf-8",shell=True)

    def run(self):
        self.work = True
        while self.work:
            self.pushNrun()

class Thread_init_dev(QThread):
    sinOut = pyqtSignal(str)
    sinOut_buttonEnable = pyqtSignal(bool)
    sinOut_initButton = pyqtSignal(bool)
    def __init__(self):
        super().__init__()

    def __del__(self):
        self.sinOut_initButton.emit(False)

    def getDevSN(self):
        self.sinOut.emit("检测设备中...")
        devInfo = subprocess.check_output("adb devices", encoding="utf-8")
        devSN = re.findall("\n" + "(.*?)" + r"\tdevice", devInfo)
        if devSN:
            if len(devSN) > 1:
                self.sinOut.emit("插入手机过多，仅支持一台手机")
                return False
            else:
                self.sinOut.emit("已检测到设备：%s"%devSN[0])
                return True
        else:
            self.sinOut.emit("未检测到设备")
            return False

    # 示例:通过dumpsys package $package | grep false 获取手机APK缺少的权限
    def getPermmsion(self):
        allGrantCmd = []
        allPkg = subprocess.check_output\
            ("adb shell monkey -c android.intent.category.LAUNCHER  -v -v -v 0" , encoding="utf-8")
        re_allPkg = re.findall("from\spackage\s*" + "(.*?)" + "\\)", allPkg)
        for pkg in re_allPkg:
            try:
                getFalse = subprocess.check_output\
                    ("adb shell dumpsys package %s | grep granted=false" % pkg, encoding= "utf-8")
            except subprocess.CalledProcessError as e:
                print(e)
            else:
                if getFalse:
                    re_getFalse = re.findall("\s*" + "(.*?)" + "\\:", getFalse)
                    for p in re_getFalse:
                        allGrantCmd.append("pm grant %s %s" % (pkg,p))
        return allGrantCmd

    #通过pm list package 获取手机内置log工具是哪个
    def getDevLog(self):
        log_tools = {
            "com.tcl.logger" : "am startservice -n com.tcl.logger/com.tcl.logger.service.LogSwitchService -a com.tcl.logger.turnon",
            "com.debug.loggerui" : "am broadcast -a com.debug.loggerui.ADB_CMD -e cmd_name start --ei cmd_target 1 -f 0x01000000",
            "com.tct.feedback" : "am start com.tct.feedback/.external.activity.MainActivity",
            "com.mediatek.mtklogger": "am broadcast -a com.mediatek.mtklogger.ADB_CMD -e cmd_name start --ei cmd_target 1"
        }
        for tools in log_tools.items():
            pmList = subprocess.check_output\
                ("adb shell pm list package %s" % (tools[0]),encoding="utf-8")
            if pmList:
                return tools[1]
    #生成脚本
    def creatShellScript(self):
        print(checkBox_Status)
        if checkBox_Status["onlyApply"] == 1:
            self.sinOut.emit("执行类型：仅执行")
        elif checkBox_Status["monkeyTest"] == 1:
            self.sinOut.emit("执行类型：MonkeyTest")
        if checkBox_Status["nohup"] == 1:
            self.sinOut.emit("脚本后台执行方式：nohup sh xx.sh&\n初始化中..")
        else:
            self.sinOut.emit("脚本后台执行方式: sh xx.sh&\n初始化中..")
        allGrantCmd = self.getPermmsion()
        if allGrantCmd:
            log_tools = self.getDevLog()
            with open("main.sh","w",encoding = "utf-8",newline = "\n") as f:
                # 设置never sleep
                f.writelines("settings put system screen_off_timeout 1\n")
                #遍历写入授权指令
                ### Check Monkey Test
                for i in allGrantCmd:
                    f.writelines("%s\n" % i)
                ### 仅授权则添加am启动Settings来辨识脚本执行完成
                if checkBox_Status["onlyApply"] == 1:
                    f.writelines("am start com.android.settings\n")
                ### Monkey测试,直接写入两种 屏蔽Monkey的方式,HZ&SZ两种方案
                elif checkBox_Status["monkeyTest"] == 1:
                    f.writelines("setprop debug.print.log false\n")
                    f.writelines("setprop debug.tct.enable_monkey_log false\n")
                    #通过
                    if log_tools:
                        f.writelines(log_tools + "\n")
                    ### 写入执行静音脚本指令
                    if checkBox_Status["nohup"] == 1:
                        f.writelines(r"nohup sh /data/local/tmp/Mute.sh&" + "\n")
                    else:
                        f.writelines(r"sh /data/local/tmp/Mute.sh&" + "\n")

            #编写执行脚本
            with open("main.txt","w",encoding="utf-8") as f:
                if checkBox_Status["nohup"] == 1:
                    f.write(r"cd /data/local/tmp" + "\n" + "nohup sh main.sh&" + "\n")
                else:
                    f.write(r"cd /data/local/tmp" + "\n" + "sh main.sh&" + "\n")
            self.sinOut.emit("clear")
            self.sinOut.emit("初始化完成")
            self.sinOut_initButton.emit(True)
            return True
        else:
            self.sinOut.emit("手机无需授权，请检查并更换手机初始化")
            self.sinOut_initButton.emit(False)
            return False

    def run(self):
        self.sinOut_buttonEnable.emit(True)
        if self.getDevSN():
            if self.creatShellScript():
                self.sinOut_buttonEnable.emit(False)


class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui = Ui_MainWindow()
        self.setupUi(self)
        self.thread_init_dev = Thread_init_dev()
        self.thread_init_dev.sinOut.connect (self.textEdit_Info)
        self.thread_init_dev.sinOut_buttonEnable.connect (self.init_Device_Button)
        self.thread_init_dev.sinOut_initButton.connect (self.init_Done)
        self.thread_run_script = Thread_run()
        self.thread_run_script.sinOut.connect (self.textEdit_Info)

    # 点击init
    def init_Device(self):
        if self.checkBox_monkeyTest.isChecked() is False and self.checkBox_onlyApply.isChecked() is False :
            self.plainTextEdit.setPlainText("必须选择测试类型,仅授权 or MonkeyTest")
            return
        self.checkBox_status()
        self.thread_init_dev.start()

    # 点击初始化，Disable其他push button
    def init_Device_Button(self,bool):
        if bool == True:
            self.pushButton_start.setDisabled(bool)
            self.pushButton_stop.setDisabled(bool)
            self.checkBox_onlyApply.setDisabled(bool)
            self.checkBox_monkeyTest.setDisabled(bool)
            self.checkBox_nohup.setDisabled(bool)
        elif bool== False:
            self.pushButton_start.setDisabled(bool)
            self.pushButton_stop.setDisabled(bool)

    #点击结束，Enable所有控件
    def init_Done(self,bool):
        if bool == False:
            self.pushButton_init.setDisabled(bool)
            self.checkBox_nohup.setDisabled(bool)
            if checkBox_Status["onlyApply"] == 1:
                self.checkBox_monkeyTest.setEnabled(bool)
                self.checkBox_onlyApply.setDisabled(bool)
            else:
                self.checkBox_onlyApply.setEnabled(bool)
                self.checkBox_monkeyTest.setDisabled(bool)
        else:
            self.pushButton_init.setDisabled(bool)
            self.checkBox_nohup.setDisabled(bool)
            self.checkBox_monkeyTest.setDisabled(bool)
            self.checkBox_onlyApply.setDisabled(bool)


    def start_Script(self):
        self.thread_run_script.start()


    def end_Script(self):
        # self.thread_init_dev.__del__()
        # self.thread_run_script.__del__()
        # self.plainTextEdit.appendPlainText("?")
        sys.exit(app.exec_())


    def textEdit_Info(self,text):
        if text == "clear":
            self.plainTextEdit.clear()
        else:
            self.plainTextEdit.appendPlainText(text)

    #检测Checkbox状态并返回值
    def checkBox_status(self):
        if self.checkBox_onlyApply.isChecked():
            current_status = {"onlyApply": 1}
        else:
            current_status = {"onlyApply": 0}
        checkBox_Status.update(current_status)
        if self.checkBox_monkeyTest.isChecked():
            current_status = { "monkeyTest": 1}
        else:
            current_status = {"monkeyTest": 0}
        checkBox_Status.update(current_status)
        if self.checkBox_nohup.isChecked():
            current_status = {"nohup": 1}
        else:
            current_status = {"nohup": 0}
        checkBox_Status.update(current_status)

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