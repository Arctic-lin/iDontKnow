# -*- coding: utf-8 -*-
# @Time    : 2020/7/14 10:46
# @Author  : Arctic
# @FileName: main.py
# @Software: PyCharm
# @Purpose :
import logging
logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
import sys
from fota import Ui_Dialog_FOTA
from installAPK import Ui_Dialog_installAPK
from mute import Ui_Dialog_mute
from pushFile import Ui_Dialog_pushfile
from userAddCommond import Ui_Dialog_useradd
from multiADB_mainUI import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget,QDialog,QFileDialog,QTableWidgetItem,QMessageBox,QPushButton
from PyQt5 import QtCore,QtGui
from PyQt5.QtCore import pyqtSignal
from PyQt5.Qt import QThread
import subprocess
import re

fota_test = {}
mute_test = {}
pushFile_test = {}
install_test = {}
Edl_mode = False
userDefine = {}
monkeyPreset = {}

class GetDevThread(QThread):
    def __init__(self):
        super().__init__()
    def getDevSN(self):
        devInfo = subprocess.check_output("adb devices", encoding="utf-8")
        devSN = re.findall("\n" + "(.*?)" + r"\t" + "(device|unauthorized|offline)", devInfo)
        return devSN

#mainWindows
class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui = Ui_MainWindow()
        self.setupUi(self)
        self.contorl_btn = [self.btn_singleADB,self.btn_monkeyPreSet,self.btn_downloadMode,self.btn_pushFile,
               self.btn_installAPK,self.btn_fota,self.btn_mute
               ]
        for i in self.contorl_btn:
            i.setEnabled(False)
    #槽函数
    def main_run(self):
        if fota_test:
            logger.info("执行FOTA测试")
        # elif:
        #     pass
    def main_fotaTest(self):
        # self.hide()
        logger.info("%s"%self.btn_fota.text())
        self.dia_fota = Ui_Dialog_fota()
        self.dia_fota.show()
        self.disableFucBTN(self.btn_fota)
    def main_mute(self):
        logger.info("%s" % self.btn_mute.text())
        self.dia_mute = Ui_Dialog_mute_1()
        self.dia_mute.show()
    def main_downloadMode(self):
        logger.info("%s" % self.btn_downloadMode.text())
        pass
    def main_pushfile(self):
        logger.info("%s" % self.btn_pushFile.text())
        self.dia_pushFile = Ui_Dialog_pushFile()
        self.dia_pushFile.show()
    def main_installAPK(self):
        logger.info("%s" % self.btn_installAPK.text())
        self.dia_install = Ui_Dialog_install()
        self.dia_install.show()
    def main_usercho(self):
        logger.info("%s" % self.btn_singleADB.text())
        self.dia_useradd = Ui_Dialog_userAdd()
        self.dia_useradd.show()
    def main_monkeyPreset(self):
        logger.info("%s" % self.btn_monkeyPreSet.text())
        pass
        # self.dia_monkeyPreset = Ui_dialog_
    def main_freshDev(self):
        logger.info("%s" % self.btn_freshDdev.text())
        for i in self.contorl_btn:
            i.setEnabled(False)
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
                    self.tableWidget.setItem(i,0,newItem_deivceId)
                    self.tableWidget.setItem(i,1,newItem_status)
                    logger.info("检测到设备:%s,连接状态:%s"%(devSN[i][0],devSN[i][-1]))
        else:
            logger.info("未检测到连接设备")

    def main_lockDev(self):
        logger.info("%s" % self.btn_confimDev.text())
        pare = {self.btn_fota:fota_test,self.btn_pushFile:pushFile_test,self.btn_mute:mute_test,
                self.btn_monkeyPreSet:monkeyPreset,self.btn_singleADB:userDefine,self.btn_installAPK:install_test,
                self.btn_downloadMode:Edl_mode
                }
        for i in pare:
            if pare[i]:
                i.setEnabled(True)
            else:
                i.setEnabled(True)

    def disableFucBTN(self,btn):
        for i in self.contorl_btn:
            if i == btn:
                i.setEnabled(True)
            else:
                i.setEnabled(False)

