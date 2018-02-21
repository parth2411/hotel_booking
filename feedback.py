# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Feedback.ui'
#
# Created: Sun Oct  1 22:28:15 2017
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
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

class Ui_Feedback(object):
    def submitFeedback(self):
        connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='booking',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        
        try:
            with connection.cursor() as cursor:
                sql = ("SELECT * FROM SESSION WHERE ID = %d"%(111))
                cursor.execute(sql)
                result = cursor.fetchall()
                for row_number, row_data in enumerate(result):
                    for column_number, data in enumerate(row_data):
                        if(data=='hotel_id'):
                            hotel_id = row_data[data]
                mytext = self.comment_textEdit.toPlainText()
                rating = self.spinBox.value()
                sql = ("INSERT INTO feedback (hotel_id,comment,rating) VALUES (%s,%s,%s)")
                cursor.execute(sql,(hotel_id,mytext,rating))
                connection.commit()
                sql = ("SELECT AVG(rating) as rat FROM feedback where hotel_id=%s"%(hotel_id))
                cursor.execute(sql)
                result = cursor.fetchall()
                for row_number, row_data in enumerate(result):
                    for column_number, data in enumerate(row_data):
                        if(data=='rat'):
                            rating = row_data[data]
                print(rating)
                sql = ("UPDATE HOTELS SET rating = '%s' WHERE id = %d" %(rating,hotel_id))
                cursor.execute(sql)
                connection.commit()
                
        finally:
            connection.close()
            
            
    def setupUi(self, Feedback):
        Feedback.setObjectName(_fromUtf8("Feedback"))
        Feedback.resize(486, 352)
        self.groupBox = QtGui.QGroupBox(Feedback)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 431, 311))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.comment_textEdit = QtGui.QTextEdit(self.groupBox)
        self.comment_textEdit.setGeometry(QtCore.QRect(70, 70, 281, 81))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.comment_textEdit.setFont(font)
        self.comment_textEdit.setObjectName(_fromUtf8("comment_textEdit"))
        self.spinBox = QtGui.QSpinBox(self.groupBox)
        self.spinBox.setGeometry(QtCore.QRect(250, 180, 51, 31))
        self.spinBox.setMaximum(10)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(70, 180, 121, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(70, 40, 201, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.submit_btn = QtGui.QPushButton(self.groupBox)
        self.submit_btn.setGeometry(QtCore.QRect(140, 230, 91, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.submit_btn.setFont(font)
        self.submit_btn.setObjectName(_fromUtf8("submit_btn"))
        self.submit_btn.clicked.connect(self.submitFeedback)
        self.retranslateUi(Feedback)
        QtCore.QMetaObject.connectSlotsByName(Feedback)
        
        
    def retranslateUi(self, Feedback):
        Feedback.setWindowTitle(_translate("Feedback", "Dialog", None))
        self.groupBox.setTitle(_translate("Feedback", "Feedback Form", None))
        self.label.setText(_translate("Feedback", "Rating UpTo 10", None))
        self.label_2.setText(_translate("Feedback", "Comment", None))
        self.submit_btn.setText(_translate("Feedback", "Submit", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
#    global Feedback
    Feedback = QtGui.QDialog()
    ui = Ui_Feedback()
    ui.setupUi(Feedback)
    Feedback.show()
    sys.exit(app.exec_())

