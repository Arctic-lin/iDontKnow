import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QDialog,QFileDialog,QMessageBox
from monitor import Ui_MainWindow
import subprocess
import re
import time


class parent_MainWindow(QMainWindow,Ui_MainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.main_ui=Ui_MainWindow()
		self.setupUi(self)
	def getdut_sn(self):
		devices_info = subprocess.check_output ("adb devices", encoding="utf-8")
		dut_sn = re.findall ("\n" + "(.*?)" + r"\tdevice", devices_info)
		return dut_sn
	def get_dut_sn(self):
		dut_sn=self.getdut_sn()
		text_dut_sn = ";".join(dut_sn)
		self.textEdit.setText(text_dut_sn)

	def start_monitor_function(self):
		dut_sn = self.getdut_sn()
		log_save_dir = self.textEdit_2.toPlainText()
		dumpsys_info = r"shell dumpsys -t 100 meminfo"
		cat_mem_info = r"shell cat /proc/meminfo"
		cat_slab_info = r"shell cat /proc/slabinfo"
		if self.checkBox_3.isChecked () == True:
			cat_slab_info_false_signal = []
			for i in dut_sn:
				cat_slab_info_out = subprocess.getstatusoutput (r"adb -s %s %s" % (i, cat_slab_info))
				if cat_slab_info_out[0] == 1:
					cat_slab_info_false_signal.append (i)
			if cat_slab_info_false_signal:
				str_cat_slab_info_false_signal = " and ".join (cat_slab_info_false_signal)
				QMessageBox.warning (self, "Warning", "%s 不支持抓取此Log,\n错误信息:\n%s" % (str_cat_slab_info_false_signal,
																					cat_slab_info_out[1]))
			else:
				for i in dut_sn:
					print(r"%s :cat /proc/slabinfo...."%i)
					cat_slab_info_out_1 = subprocess.check_output (r"adb -s %s %s" % (i, cat_slab_info),
																   encoding="utf-8")
					with open (log_save_dir + "//" + i + "_slabinfo.txt", "a") as f:
						localtime = time.asctime (time.localtime (time.time ()))
						f.writelines (localtime + "\n")
						f.writelines (cat_slab_info_out_1 + "\n")
					print("Finished")

		if self.checkBox.isChecked() == True:
			for i in dut_sn:
				print ("%s :dumpsys meminfo...." % i)
				dumpsys_out=subprocess.check_output(r"adb -s %s %s"%(i,dumpsys_info),encoding="utf-8")
				with open(log_save_dir+"//"+i+"_meminfo.txt","a") as f:
					localtime=time.asctime(time.localtime(time.time()))
					f.writelines(localtime+"\n")
					f.writelines(dumpsys_out+"\n")
				print("Finished")
		if self.checkBox_2.isChecked() == True:
			for i in dut_sn:
				print (r"%s :cat /proc/meminfo...." % i)
				cat_mem_out=subprocess.check_output(r"adb -s %s %s"%(i,cat_mem_info),encoding="utf-8")
				with open(log_save_dir+"//"+i+"_catmem.txt","a") as f:
					localtime=time.asctime(time.localtime(time.time()))
					f.writelines(localtime+"\n")
					f.writelines(cat_mem_out+"\n")
				print("Finisded")

	def start_monitor(self):
		test_time=1
		self.pushButton_3.setEnabled(False)
		QApplication.processEvents()
		if self.radioButton.isChecked() == True:
			set_time_clock=300
		elif self.radioButton_2.isChecked() == True:
			set_time_clock=3600
		while True:
			print("记录次数:"+" "+str(test_time))
			self.start_monitor_function()
			print("\n\nWait %d second"%set_time_clock)
			test_time = test_time + 1
			time.sleep(set_time_clock)

	def stop_monitor(self):
		pass
	def save_file(self):
		log_dir = QFileDialog.getExistingDirectory(self,"Choose Dir","./")
		self.textEdit_2.setText(log_dir)
		return log_dir
	def help_contact(self):
		QMessageBox.information(self,"Information","如需监控其他信息,可联系本人进行添加。\nLync:Yongjie.lin",
							   QMessageBox.Yes)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = parent_MainWindow()
	window.show()
	sys.exit(app.exec_())