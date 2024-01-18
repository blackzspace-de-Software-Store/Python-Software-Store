#/usr/bin/env python3
# software-store.py

# Author: BlackLeakz
# Version: 0.0.0.1 (alpha)
# Website: https://blackzspace.de/software-store
# Github: https://github.com/blackzspace-de-Software-Store



from __future__ import print_function

import os
import os.path
import subprocess
import sys

import logging
import platform as pl
import json

import time
import datetime

import treq
import certifi
#import cgi

import requests
import posixpath
import urllib.parse


# tmp
import tqdm


from time import sleep
from datetime import datetime
from pathlib import Path
from urllib.request import urlopen


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import uic
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QCoreApplication
from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt6.QtWidgets import QProgressBar, QFileDialog


import mainui
from mainui import Ui_MainWindow

curr_dir = os.cwd()


imgs_path = "./.data/.imgs"
log_path = "./.data/.logs/software-store.logs"
cfg_path = "./.data/.configs/config.json"
download_path = curr_dir + "/downloads"
version_file_new = ".data/.tmp/version.json"
download_urls = ".data/.configs/download_urls.json"


sysx = pl.system()
mach = pl.machine()


logging.basicConfig(filemode="w", filename=log_path, level="DEBUG")

strf_time = datetime.now()






with open(cfg_path, "r") as f:
    data = f.read()
    

config = json.loads(data)


update_url = config['update-url']
version = config['version']
update_server = config['update-server']






with open(download_urls, "r") as f:
    xdata = f.read()
    

dlurls = json.loads(xdata)


code_win = dlurls['vscode-win']
code_linux = dlurls['vscode-linux']
code_mac = dlurls['vscode-mac']


pycharm_win = dlurls['pycharm-win']
pycharm_linux = dlurls['pycharm-linux']
pycharm_mac = dlurls['pycharm-mac']

intellij_win = dlurls['intellij-win']
intellij_linux = dlurls['intellij-linux']
intellij_mac = dlurls['intellij-mac']

arduino_win = dlurls['arduino-win']
arduino_linux = dlurls['arduino-linux']
arduino_mac = dlurls['arduino-mac']

android_win = dlurls['android-studio-win']
android_linux = dlurls['android-studio-linux']
android_mac = dlurls['android-studio-mac']

qtcreator_win = dlurls['qt-creator-win']
qtcreator_linux = dlurls['qt-creator-linux']
qtcreator_mac = dlurls['qt-creator-mac']




class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        
        
        # Settings
        self.setDownloadPath_Button.clicked.connect(self.setDLPath)
        self.download_Path.setText(download_path)
        
        ## Check Update
        self.VERSION.setText(version)
        self.check_Button.clicked.connect(self.check_update)
        self.update_Button.clicked.connect(self.update)
        
        
        
        
        # Store Installer
        self.vscode_Install.clicked.connect(self.vscode_install)
        
        self.pycharm_Install.clicked.connect(self.pycharm_install)
        
        self.intellij_Install.clicked.connect(self.intellij_install)
        
        self.androidstudio_Install.clicked.connect(self.android_install)
        
        self.qtcreator_Install.clicked.connect(self.qtcreator_install)
        
        self.arduino_Install.clicked.connect(self.arduino_install)
        
        
        
        
        
        
        
        
        
########################################  SETTINGS SETTINGS ###############################################################################

        
        
    def setDLPath(self):
        dir_name = QFileDialog.getExistingDirectory(self, "Select a Directory")
        if dir_name:
            path = Path(dir_name)
            self.download_Path.setText(str(path))
            
            
            
            
    def check_update(self):
        if os.path.isfile(version_file_new):
            os.remove(version_file_new)
        self.downloader = Downloader(URL=update_server)
        time.sleep(1.5)
        
        
        with open(version_file_new, "r") as f:
                ver = f.read()
        latest_version = json.loads(ver)
        latest_version = latest_version['version']
        self.VERSION_LATEST.setText(latest_version)
        return latest_version
        
    
    def update(self, latest_version):
        if int(version) > int(latest_version):
            self.initDownload(URL=update_url)
     
            
            
            
            
        
            
            
        
        
