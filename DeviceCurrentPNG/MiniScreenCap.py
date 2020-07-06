# -*- coding: utf-8 -*-
# @Time    : 2020/7/6 16:41
# @Author  : Arctic
# @FileName: MiniScreenCap.py
# @Software: PyCharm
# @Purpose :

import sys
import os
from MiniScreenCapUI import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow,QApplication,QComboBox
from PyQt5.Qt import QThread
from PyQt5.QtCore import pyqtSignal
import subprocess
import re
from PIL import Image

sed = r"D:\Program\Git\usr\bin\sed.exe"
currentDev = ""
indexx = 0
class CustomComboBox(QComboBox):
    popUP = pyqtSignal()

    def __init__(self,parent = None):
        super(CustomComboBox,self).__init__(parent)

    def showPopup(self):
        self.clear()
        self.insertItem(0,"None")
        index = 1
        devInfo = subprocess.check_output("adb devices", encoding="utf-8")
        devSN = re.findall("\n" + "(.*?)" + r"\tdevice", devInfo)
        if devSN:
            for i in devSN:
                self.insertItem(index,i)
                index += 1
        QComboBox.showPopup(self)

class Thread_getPNG(QThread):
    sinOut = pyqtSignal(list)

    def __init__(self):
        super().__init__()

    def callShell(self):
        imgName = "%s_%d"%(currentDev,indexx)
        subprocess.check_output("adb -s %s shell screencap -p | %s 's/\r$//' > ./%s.png"%(currentDev,sed,imgName),shell=True)
        img = Image.open("%s.png"%imgName)
        img.show()
    def run(self):
        self.callShell()

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui = Ui_MainWindow()
        self.setupUi(self)
        self.comboBox.close()
        self.comboBox = CustomComboBox(self.layoutWidget)
        self.horizontalLayout.addWidget(self.comboBox)
        self.Thread_getPNG = Thread_getPNG()
    def getPNG(self):
        global currentDev
        global indexx
        indexx += 1
        currentDev = self.comboBox.currentText()
        self.Thread_getPNG.start()
    def getDev(self):
        pass

    # def addComboxItem(self,sin_list):
    #     if sin_list:
    #         self.comboBox.addItems(sin_list)
if __name__ == '__main__':
    # import ctypes
    # whnd = ctypes.windll.kernel32.GetConsoleWindow()
    # if whnd != 0:
    #     ctypes.windll.user32.ShowWindow(whnd, 0)
    #     ctypes.windll.kernel32.CloseHandle(whnd)
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    # a="s/\r$//"
    # # subprocess.check_output("adb shell 'screencap -p | sed %s' > D:\Test.png"%a, shell=False)
    # subprocess.check_output("adb shell screencap -p | %s '%s' > D:\Test.png" % ("sed.exe",a), shell=True)