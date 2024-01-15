from __future__ import print_function

import os
import sys

import socket

import os.path

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import uic
from PyQt6.QtGui import QPixmap
import hashlib



import mysql.connector
from mysql.connector import errorcode



import mainui
from mainui import Ui_MainWindow





class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        
        
        self.pixmap = QPixmap('code.png')
        self.vscode.setPixmap(self.pixmap)
        self.vscode.resize(self.pixmap.width(),
                          self.pixmap.height())





        self.login_Button.clicked.connect(self.login_func)
       # self.login2()










    def login2(self):
        cnx = mysql.connector.connect(user='test', password='test!',
                              host='bananapim2ultra.fritz.box',
                              database='userdb')
        
        username = self.username_Input.text()
        password = self.password_Input.text()
        
        # Fetch one record and return the result
        account = cursor.fetchone()
        
        cursor = cnx.cursor()
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password,))



        cursor.close()

    
        cnx.close()




    def login_func(self):
        connection = mysql.connector.connect(
     host='bananapim2ultra.fritz.box',
     user='test',
     password='test',
     port='3306',
     database='userdb'
)

        c = connection.cursor()
        username = self.username_Input.text()
        password = self.password_Input.text()
        username1, password1 = username, hashlib.sha256(password.encode()).hexdigest()
        select_query = 'SELECT * FROM `accounts` WHERE `username` = %s and password = %s'
        vals = (username1, password1,)
        c.execute(select_query, vals)
       # print(c.fetchall())
        user = c.fetchone()
        if user is not None:
            print("xes")
        else:
            print("no")





    def login(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(("localhost", 9998))
        username = self.username_Input.text()
        password = self.password_Input.text()

        message = client.recv(1024).decode()
        client.send(username.encode())
        message = client.recv(1024).decode()
        client.send(password.encode())

        print(client.recv(1024).decode())










if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()
    app.exec()