########################################  STORE STORE STORE #######(SOON BACKEND-HANDLED)#########################
    def vscode_install(self):
        if sysx == "Windows":
            self.initDownload(URL=code_win)
    
        if sysx == "Linux":
            self.initDownload(URL=code_linux)
            
        if sysx == "Mac":
            self.initDownload(URL=code_mac)
       
        else:
            logging.debug("OS NOT SUPPORTED!!! RUNNING: " + sysx)
            
       
        
    def pycharm_install(self):
        if sysx == "Windows":
            self.initDownload(URL=pycharm_win)
    
        if sysx == "Linux":
            self.initDownload(URL=pycharm_linux)
            
        if sysx == "Mac":
            self.initDownload(URL=pycharm_mac)
       
        else:
            logging.debug("OS NOT SUPPORTED!!! RUNNING: " + sysx)
        
        
        
    def intellij_install(self):
        if sysx == "Windows":
            self.initDownload(URL=intellij_win)
    
        if sysx == "Linux":
            self.initDownload(URL=intellij_linux)
            
        if sysx == "Mac":
            self.initDownload(URL=intellij_mac)
       
        else:
            logging.debug("OS NOT SUPPORTED!!! RUNNING: " + sysx)
        
        
        
        
    def arduino_install(self):
        if sysx == "Windows":
            self.initDownload(URL=arduino_win)
    
        if sysx == "Linux":
            self.initDownload(URL=arduino_linux)
            
        if sysx == "Mac":
            self.initDownload(URL=arduino_mac)
       
        else:
            logging.debug("OS NOT SUPPORTED!!! RUNNING: " + sysx)
        
        
        
    def android_install(self):
        if sysx == "Windows":
            self.initDownload(URL=android_win)
    
        if sysx == "Linux":
            self.initDownload(URL=android_linux)
            
        if sysx == "Mac":
            self.initDownload(URL=android_mac)
       
        else:
            logging.debug("OS NOT SUPPORTED!!! RUNNING: " + sysx)
        
        
        
    def qtcreator_install(self):
        if sysx == "Windows":
            self.initDownload(URL=qtcreator_win)
    
        if sysx == "Linux":
            self.initDownload(URL=qtcreator_linux)
            
        if sysx == "Mac":
            self.initDownload(URL=qtcreator_mac)
       
        else:
            logging.debug("OS NOT SUPPORTED!!! RUNNING: " + sysx)
          
        
        
        
########################################  STORE STORE STORE ###############################################################################

        

        
        
    
        
        
        
        
    def initDownload(self, URL):
        self.url = URL
        path = urllib.parse.urlsplit(self.url).path
        filenamex = posixpath.basename(path)
        self.downloader = Downloader(
            self.url,
            filenamex
        )
        self.downloader.setTotalProgress.connect(self.progressBar.setMaximum)
        self.downloader.setCurrentProgress.connect(self.progressBar.setValue)
        self.downloader.succeeded.connect(self.downloadSucceeded)
        self.downloader.finished.connect(self.downloadFinished)
        self.downloader.start()

    def downloadSucceeded(self):
        self.progressBar.setValue(self.progressBar.maximum())

    def downloadFinished(self):
        self.progressBar.setValue(0)
        del self.downloader
   
    
    
    

    
    
class Downloader(QThread):
    setTotalProgress = pyqtSignal(int)
    setCurrentProgress = pyqtSignal(int)
    succeeded = pyqtSignal()

    def __init__(self, url, filename):
        super().__init__()
        self._url = url
        self._filename = filename
        

    def run(self):
        url = self._url
        filename = self._filename
        readBytes = 0
        chunkSize = 1024
        
        if filename == "version.json":
            pathx = ".data/.tmp/"
        else:
            pathx = self.download_Path.text()
            
        with urlopen(url) as r:
            self.setTotalProgress.emit(int(r.info()["Content-Length"]))
            with open(pathx + filename, "ab") as f:
                while True:
                    chunk = r.read(chunkSize)
                    if chunk is None:
                        continue
                    elif chunk == b"":
                        break
                  
                    f.write(chunk)
                    readBytes += chunkSize
                    self.setCurrentProgress.emit(readBytes)
        self.succeeded.emit()


        
    
                        
                        



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()