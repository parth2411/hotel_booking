# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Signup.ui'
#
# Created: Fri Sep 22 20:10:10 2017
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
#from Login import Ui_Login
import pymysql.cursors
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

class Ui_Signup(object):
#    def loginShow(self):
#       self.loginWindow = QtGui.QDialog()
#        self.ui = Ui_Login()
#        self.ui.setupUi(self.loginWindow)
#        self.loginWindow.show()
        
    def signUpCheck(self):
        firstname = self.firstname_lineEdit.text()
        lastname = self.lastname_lineEdit.text()
        email = self.email_lineEdit.text()
        mobile = self.mobile_lineEdit.text()
        address = self.address_textEdit.toPlainText()
        username = self.uaername_lineEdit.text()
        password = self.password_lineEdit.text()

        connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='booking',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        try:
            with connection.cursor() as cursor:
                sql = ("INSERT INTO customer (fname,lname,email,mobno,city,username,password) VALUES (%s,%s,%s,%s,%s,%s,%s)")
                
                cursor.execute(sql,(firstname,lastname,email,mobile,address,username,password))
                connection.commit()
        finally:
            connection.close()
    
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(1000, 700)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(310, 110, 361, 81))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(340, 200, 100, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.firstname_lineEdit = QtGui.QLineEdit(Dialog)
        self.firstname_lineEdit.setGeometry(QtCore.QRect(460, 200, 175, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.firstname_lineEdit.setFont(font)
        self.firstname_lineEdit.setObjectName(_fromUtf8("firstname_lineEdit"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(340, 250, 100, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lastname_lineEdit = QtGui.QLineEdit(Dialog)
        self.lastname_lineEdit.setGeometry(QtCore.QRect(460, 250, 175, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.lastname_lineEdit.setFont(font)
        self.lastname_lineEdit.setObjectName(_fromUtf8("lastname_lineEdit"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(340, 300, 100, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.email_lineEdit = QtGui.QLineEdit(Dialog)
        self.email_lineEdit.setGeometry(QtCore.QRect(460, 300, 175, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.email_lineEdit.setFont(font)
        self.email_lineEdit.setObjectName(_fromUtf8("email_lineEdit"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(340, 350, 100, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.mobile_lineEdit = QtGui.QLineEdit(Dialog)
        self.mobile_lineEdit.setGeometry(QtCore.QRect(460, 350, 175, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.mobile_lineEdit.setFont(font)
        self.mobile_lineEdit.setObjectName(_fromUtf8("mobile_lineEdit"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(340, 490, 100, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.uaername_lineEdit = QtGui.QLineEdit(Dialog)
        self.uaername_lineEdit.setGeometry(QtCore.QRect(460, 490, 175, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.uaername_lineEdit.setFont(font)
        self.uaername_lineEdit.setObjectName(_fromUtf8("uaername_lineEdit"))
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(340, 540, 100, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.password_lineEdit = QtGui.QLineEdit(Dialog)
        self.password_lineEdit.setGeometry(QtCore.QRect(460, 540, 175, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.password_lineEdit.setFont(font)
        self.password_lineEdit.setObjectName(_fromUtf8("password_lineEdit"))
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(340, 400, 100, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.address_textEdit = QtGui.QTextEdit(Dialog)
        self.address_textEdit.setGeometry(QtCore.QRect(460, 400, 175, 70))
        self.address_textEdit.setObjectName(_fromUtf8("address_textEdit"))
        self.signup_btn = QtGui.QPushButton(Dialog)
        self.signup_btn.setGeometry(QtCore.QRect(460, 600, 75, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.signup_btn.setFont(font)
        self.signup_btn.setObjectName(_fromUtf8("signup_btn"))
#################
        self.signup_btn.clicked.connect(self.signUpCheck)
        
        self.cancel_btn = QtGui.QPushButton(Dialog)
        self.cancel_btn.setGeometry(QtCore.QRect(560, 600, 75, 30))
#################
        #self.cancel_btn.clicked.connect(self.loginShow)
        
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cancel_btn.setFont(font)
        self.cancel_btn.setObjectName(_fromUtf8("cancel_btn"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "SignUp", None))
        self.label_2.setText(_translate("Dialog", "First Name", None))
        self.label_3.setText(_translate("Dialog", "Last Name", None))
        self.label_4.setText(_translate("Dialog", "Email", None))
        self.label_5.setText(_translate("Dialog", "Mobile No", None))
        self.label_6.setText(_translate("Dialog", "UserName", None))
        self.label_7.setText(_translate("Dialog", "Password", None))
        self.label_8.setText(_translate("Dialog", "Address", None))
        self.signup_btn.setText(_translate("Dialog", "SignUp", None))
        self.cancel_btn.setText(_translate("Dialog", "Cancel", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Signup()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

