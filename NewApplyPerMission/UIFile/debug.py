# -*- coding: utf-8 -*-
# @Time    : 2020/6/4 11:57
# @Author  : Arctic
# @FileName: debug.py
# @Software: PyCharm
# @Purpose :
import sys
from NewApplyPerMission.UIFile.mainui import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.Qt import QThread
from PyQt5.QtCore import pyqtSignal
import subprocess
import re

class Thread_getDevSN(QThread):
    sinOut = pyqtSignal(list)
    
    def __init__(self):
        super().__init__()
    
    def getDevSN(self):
        devInfo = subprocess.check_output("adb devices", encoding="utf-8")
        devSN = re.findall( "\n" + "(.*?)" + r"\tdevice" , devInfo)
        return devSN

    def __start__(self):
        devSN = self.getDevSN()
        self.sinOut.emit(devSN)

    
class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui = Ui_MainWindow()
        self.setupUi(self)
        self.thread_getDevSN = Thread_getDevSN()
        self.thread_getDevSN.sinOut.connect(self.addItemsDevSN)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())