# -*- coding: utf-8 -*-
# @Time    : 2019/12/9 10:35
# @Author  : Arctic
# @FileName: memory_leak_GUI.py
# @Software: PyCharm
# @Purpose :Momory_leak_GUI

import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QDialog,QFileDialog,QMessageBox,QListWidget,QInputDialog
from PyQt5.Qt import QThread
from PyQt5.QtCore import pyqtSignal
from ui_memory import Ui_MainWindow
import subprocess
import re
import os
import webbrowser


file_dir = []
app_local_name = []
class Thread_1(QThread):
	sinOut = pyqtSignal(int)
	def __init__(self):
		super().__init__()
	def run(self):
		self.sinOut.emit(0)
		memory_leak_root=[]
		local_app = app_local_name[-1]
		for root,dirs,files in os.walk(file_dir[-1]):
			for file in files:
				if os.path.splitext(file)[0] == "meminfo_leak":
					memory_leak_root.append(os.path.abspath(os.path.join(root,file)))
				elif os.path.splitext(file)[0] == "mem_leaked":
					memory_leak_root.append (os.path.abspath (os.path.join (root, file)))
		self.sinOut.emit(20)
		mk_html = file_dir[-1] + "\\"+"memory_leak.html"
		print(mk_html)
		w = open(mk_html,"w")
		w.close()
		w = open(mk_html,"a+")
		message = """
				<html>
				<head></head>
				<body>
				</body>
				</html>"""
		w.write (message)
		self.sinOut.emit (40)
		int_value_count = 45
		for i in local_app:
			self.sinOut.emit(int_value_count)
			html_pack=[]
			html_mess=[]
			html_dir=[]
			for j in memory_leak_root:
				with open(j,"r") as f:
					for line in f.readlines():
						if i in line:
							if i not in html_pack:
								html_pack.append(i)
							html_mess.append(line)
							html_dir.append(j)
			dict_data = dict(zip(html_mess,html_dir))
			new_dict={}
			for k,v in dict_data.items():
				new_dict.setdefault(v,[]).append(k)
			for j in html_pack:
				message1 = """<body><h3 title='PackageName:'><mark>%s -- Total:%s</mark></h3></body>""" % (j, str (len (html_mess)))
				w.write (message1)
				for k in new_dict:
					for l in new_dict[k]:
						message2 = """
						<body>
						<p>%s</p>
						</body>"""%(l)
						w.write(message2)
					message2="""
					<body>
					<a href="file:///%s">%s</a>
					</body>
					"""%(os.path.dirname(k),k)
					w.write (message2)
			int_value_count = int_value_count +10
		w.close ()
		self.sinOut.emit (100)
		webbrowser.open (mk_html, new=1)

class Thread_2(QThread):
	def __init__(self):
		super().__init__()
	def run(self):
		pass

