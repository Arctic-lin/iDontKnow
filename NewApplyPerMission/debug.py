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
from subprocess import check_output,getstatusoutput,call
from re import findall
from time import sleep
import logging

logging.basicConfig(level= logging.DEBUG,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',filename="ToolsLog.log",filemode="a+")
logger = logging.getLogger(__name__)
dict_config = {"monkeylog":"0","mute":"0","only_apply":"0","adb_switch":"0","adb_content":"0","sh_nohup":"1","gcc":0}
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
		devices_info = check_output("adb devices", encoding="utf-8")
		dut_sn = findall ("\n" + "(.*?)" + r"\tdevice", devices_info)
		for i in dut_sn:
			dev_sn.append(i)

	def getPermission(self):
		# 获取手机所有包名
		allGrantCmd = []
		allPackageCmd = check_output \
			("adb shell monkey -c android.intent.category.LAUNCHER  -v -v -v 0", encoding="utf-8")
		rePackage = findall("from\spackage\s*" + "(.*?)" + "\\)", allPackageCmd)
		for pkg in rePackage:
			get_permmsion_cmd = check_output \
				("adb shell dumpsys package %s | grep granted=false" % pkg, encoding="utf-8")
			get_permmsion = findall("\s*" + "(.*?)" + "\\:", get_permmsion_cmd)
			for p in get_permmsion:
				allGrantCmd.append("pm grant %s %s" % (pkg, p))
		return allGrantCmd

	def write_script(self,dict_config_para):
		# app_total = self.get_dut_package()

		allGrantCmd = self.getPermission()
		print(allGrantCmd)
		# app_name = app_total[0]
		# app_cmd = app_total[-1]
		with open("main.sh","w",encoding="utf-8",newline="\n") as f:
			f.writelines("settings put system screen_off_timeout 1\n")
			if dict_config_para["only_apply"] == "1":
				# for i in app_name:
				# 	for j in app_cmd:
				# 		f.writelines("pm grant %s %s\n" % (i,j))
				for i in allGrantCmd:
					f.writelines("%s\n" % (i))
				f.writelines("am start com.android.settings\n")
			elif dict_config_para["only_apply"] == "0":
				if dict_config_para["monkeylog"] == "1":
					f.writelines("setprop debug.print.log false\n")
				if dict_config_para["gcc"] == "1":
					f.writelines("setprop debug.tct.enable_monkey_log false\n")
				# for i in app_name:
				# 	for j in app_cmd:
				# 		f.writelines("pm grant %s %s\n" % (i,j))
					for i in allGrantCmd:
						f.writelines("%s\n" % (i))
				f.writelines("am start com.android.settings\n")
				if dict_config_para["adb_switch"] == "1":
					adb_cmd = dict_config_para["adb_content"].split(";")
					for i in adb_cmd:
						f.writelines(i + "\n")
				if dict_config_para["mute"] == "1":
					if dict_config_para["sh_nohup"] is not None:
						if dict_config_para["sh_nohup"] == "1":
							f.write (r"nohup sh /data/local/tmp/Mute.sh&")
						elif dict_config_para["sh_nohup"] == "0":
							f.write (r"sh /data/local/tmp/Mute.sh&")
					else:
						f.write (r"sh /data/local/tmp/Mute.sh&")
		logger.info("Write main.sh")
		with open("main.txt","w",encoding="utf-8") as f:
			if dict_config_para["sh_nohup"] is not None:
				if dict_config_para["sh_nohup"] == "1":
					f.write (r"cd /data/local/tmp" + "\n" + "nohup sh main.sh&" + "\n")
				elif dict_config_para["sh_nohup"] == "0":
					f.write (r"cd /data/local/tmp" + "\n" + "sh main.sh&" + "\n")
			else:
				f.write (r"cd /data/local/tmp" + "\n" + "sh main.sh&" + "\n")
			logger.info ("Write main.txt")
			call ("adb wait-for-device")
			script_cmds = [r"adb wait-for-device", r"adb push main.sh /data/local/tmp/"]
			if dict_config_para["mute"] == "1":
				script_cmds.insert (2, r"adb push Mute.sh /data/local/tmp")
		return script_cmds

	def run(self):
		print(dict_config)
		logger.info("Thread Running")
		self.sinOut.emit ("初始化中..请插入手机")
		write = self.write_script (dict_config)
		logger.info("Start loop")
		while self.working:
			logger.info("<<<Wait-For-Device>>>")
			self.sinOut.emit("等待设备连接...")
			check_output ("adb wait-for-device")
			run_cmd=[]
			devices_info = check_output ("adb devices", encoding="utf-8")
			dut_sn = findall ("\n" + "(.*?)" + r"\tdevice", devices_info)
			for i in write:
				if "wait-for-device" in i:
					run_cmd.append(i)
				else:
					i = i[:4] + "-s %s"%dut_sn[0] + i[3:]
					run_cmd.append(i)
			check_output(run_cmd[0])
			self.sinOut.emit("正在执行脚本..请确认手机已插入")
			for i in run_cmd:
				if i != run_cmd[0]:
					check_output(i,shell=True)
					if i == run_cmd[-1]:
						finger_print = check_output("adb shell getprop ro.build.fingerprint",encoding="utf-8")
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
			getstatusoutput(r"adb -s %s shell < main.txt"%dut_sn[0])

class parent_MainWindow(QMainWindow,Ui_MainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.main_ui = Ui_MainWindow()
		self.setupUi(self)
		#self.dir_path = os.path.dirname (os.path.abspath (__file__))
		self.thread=Thread_1()
		self.thread.sinOut.connect (self.textEdit_info)
	def start_sh(self):
		pass
	def textEdit_info(self,text_str):
		pass
	def end(self):
		pass

if __name__ == '__main__':
	import ctypes
	whnd = ctypes.windll.kernel32.GetConsoleWindow ()
	if whnd != 0:
		ctypes.windll.user32.ShowWindow (whnd, 0)
		ctypes.windll.kernel32.CloseHandle (whnd)
	app = QApplication(sys.argv)
	window = parent_MainWindow()
	# child = child_dialog()
	# btn = window.btn_addProject
	# btn.clicked.connect(child.show)
	window.show()
	sys.exit(app.exec_())