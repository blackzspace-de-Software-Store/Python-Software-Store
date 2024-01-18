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



imgs_path = "./.data/.imgs"
log_path = "./.data/.logs/software-store.logs"
cfg_path = "./.data/.configs/config.json"
download_path = "./downloads"
version_file_new = ".data/.tmp/version.json"


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






class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        
        
        # Settings
        self.setDownloadPath_Button.clicked.connect(self.setDLPath)
        
        
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
        
        
        
        
        
        
        
        
        
########################################  SETTINGS SETTINGS ###############################################################################

        
        
    def setDLPath(self):
        dir_name = QFileDialog.getExistingDirectory(self, "Select a Directory")
        if dir_name:
            path = Path(dir_name)
            self.download_Path.setText(str(path))
            
            
            
            
    def check_update(self):
        if os.path.isfile(".data/.tmp/version.json"):
            os.system("rm -rf .data/.tmp/version.json")
       
        self.downloader = Downloaderx().dlx(urlx=update_server)
        time.sleep(1.5)
        
        
        with open(version_file_new, "r") as f:
                ver = f.read()
        latest_version = json.loads(ver)
        versionx = latest_version['version']
        self.VERSION_LATEST.setText(versionx)
        
    
    def update(self):
        if version < self.versionx:
            self.initDownload(URL="https://blackzspace.de/software-store/update/latest/version.json")
            
            
            
            
        
            
            
        
        
########################################  STORE STORE STORE ###############################################################################
    def vscode_install(self):
        if sysx == "Windows":
            self.initDownload(URL="https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user")
    
        if sysx == "Linux":
            self.initDownload(URL="https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-x64")
        
        else:
            logging.debug("OS NOT SUPPORTED!!! RUNNING: " + sysx)
            
       
        
    def pycharm_install(self):
        if sysx == "Windows":
            self.initDownload(URL="https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=windows&code=PCC")
    
        if sysx == "Linux":
            self.initDownload(URL="https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=linux&code=PCC")
        
        else:
            logging.debug("OS NOT SUPPORTED!!! RUNNING: " + sysx)
        
        
        
    def intellij_install(self):
        if sysx == "Windows":
            self.initDownload(URL="https://www.jetbrains.com/de-de/idea/download/download-thanks.html?platform=windows&code=IIC")
    
        if sysx == "Linux":
            self.initDownload(URL="https://www.jetbrains.com/de-de/idea/download/download-thanks.html?platform=linux&code=IIC")
        
        else:
            logging.debug("OS NOT SUPPORTED!!! RUNNING: " + sysx)
        
        
        
        
    def arduino_install(self):
        if sysx == "Windows":
            self.initDownload(URL="https://downloads.arduino.cc/arduino-ide/arduino-ide_2.2.1_Windows_64bit.msi?_gl=1*1gpjh2h*_ga*MTY0ODM1NTkxNy4xNzA1NTI0OTcz*_ga_NEXN8H46L5*MTcwNTUyNDk3Mi4xLjEuMTcwNTUyNDk3Ny4wLjAuMA..*_fplc*eVpkUzYlMkY1MG93NUNrTGR1Z3FUM09VNDVFdk9Nb21JRlREaVdON1ZZNTFFbDAlMkZvTGQxb3V0ZVRIeGRXMDVQVjBIWEdUNTBUazAxWEQ0T2pMZzBIMW9Mbm1ZdG5JM0ZOOEpIVEUzNlJXTyUyQkN3WjJKYUpucUhZNzhUcGxMdDVRJTNEJTNE")
    
        if sysx == "Linux":
            self.initDownload(URL="https://downloads.arduino.cc/arduino-ide/arduino-ide_2.2.1_Linux_64bit.AppImage?_gl=1*1gpjh2h*_ga*MTY0ODM1NTkxNy4xNzA1NTI0OTcz*_ga_NEXN8H46L5*MTcwNTUyNDk3Mi4xLjEuMTcwNTUyNDk3Ny4wLjAuMA..*_fplc*eVpkUzYlMkY1MG93NUNrTGR1Z3FUM09VNDVFdk9Nb21JRlREaVdON1ZZNTFFbDAlMkZvTGQxb3V0ZVRIeGRXMDVQVjBIWEdUNTBUazAxWEQ0T2pMZzBIMW9Mbm1ZdG5JM0ZOOEpIVEUzNlJXTyUyQkN3WjJKYUpucUhZNzhUcGxMdDVRJTNEJTNE")
        
        else:
            logging.debug("OS NOT SUPPORTED!!! RUNNING: " + sysx)
        
        
        
    def android_install(self):
        if sysx == "Windows":
            self.initDownload(URL="https://redirector.gvt1.com/edgedl/android/studio/install/2023.1.1.27/android-studio-2023.1.1.27-windows.exe")
    
        if sysx == "Linux":
            self.initDownload(URL="https://redirector.gvt1.com/edgedl/android/studio/ide-zips/2023.1.1.27/android-studio-2023.1.1.27-linux.tar.gz")
        
        else:
            logging.debug("OS NOT SUPPORTED!!! RUNNING: " + sysx)
        
        
        
    def qtcreator_install(self):
        if sysx == "Windows":
            self.initDownload(URL="https://download.qt.io/official_releases/qtcreator/12.0/12.0.1/qt-creator-opensource-windows-x86_64-12.0.1.exe?__hstc=45788219.64f02eb7ed6ba237641c1ba3ab97ff53.1689838104787.1689838104787.1689838104787.1&__hssc=45788219.1.1689838104787&__hsfp=783877104")
    
        if sysx == "Linux":
            self.initDownload(URL="https://download.qt.io/official_releases/qtcreator/12.0/12.0.1/qt-creator-opensource-linux-x86_64-12.0.1.run?__hstc=45788219.64f02eb7ed6ba237641c1ba3ab97ff53.1689838104787.1689838104787.1689838104787.1&__hssc=45788219.1.1689838104787&__hsfp=783877104")
        
        else:
            logging.debug("OS NOT SUPPORTED!!! RUNNING: " + sysx)
          
        
        
        