class main_MainWindow(QMainWindow,Ui_MainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.main_ui = Ui_MainWindow()
		self.setupUi(self)
		self.thread=Thread_1()
		self.thread.sinOut.connect(self.process_bar)

	def get_dut_package_f(self):
		#pack_name = subprocess.getstatusoutput ("adb shell monkey -c android.intent.category.LAUNCHER  -v -v -v  0 ")
		pack_name = subprocess.getstatusoutput ("adb shell monkey -c android.intent.category.LAUNCHER  -v -v -v  0 ")
		if pack_name[0] == 1:
			message_to_connect = QMessageBox.warning(self,"Warning","%s"%pack_name[-1])
			if message_to_connect == QMessageBox.Ok:
				return False
		elif pack_name[0] == 0:
			# pack_name = subprocess.check_output (
			# 	"adb shell monkey -c android.intent.category.LAUNCHER  -v -v -v  0 "
		  	# 								 , shell=True, encoding="utf-8")
			pack_name = subprocess.check_output ("adb shell pm list package" , shell=True, encoding="utf-8")
			#pattern = re.findall ("from package.*", pack_name)
			pattern = re.findall ("package:.*", pack_name)
			app_name = []
			tcl_pack = []
			for i in pattern:
				#i = i.replace ("from package ", "").replace (")", "")
				i = i.replace("package:","")
				app_name.append (i)
			for i in app_name:
				test = re.match(r"com.tcl.*|com.tct.*|com.jrd.*|com.alcatel.*",i)
				if test:
					tcl_pack.append(i)
			return app_name,tcl_pack
	def get_dut_package(self):
		message_to_connect = QMessageBox.about(self,"获取包名","请连接测试机后点击OK")
		app_name=self.get_dut_package_f()
		if app_name:
			app_name[0].sort()
		other_name=["com.android.settings" , "com.android.phone" , "com.android.systemui","com.android.deskclock",
					"com.android.bluetooth","com.android.camera","com.tcl.library"]
		#local_pack = self.local_package_preload ()
		if app_name:
			self.listWidget_all.clear()
			self.listWidget_local.clear()
			for i in app_name[0]:
				if i in app_name[1]:
					if i == "com.tct.contacts.transfer":
						self.listWidget_local.addItem("com.tct.contacts")
					elif i == "com.tcl.fmradio":
						self.listWidget_local.addItem("com.tct.fmradio")
					self.listWidget_local.addItem (i)
				elif i in other_name:
					self.listWidget_local.addItem(i)
				else:
					self.listWidget_all.addItem(i)
			self.label_all_package.setText ("待选择%s项" % str (self.listWidget_all.count ()))
			self.label_local_package.setText ("已选择%s项" % str (self.listWidget_local.count ()))
		self.btn_getpackage.setText("重新获取包名")


	def get_dir(self):
		log_dir = QFileDialog.getExistingDirectory (self, "Choose Dir", "./")
		self.lineEdit.setText (log_dir)
		return log_dir

	def start_analysis(self):
		self.progressBar.setValue(0)
		self.btn_analysis.setEnabled(False)
		file_dir.append(self.lineEdit.text())
		count_local_list=[]
		count_local = self.listWidget_local.count()
		for i in range(count_local):
			count_local_list.append(self.listWidget_local.item(i).text())
		count_local_list=list(set(count_local_list))
		if count_local_list:
			count_local_list.sort()
		app_local_name.append(count_local_list)
		self.progressBar.setValue(10)
		self.thread.start()
		self.btn_analysis.setEnabled (True)

	def process_bar(self,int_value):
		self.progressBar.setValue(int_value)
	def listWidget_add_to_local(self):
		item = self.listWidget_all.currentItem().text()
		item_row = self.listWidget_all.currentRow()
		self.listWidget_all.takeItem(item_row)
		self.listWidget_local.addItem(item)
		self.label_all_package.setText ("待选择%s项" % str (self.listWidget_all.count ()))
		self.label_local_package.setText ("已选择%s项" % str (self.listWidget_local.count ()))

	def listWidget_back_to_all(self):
		item = self.listWidget_local.currentItem().text()
		item_row = self.listWidget_local.currentRow()
		self.listWidget_local.takeItem(item_row)
		self.listWidget_all.addItem(item)
		self.label_all_package.setText ("待选择%s项" % str (self.listWidget_all.count ()))
		self.label_local_package.setText ("已选择%s项" % str (self.listWidget_local.count ()))

	def local_package_preload(self):
		dut_pack = ['com.android.settings', 'com.tcl.camera','com.tct.contacts','com.tct.dialer', 'com.tct.soundrecorder',
					'com.alcatel.mcrm','com.jrdcom.filemanager','com.tcl.fmradio','com.tcl.live','com.tcl.usercare','com.tclhz.gallery'
					, 'com.tct.calculator', 'com.tct.onetouchbooster', 'com.tct.video', 'com.tct.weather','com.android.deskclock'
					,"com.tct.contacts.transfer",'com.tcl.usercare',"com.tct.fmradio"]
		return dut_pack

	def listWidget_add_item(self):
		text , ok = QInputDialog.getText(self,"新增加包名","输入包名：")
		if ok and text:
			self.listWidget_all.addItem(text)
			self.label_all_package.setText ("待选择%s项" % str (self.listWidget_all.count ()))

	def listWidget_local_delete(self):
		item_row = self.listWidget_local.currentRow ()
		self.listWidget_local.takeItem (item_row)
		self.label_local_package.setText ("已选择%s项" % str (self.listWidget_local.count ()))

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = main_MainWindow()
	window.show()
	sys.exit(app.exec_())