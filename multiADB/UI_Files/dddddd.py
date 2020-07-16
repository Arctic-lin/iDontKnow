# -*- coding: utf-8 -*-
# @Time    : 2020/7/16 15:24
# @Author  : Arctic
# @FileName: dddddd.py
# @Software: PyCharm
# @Purpose :
import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget,QDialog,QFileDialog,QTableWidgetItem,QMessageBox,QPushButton,QLabel
from PyQt5 import QtWidgets,QtCore
from UI_Files.look import Ui_MainWindow
import sip


class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui = Ui_MainWindow()
        self.setupUi(self)
        self.pushButton.clicked.connect(lambda: self.buttonEvent(self.pushButton))
        self.pushButton_2.clicked.connect(lambda: self.buttonEvent(self.pushButton_2))
        self.radioButton.clicked.connect(lambda: self.radioEvent(self.radioButton))
        self.radioButton.clicked.connect(lambda: self.radioEvent(self.radioButton_2))
        self.pushButton_3.clicked.connect(lambda: self.test())

    def test(self):
        for i in range(self.widget.layout().count()):
            print(self.widget.layout().itemAt(i).widget().setEnabled(False))
    def buttonEvent(self,btn):
        if self.widget.children():
            for i in self.widget.children():
                self.widget.children().remove(i)
                sip.delete(i)
        if btn == self.pushButton:
            layout = QtWidgets.QGridLayout()
            addLable = QtWidgets.QLabel(u"pushbutton1")
            addBtn = QtWidgets.QPushButton(u'pushbutton1')
            layout.addWidget(addLable,1,0)
            layout.addWidget(addBtn,2,0)
            self.widget.setLayout(layout)
        if btn == self.pushButton_2:
            layout = QtWidgets.QGridLayout()
            addLable = QtWidgets.QLabel(u"pushbutton2")
            addBtn = QtWidgets.QPushButton(u'pushbutton2')
            layout.addWidget(addLable, 1, 0)
            layout.addWidget(addBtn, 2, 0)
            self.widget.setLayout(layout)


    def radioEvent(self,btn):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())