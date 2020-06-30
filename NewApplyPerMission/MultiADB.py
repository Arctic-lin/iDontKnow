# -*- coding: utf-8 -*-
# @Time    : 2020/5/27 16:12
# @Author  : Arctic
# @FileName: FOTA_Preset.py
# @Software: PyCharm
# @Purpose :Pre_set fota auto upgrade-downgrade

import subprocess
import os
import re
import datetime
import threading
import time

sdcardDir=r"\sdcard"
upgrade=r"D:\Work\DMFOTA\Thor8\6F3P_6F3Q\update_rkey.zip"
downgrade = r"D:\Work\DMFOTA\Thor8\6F3P_6F3Q\downgrade_rkey.zip"
installpkg = r"D:\Work\DMFOTA\Thor8\6F3O_6F3P\JrdFotaAutotest.apk"
video = r"D:\Work\MemoryTest\Source\Video\Source.mp4"
more_apk = r"D:\Work\MemoryLeak\resource\APK"
thor_monkey_log = r"D:\Work\Monkey\Thro8"
mtbf_resource = r"D:\Work\MTBF\Script\Thor\StabilityResource"

class MyThread(threading.Thread):
    def __init__(self,dev):
        super().__init__()
        self.dev = dev

    #获取多台设备号
    def getDutSN(self):
        devices_info = subprocess.check_output("adb devices", encoding="utf-8")
        dut_sn = re.findall("\n" + "(.*?)" + r"\tdevice", devices_info)
        return dut_sn

    #用于Fota升降机测试
    def fotaTest(self):
        # 设置不灭屏
        print(
            f'线程名称：{threading.current_thread().name} 参数：{self.dev} 开始时间：{time.strftime("%Y-%m-%d %H:%M:%S")}'
        )
        print("Never Sleep--%s" % self.dev)
        subprocess.call("adb -s %s shell settings put system screen_off_timeout 1" % self.dev)

        # 执行静音脚本
        print("Mute Dut")
        for i in range(1, 11):
            print("adb -s %s shell media volume --stream %d --set 0" % (self.dev, i))
            test = subprocess.getstatusoutput("adb -s %s shell media volume --stream %d --set 0" % (self.dev, i))

        # 推送文件
        print("push file upgrade --%s" % self.dev)
        subprocess.call("adb -s %s push %s /sdcard/.downloaded/upgrade.zip" % (self.dev, upgrade), shell=True)
        print("push file downgrade --%s" % self.dev)
        subprocess.call("adb -s %s push %s /sdcard/.downloaded/downgrade.zip" % (self.dev, downgrade), shell=True)

        # 安装文件
        print("Install apk--%s" % self.dev)
        subprocess.call("adb -s %s install -r %s" % (self.dev, installpkg))

        print(
            f'线程名称：{threading.current_thread().name} 参数：{self.dev} 结束时间：{time.strftime("%Y-%m-%d %H:%M:%S")}'
        )

    #Push file
    def pushFile(self):
        print("push file upgrade --%s" % self.dev)
        # subprocess.call("adb -s %s push %s /sdcard/.downloaded/upgrade.zip" % (self.dev, upgrade), shell=True)
        subprocess.call("adb -s %s push %s %s" % (self.dev,mtbf_resource,r"/sdcard/"))

    #安装apk
    def installAPK(self,reName=True):
        filedir = more_apk
        #文件名最后为中文,adb install易报错
        for filename in os.listdir(filedir):
            a = filename.split(".")
            if "apk" in a[-1]:
                #判断文件最后是否为中文,是则在结果加个_rename.
                if u'\u4e00' <= a[0][-1:] <= u'\u9fff':
                    os.rename(os.path.join(filedir, filename),os.path.join(filedir,a[0] + "_rename." + a[-1]))
        #二次遍历
        for filename in os.listdir(filedir):
            a = filename.split(".")
            if "apk" in a[-1]:
                b = os.path.join(filedir, filename)
                print(filename)
                subprocess.check_output("adb install -r %s"%b , encoding= "utf-8")
                if reName:
                    print("Change Name to the first time")
                    if len(a[0]) > 7 :
                        if a[0][-7:] == "_rename":
                            os.rename(os.path.join(filedir, filename), os.path.join(
                                os.path.join(filedir, a[0][0:-7] + "." + a[-1])))
    #Reboot edl
    def rebootEDL(self):
        print("adb -s %s reboot edl" % self.dev)
        os.system("adb -s %s reboot edl" % self.dev)

    def shellCmd(self,cmds):
        print("adb -s %s shell %s" %(self.dev,cmds))
        os.system("adb -s %s shell %s" %(self.dev,cmds))

    #Memory Long_video
    def longVideoEnv(self):
        print("push video file dir:%s"%video)
        subprocess.check_output("adb -s %s push %s /sdcard/"%video)
        print("finished")

    def getFilesTree(self):
        fileTree=[]
        file_dir = subprocess.check_output\
            ("adb -s %s shell ls -1 /sdcard/TCTReport/mobilelog" % (self.dev),encoding="utf-8").split("\n")
        for i in file_dir:
            if i :
                files = subprocess.check_output \
                    ("adb -s %s shell ls -1 /sdcard/TCTReport/mobilelog/%s" % (self.dev,i), encoding="utf-8").split("\n")
                for j in files:
                    if j:
                        fileTree.append("/sdcard/TCTReport/mobilelog/%s/%s"%(i,j))
        return file_dir,fileTree

    #Monkey output log
    def getFeedbackLog(self):
        print("get feedback log")
        monkeyDir = []
        for i in os.listdir(thor_monkey_log):
            i = os.path.join(thor_monkey_log,i)
            monkeyDir.append(i)
        for i in monkeyDir:
            if self.dev in i:
                if not os.path.isdir(i+"\\mobilelog"):
                    os.mkdir(os.path.join(i,"mobilelog"))
                filesTree = self.getFilesTree()
                for j in filesTree[0]:
                    if j:
                        k = os.path.join(i, "mobilelog\\%s" % j)
                        if not os.path.isdir(k):
                            os.mkdir(k)
                        for h in filesTree[1]:
                            if j in h:
                                start_time = datetime.datetime.now()
                                print("adb -s %s pull %s %s"%(self.dev,h,k))
                                subprocess.call("adb -s %s pull %s %s"%(self.dev,h,k))
                                time.sleep(0.03)
                                end_time = datetime.datetime.now()
                                time_cost = end_time - start_time
                                print(str(time_cost).split('.')[0])


    def run(self):
        self.rebootEDL()