#FOTA Dialog
class Ui_Dialog_fota(QDialog,Ui_Dialog_FOTA):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

    #槽函数
    def getData(self):
        fota_test.clear()
        self.linetext_data = {self.label_upgrade.text(): self.lineEdit_upgrade.text(),
                              self.label_downgrade.text(): self.lineEdit_downgrade.text(),
                              self.label_apkfile.text(): self.lineEdit_apk.text(),
                              self.label_pushdir.text(): self.lineEdit_phonedir.text()
                              }
        for i in self.linetext_data:
            if self.linetext_data[i] :
                fota_test[i] = self.linetext_data[i]
            else:
                button = QMessageBox.warning(self, "Warning", "%s路径不能为空"%i, QMessageBox.Yes)
                if button == QMessageBox.Yes:
                    logger.info("%s路径不能为空"%i)
                    return False
        if fota_test:
            for i in fota_test:
                logger.info("%s%s"%(i,fota_test[i]))
            self.accept()

    def choUpFile(self):
        upFile = QFileDialog.getOpenFileName (self,"选择文件",filter="APK file (*.zip)")
        if upFile:
            self.lineEdit_upgrade.setText(upFile[0])
            logger.info("%s"%upFile[0])
    def choDoFile(self):
        downFile = QFileDialog.getOpenFileName(self,"选择文件",filter="APK file (*.zip)")
        if downFile:
            self.lineEdit_downgrade.setText(downFile[0])
            logger.info("%s" % downFile[0])
    def choApkFile(self):
        apkFile = QFileDialog.getOpenFileName(self,"选择文件",filter="APK file (*.apk)")
        if apkFile:
            self.lineEdit_apk.setText(apkFile[0])
            logger.info("%s" % apkFile[0])

#installApk Dialog
class Ui_Dialog_install(QDialog,Ui_Dialog_installAPK):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
    #槽函数
    def chooseAPK(self):
        apkFile = QFileDialog.getOpenFileName(self, "选择文件",filter="APK file (*.apk)")
        if apkFile:
            self.lineEdit_srcFile.setText(apkFile[0])
            logger.info("%s"%apkFile[0])

    def chooseDir(self):
        apkdir = QFileDialog.getExistingDirectory(self,"选择目录")
        if apkdir:
            self.lineEdit_srcFile.setText(apkdir)
            logger.info("%s"%apkdir)
    def getData(self):
        install_test.clear()
        if not self.lineEdit_srcFile.text():
            button = QMessageBox.warning(self, "Warning", "路径不能为空" , QMessageBox.Yes)
            if button == QMessageBox.Yes:
                logger.info("路径不能为空")
                return False
        else:
            install_test["install"] = self.lineEdit_srcFile.text()
            self.accept()
        # if self.lineEdit_srcFile.text():


#mute Dialog
class Ui_Dialog_mute_1(QDialog,Ui_Dialog_mute):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.diable_ui = [self.label_2,self.label_4,self.lineEdit]
        #设置输入规则
        _reg = QtCore.QRegExp('[1-9][0-9]{1,5}')
        self.lineEdit.setValidator(QtGui.QRegExpValidator(_reg,self))
        #默认选项
        if self.rbtn_mute_only.isChecked():
            for i in self.diable_ui:
                i.setEnabled(False)
    #槽函数,用于diable非选项
    def cho_only(self):
        for i in self.diable_ui:
            i.setEnabled(False)
    def cho_loop(self):
        for i in self.diable_ui:
            i.setEnabled(True)
    def getData(self):
        mute_test.clear()
        if self.rbtn_mute_only.isChecked():
            mute_test[0] = 0
        elif self.rbtn_mute_loop.isChecked():
            if not self.lineEdit.text():
                times = self.lineEdit.placeholderText()
                self.lineEdit.setText(times)
            mute_test[1] = self.lineEdit.text()
        for i in mute_test:
            if i == 0:
                logger.info("仅执行一次")
            elif i == 1:
                logger.info("循环执行,每隔%s秒执行一次"%mute_test[1])
        self.accept()
    # def choUpFile(self):
    #     pass
    # def choDoFile(self):
    #     pass
    # def choApkFile(self):
    #     pass

#pushFile Dialog
class Ui_Dialog_pushFile(QDialog,Ui_Dialog_pushfile):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
    #槽函数
    def chooseSrcFile(self):
        scrFile = QFileDialog.getOpenFileName(self, "选择文件")
        if scrFile:
            self.lineEdit_srcFile.setText(scrFile[0])
            logger.info("%s" % scrFile[0])
    def chooseToFile(self):
        toFile = QFileDialog.getExistingDirectory(self, "选择文件")
        if toFile:
            self.lineEdit_srcFile.setText(toFile)
            logger.info("%s" % toFile)
    def getData(self):
        pushFile_test.clear()
        self.linetext_data = {self.label.text(): self.lineEdit_srcFile.text(),
                              self.label_2.text(): self.lineEdit_tofile.text(),
                              }
        for i in self.linetext_data:
            if self.linetext_data[i]:
                pushFile_test[i] = self.linetext_data[i]
            else:
                button = QMessageBox.warning(self, "Warning", "%s路径不能为空" % i, QMessageBox.Yes)
                if button == QMessageBox.Yes:
                    logger.info("%s路径不能为空" % i)
                    return False
        if pushFile_test:
            for i in pushFile_test:
                logger.info("%s%s"%(i,pushFile_test[i]))
            self.accept()

    # def choApkFile(self):
    #     pass
    #

#userAdd Dialog
class Ui_Dialog_userAdd(QDialog,Ui_Dialog_useradd):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
    #槽函数
    def addAdb(self):
        pass
    def deleteAdb(self):
        pass
    # def choApkFile(self):
    #     pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())