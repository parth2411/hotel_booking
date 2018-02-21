# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created: Fri Sep 22 14:35:33 2017
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from Homepage import Ui_MainWindow
from Signup import Ui_Signup
import pymysql.cursors

#import sqlite3
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Login(object):
    def showMessageBox(self,title,message):
        msgBox = QtGui.QMessageBox()
        msgBox.setIcon(QtGui.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
        msgBox.exec_()
    
    def welcomeWindowShow(self):
        self.welcomeWindow = QtGui.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.welcomeWindow)
        self.welcomeWindow.show()
        

    def signUpShow(self):
        self.signUpWindow = QtGui.QDialog()
        self.ui = Ui_Signup()
        self.ui.setupUi(self.signUpWindow)
        self.signUpWindow.show()
        
    def loginCheck(self):
        username = self.username_lineEdit.text()
        password = self.password_lineEdit.text()
        connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='booking',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        try:
            with connection.cursor() as cursor:
                sql = ("SELECT * FROM CUSTOMER WHERE USERNAME = '%s' AND PASSWORD = '%s'" %(username,password))  
                cursor.execute(sql)
                result = cursor.fetchall()
                connection.commit()
                print(" data "+username +" "+ password)
                if( len(result) > 0 and username != "" and password!=""):
                    print("User Found !")
                    self.welcomeWindowShow()
                    id1 = 111;
                    sql = ("UPDATE SESSION SET username = '%s',password='%s' WHERE id = %d" %(username,password,id1))
                    cursor.execute(sql)
                    connection.commit()
                    
                else:
                    self.showMessageBox('Warnning','Invalid User Or Password')
        finally:
            connection.close()
    

        
    def signUpCheck(self):
        self.signUpShow()
        
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setStyleSheet("background-image:url(img11.jpg);background-attachment:cover")
        Dialog.resize(1000, 700)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(380, 300, 75, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label.setStyleSheet("background:none")
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(380, 360, 75, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_2.setStyleSheet("background:none")
        self.username_lineEdit = QtGui.QLineEdit(Dialog)
        self.username_lineEdit.setGeometry(QtCore.QRect(480, 300, 175, 30))
        self.username_lineEdit.setObjectName(_fromUtf8("username_lineEdit"))
######### style ###########        
        self.username_lineEdit.setStyleSheet("background:none")
        self.password_lineEdit = QtGui.QLineEdit(Dialog)
        self.password_lineEdit.setGeometry(QtCore.QRect(480, 360, 175, 30))
        self.password_lineEdit.setObjectName(_fromUtf8("password_lineEdit"))
        self.password_lineEdit.setStyleSheet("background:none")
############## Password ##########
        self.password_lineEdit.setEchoMode(QtGui.QLineEdit.Password)
        
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(380, 170, 281, 111))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_3.setStyleSheet("background:none")
        self.login_btn = QtGui.QPushButton(Dialog)
        self.login_btn.setGeometry(QtCore.QRect(480, 410, 75, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.login_btn.setFont(font)
        self.login_btn.setObjectName(_fromUtf8("login_btn"))
##########        Login click ##########
        self.login_btn.clicked.connect(self.loginCheck)
        self.login_btn.setStyleSheet("color:blue;border-radius:3px")

        
        self.signup_btn = QtGui.QPushButton(Dialog)
        self.signup_btn.setGeometry(QtCore.QRect(580, 410, 75, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.signup_btn.setFont(font)
        self.signup_btn.setObjectName(_fromUtf8("signup_btn"))
############        Signup Click #############
        self.signup_btn.clicked.connect(self.signUpCheck)
        self.signup_btn.setStyleSheet("color:blue;border-radius:3px")
        
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(110, 240, 240, 180))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_4.setStyleSheet("background-image:url(user-group-icon.png);background-attachment:fixed")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "UserName", None))
        self.label_2.setText(_translate("Dialog", "Password", None))
        self.label_3.setText(_translate("Dialog", "Hotel Booking", None))
        self.login_btn.setText(_translate("Dialog", "Login", None))
        self.signup_btn.setText(_translate("Dialog", "Signup", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Login()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