def getDevSN():
    devices_info = subprocess.check_output ("adb devices", encoding="utf-8")
    dut_sn = re.findall ("\n" + "(.*?)" + r"\tdevice", devices_info)
    return dut_sn


if __name__ == '__main__':
    print(f'主线程开始时间：{time.strftime("%Y-%m-%d %H:%M:%S")}')
    # for i in range(6):
    #     exec('var{} = "{}"'.format(i,getDevSN()[i]))
    threadpool = []
    for i in getDevSN():
        th = MyThread(i)
        threadpool.append(th)
    for th in threadpool:
        th.start()
    for th in threadpool:
        threading.Thread.join(th)


    # #初始化3个线程，传递不同的参数
    # t1 = MyThread(var0)
    # t2 = MyThread(var1)
    # t3 = MyThread(var2)
    # t4 = MyThread(var3)
    # t5 = MyThread(var4)
    # t6 = MyThread(var5)
    # # 开启三个线程
    # t1.start()
    # t2.start()
    # t3.start()
    # t4.start()
    # t5.start()
    # t6.start()
    #
    # # 等待运行结束
    # t1.join()
    # t2.join()
    # t3.join()
    # t4.join()
    # t5.join()
    # t6.join()


    print(f'主线程结束时间：{time.strftime("%Y-%m-%d %H:%M:%S")}')


