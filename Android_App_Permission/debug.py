 # -*- coding: utf-8 -*-
# @Time    : 2019/12/17 10:39
# @Author  : Arctic
# @FileName: debug.py
# @Software: PyCharm
# @Purpose :AppPermission重构

import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QDialog,QMessageBox
from PyQt5.Qt import QThread
from PyQt5.QtCore import pyqtSignal
from APP_Permission_Main import Ui_MainWindow
from APP_Permission_dialog import Ui_Dialog
from getconfigs import GetConfigs
import subprocess
import re
from time import sleep
import logging
import PyQt5.sip

logging.basicConfig(level= logging.DEBUG,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',filename="ToolsLog",filemode="a+")
logger = logging.getLogger(__name__)
dict_config = {"monkeylog":"0","mute":"0","only_apply":"0","adb_switch":"0","adb_content":"0"}
logger.info("============================================")
dev_sn=[]
class Thread_1(QThread):
	sinOut = pyqtSignal(str)
	def __init__(self):
		super().__init__()
	def __del__(self):
		self.working = False
		self.sinOut.emit("结束")
		logger.info("End...")
	def __start__(self):
		dev_sn.clear()
		self.working = True
		self.get_dut_sn()
		logger.info("Dev_sn=%s  Work Status=%s"%(str(dev_sn),str(self.working)))
	def get_dut_sn(self):
		devices_info = subprocess.check_output ("adb devices", encoding="utf-8")
		dut_sn = re.findall ("\n" + "(.*?)" + r"\tdevice", devices_info)
		for i in dut_sn:
			dev_sn.append(i)

	def get_dut_package(self):
		logger.info ("<<<Wait-For-Device>>>")
		a=subprocess.getstatusoutput("adb wait-for-device")
		app_cmd = ["android.permission.READ_CONTACTS",
				   "android.permission.WRITE_CONTACTS",
				   "android.permission.GET_ACCOUNTS",
				   "android.permission.READ_PHONE_STATE",
				   "android.permission.CALL_PHONE",
				   "android.permission.READ_CALENDAR",
				   "android.permission.WRITE_CALENDAR",
				   "android.permission.READ_CALL_LOG",
				   "android.permission.WRITE_CALL_LOG",
				   "android.permission.CAMERA",
				   "android.permission.ACCESS_FINE_LOCATION",
				   "android.permission.ACCESS_COARSE_LOCATION",
				   "android.permission.READ_EXTERNAL_STORAGE",
				   "android.permission.WRITE_EXTERNAL_STORAGE",
				   "android.permission.RECORD_AUDIO",
				   "android.permission.READ_SMS"]
		get_pack=subprocess.getstatusoutput ("adb shell  monkey -c android.intent.category.LAUNCHER  -v -v -v 0")
		logger.info("Get Monkey Package...")
		pattern = re.findall ("from package.*",get_pack[-1])
		app_name = []
		for i in pattern:
			i = i.replace ("from package ", "").replace (")", "")
			app_name.append (i)
		return app_name, app_cmd
	def write_script(self,dict_config_para):
		app_total = self.get_dut_package()
		app_name = app_total[0]
		app_cmd = app_total[-1]
		with open("main.sh","w",encoding="utf-8",newline="\n") as f:
			f.writelines("settings put system screen_off_timeout 1\n")
			if dict_config_para["only_apply"] == "1":
				for i in app_name:
					for j in app_cmd:
						f.writelines("pm grant %s %s\n" % (i,j))
				f.writelines("am start com.android.settings\n")
			elif dict_config_para["only_apply"] == "0":
				if dict_config_para["monkeylog"] == "1":
					f.writelines("setprop debug.print.log false\n")
				for i in app_name:
					for j in app_cmd:
						f.writelines("pm grant %s %s\n" % (i,j))
				if dict_config_para["adb_switch"] == "1":
					adb_cmd = dict_config_para["adb_content"].split(";")
					for i in adb_cmd:
						f.writelines(i + "\n")
				if dict_config_para["mute"] == "1":
					f.write(r"sh /data/local/tmp/Mute.sh&")
		logger.info("Write main.sh")
		with open("main.txt","w",encoding="utf-8") as f:
			f.write(r"cd /data/local/tmp"+"\n"+"sh main.sh&")
			logger.info ("Write main.txt")
			subprocess.call ("adb wait-for-device")
			script_cmds = [r"adb wait-for-device", r"adb push main.sh /data/local/tmp/"]
			if dict_config_para["mute"] == "1":
				script_cmds.insert (2, r"adb push Mute.sh /data/local/tmp")
			# for j in script_cmds:
			# 	subprocess.call(j,shell=True)
			# 	sleep(2)
		return script_cmds

	def run(self):
		logger.info("Thread Running")
		self.sinOut.emit ("初始化中..请插入手机")
		write = self.write_script (dict_config)
		logger.info("Start loop")
		while self.working:
			logger.info("<<<Wait-For-Device>>>")
			self.sinOut.emit("等待设备连接...")
			subprocess.check_output ("adb wait-for-device")
			run_cmd=[]
			devices_info = subprocess.check_output ("adb devices", encoding="utf-8")
			dut_sn = re.findall ("\n" + "(.*?)" + r"\tdevice", devices_info)
			for i in write:
				if "wait-for-device" in i:
					run_cmd.append(i)
				else:
					i = i[:4] + "-s %s"%dut_sn[0] + i[3:]
					run_cmd.append(i)
			subprocess.check_output(run_cmd[0])
			self.sinOut.emit("正在执行脚本..请确认手机已插入")
			for i in run_cmd:
				if i != run_cmd[0]:
					subprocess.check_output(i,shell=True)
					if i == run_cmd[-1]:
						finger_print = subprocess.check_output("adb shell getprop ro.build.fingerprint",encoding="utf-8")
						self.sinOut.emit("%s:\n"
										 "%s\n"
										 "脚本已推送完成,请更换手机..."%(dut_sn[0],finger_print[0:-2]))
						if dev_sn:
							logger.debug("%s:\n"
										 "%s\n"
										 "脚本已推送完成,请更换手机..."%(dut_sn[0],finger_print[0:-2]))
						else:
							logger.info("Push script finished,pls puls-in other phone!!!")
			sleep(2)
			subprocess.getstatusoutput(r"adb -s %s shell < main.txt"%dut_sn[0])

class parent_MainWindow(QMainWindow,Ui_MainWindow):
	def __init__(self):
		self.cfg = GetConfigs()
		self.section = self.cfg.getallsection()
		QMainWindow.__init__(self)
		self.main_ui = Ui_MainWindow()
		self.setupUi(self)
		logger.info("Loading Default Config: %s"%self.comboBox.currentText())
		#self.dir_path = os.path.dirname (os.path.abspath (__file__))
		self.thread=Thread_1()
		self.thread.sinOut.connect (self.textEdit_info)
	def start_sh(self):
		if self.checkBox_onlyapply.isChecked():
			dict_config["only_apply"] = "1"
			dict_config["monkeylog"] = "0"
			dict_config["mute"] = "0"
			dict_config["adb_switch"] = "0"
			dict_config["adb_content"] = "0"
		else:
			dict_config["only_apply"] = "0"
			if self.checkBox_mute.isChecked():
				dict_config["mute"] = "1"
			else:
				dict_config["mute"] = "0"
			if self.checkBox_monkeylog.isChecked():
				dict_config["monkeylog"] = "1"
			else:
				dict_config["monkeylog"] = "0"
			if self.cfg.getstr(self.comboBox.currentText(),"need_adb") == "1":
				dict_config["adb_switch"] = "1"
				dict_config["adb_content"] = self.cfg.getstr(self.comboBox.currentText(),"adb_content")
			else:
				dict_config["adb_switch"] = "0"
				dict_config["adb_content"] = "None"
		self.btn_addProject.setEnabled(False)
		self.btn_start.setEnabled(False)
		logger.info("Update info:%s"%str(dict_config))
		self.thread.__start__ ()
		if len(dev_sn) == 0:
			button = QMessageBox.warning (self, "Warning", "请连接手机后再点击执行", QMessageBox.Yes)
			if button == QMessageBox.Yes:
				logger.info ("Error:未连接手机")
				self.end()
				return False
		elif len (dev_sn) > 1:
			button = QMessageBox.warning (self, "Warning", "目前仅支持单台设备,请勿连接多台设备", QMessageBox.Yes)
			if button == QMessageBox.Yes:
				logger.info("Error:连接多台设备")
				self.end()
				return False
		logger.info("Thread status:%s"%str(self.thread.working))
		self.thread.start ()
	def textEdit_info(self,text_str):
		if "\n" in text_str:
			text_str = text_str.split("\n")
			self.textEdit.setPlainText(text_str[0]+"\n"+text_str[1]+"\n"+text_str[-1])
		else:
			self.textEdit.setPlainText(text_str)
	def end(self):
		self.thread.__del__()
		logger.info ("Thread status:%s" % str (self.thread.working))
		self.btn_start.setEnabled(True)
		self.btn_addProject.setEnabled(True)

class child_dialog(QDialog,Ui_Dialog):
	def __init__(self):
		QDialog.__init__(self)
		self.cfg = GetConfigs ()
		self.child = Ui_Dialog()
		self.child.setupUi(self)
		#self.dir_path = os.path.dirname (os.path.abspath (__file__))




if __name__ == '__main__':
	import ctypes
	whnd = ctypes.windll.kernel32.GetConsoleWindow ()
	if whnd != 0:
		ctypes.windll.user32.ShowWindow (whnd, 0)
		ctypes.windll.kernel32.CloseHandle (whnd)
	app = QApplication(sys.argv)
	window = parent_MainWindow()
	child = child_dialog()
	btn = window.btn_addProject
	btn.clicked.connect(child.show)
	window.show()
	sys.exit(app.exec_())