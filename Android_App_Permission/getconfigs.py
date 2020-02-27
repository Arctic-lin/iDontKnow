# -*- coding: UTF-8 -*-

import sys
import os
from configparser import ConfigParser
import frozen_dir

class GetConfigs (object):
	"""Get a option value from a given section."""

	def __init__(self):
		self.commonconfig = ConfigParser ()
		# self.config_file = os.path.join (
		# 	os.path.join (os.path.dirname (os.path.dirname (os.path.abspath (__file__))), 'MonkeyPermission'), 'config.ini')
		# self.config_file = os.path.join(frozen_dir.app_path(),"config.ini")
		# print("2" + ":"+self.config_file)
		self.config_file = os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])),"config.ini")
		self.commonconfig.read (self.config_file, encoding='utf-8')
		# section = self.commonconfig.
		# self.need_adb = self.commonconfig.get (section, "need_adb").upper ()
		# self.adb_content = self.commonconfig.get (section, "adb_content").upper()
		# self.default_check = self.commonconfig.get(section,"default_check").upper()
		# self.disable_switch = self.commonconfig.get (section, "disable_switch").upper ()
		# self.only_apply = self.commonconfig.get (section, "only_apply").upper ()


	def getint(self, section, option, exc=0):
		"""return an integer value for the named option.
		return exc if no the option.
		"""
		try:
			self.commonconfig.read (self.config_file, encoding='utf-8')
			return (self.commonconfig.get (section, option))
		except:
			return exc

	def getstr(self, section, option, exc=None):
		"""return an string value for the named option."""
		try:
			self.commonconfig.read (self.config_file, encoding='utf-8')
			return self.commonconfig.get (section, option)
		except:
			return exc
	def getallsection(self,exc=None):
		try:
			self.commonconfig.read (self.config_file, encoding='utf-8')
			sections = self.commonconfig.sections()
			return sections
		except:
			return exc

if __name__ == '__main__':
	a= GetConfigs()
	print(a.getstr("Tokyo","default_check"))