########################################  STORE STORE STORE ###############################################################################

        
        
        
    
            
        
        
        
    def initDL(self, URL):
        path = urllib.parse.urlsplit(URL).path
        filename = posixpath.basename(path)

        self.download(urlx=URL, filenamex=filename)
        
        
        
        
        
    def initDownload(self, URL):
        path = urllib.parse.urlsplit(URL).path
        filename = posixpath.basename(path)

        self.downloader = Downloader(
            url=URL,
            filename=filename
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
    
    
    
 
    
class Downloaderx(QThread):
    setTotalProgress = pyqtSignal(int)
    setCurrentProgress = pyqtSignal(int)
    succeeded = pyqtSignal()
    
    def dlx(self, urlx: str):
        path = urllib.parse.urlsplit(urlx).path
        filenamex = posixpath.basename(path)
        readBytes = 0
        chunkSize = 1024
        if filenamex == "version.json":
            
            pathx = ".data/.tmp/"
          
            
        else:
            pathx = "downloads/"
        with urlopen(urlx) as r:
            self.setTotalProgress.emit(int(r.info()["Content-Length"]))
            with open(pathx + filenamex, "ab") as f:
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
    
    
    
class Downloader(QThread):
    setTotalProgress = pyqtSignal(int)
    setCurrentProgress = pyqtSignal(int)
    succeeded = pyqtSignal()

    def __init__(self, url, filename):
        super().__init__()
        self._url = url
        self._filename = filename

    def run(self):
        url = "https://vscode.download.prss.microsoft.com/dbazure/download/stable/0ee08df0cf4527e40edc9aa28f4b5bd38bbff2b2/code_1.85.1-1702462158_amd64.deb"
        filename = "vscode.deb"
        readBytes = 0
        chunkSize = 1024
        with urlopen(url) as r:
            self.setTotalProgress.emit(int(r.info()["Content-Length"]))
            with open(filename, "ab") as f:
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