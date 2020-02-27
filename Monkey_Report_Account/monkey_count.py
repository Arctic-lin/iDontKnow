# -*- coding: utf-8 -*-
# @Time    : 2020/1/8 15:12
# @Author  : Arctic
# @FileName: monkey_count.py
# @Software: PyCharm
# @Purpose :
import os
import xlrd
import webbrowser
dut_pack = ['com.android.settings', 'com.tcl.camera','com.tct.contacts','com.tct.dialer', 'com.tct.soundrecorder',
			'com.alcatel.mcrm','com.jrdcom.filemanager','com.tcl.fmradio','com.tcl.live','com.tcl.usercare',
			'com.tclhz.gallery','com.tct.calculator', 'com.tct.onetouchbooster', 'com.tct.video', 'com.tct.weather',
			'com.android.deskclock',"com.tct.contacts.transfer",'com.tcl.usercare']
def get_memory_file(file_dir):
	memory_leak_root = []
	for root, dirs, files in os.walk (file_dir):
		for file in files:
			if os.path.splitext (file)[1] == ".xls":
				memory_leak_root.append (os.path.join (root, file))
			# elif os.path.splitext (file)[0] == "mem_leaked":
			# 	memory_leak_root.append (os.path.join (root, file))
	return memory_leak_root

def open_excel(dirs,detail=1):
	dir = get_memory_file (dirs)
	html = dirs+"\\"+"monkey_cout.html"
	w=open(html,"w")
	w.close()
	w=open(html,"a+")
	message = """<html><head></head><body></body></html>"""
	w.write(message)
	for i in dir:
		data = xlrd.open_workbook(i)
		device_sn_row = data.sheet_by_index(0).row(0)
		device_sn = device_sn_row[0].value[-8:]
		message="""<body><h3 title='device_name:'>%s</h5></body>"""%device_sn
		w.write(message)
		for h in range(0,2):
			if h == 1:
				sheet = data.sheet_by_index (h)
				message = """<body><h4 titel='test_type'>Integrtion test--Total_ANR:%s  Total_Crash:%s</h4></body>"""%(
					sheet.row(6)[2].value,sheet.row(7)[2].value)
				w.write (message)
			elif h == 0:
				sheet = data.sheet_by_index (h)
				message = """<body><h4 titel='test_type'>System test--Total_ANR:%s  Total_Crash:%s</h4></body>""" % (
					sheet.row (6)[2].value, sheet.row (7)[2].value)
				w.write(message)
			c_row = sheet.nrows
			for l in range(c_row):
				if sheet.row (6)[2].value != "0":
					if sheet.row (7)[2].value != "0":
						if sheet.row(l)[0].value == "CRASH":
							for j in range(11,l):
								message="""<body><p>ANR-%s-count:%s\n</p></body>"""%(sheet.row(j)[0].value,sheet.row(j)[2].value)
								w.write(message)
							for k in range(l+2,sheet.nrows):
								message = """<body><p>Crash-%s-count:%s\n</p></body>""" % (sheet.row (k)[0].value, sheet.row (k)[3].value)
								w.write (message)
					elif sheet.row (7)[2].value == "0":
						if sheet.row (l)[0].value == "ANR":
							for j in range (11, sheet.nrows):
								message = """<body><p>ANR-%s-count:%s\n</p></body>""" % (
								sheet.row (j)[0].value, sheet.row (j)[2].value)
								w.write (message)
				elif sheet.row (6)[2].value == "0":
					if sheet.row (7)[2].value != "0":
						if sheet.row (l)[0].value == "CRASH":
							for j in range (11, sheet.nrows):
								message = """<body><p>Crash-%s-count:%s\n</p></body>""" % (
								sheet.row (j)[0].value, sheet.row (j)[3].value)
								w.write (message)
		# c_row = sheet.row(6)
		# anr_count = c_row[2].value
		# c_row = sheet.row (7)
		# crash_count = c_row[2].value
		# message = """<body><b>Total ANR:%s\tTotal Crash:%s</b></body>""" % (anr_count,crash_count)
		#w.write (message)
	w.close()
	webbrowser.open(html,new=1)


if __name__ == '__main__':
	dirs = input("Dirs:\n")
	open_excel(dirs)