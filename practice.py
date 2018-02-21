# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'practice.ui'
#
# Created: Mon Sep 25 12:07:40 2017
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import pymysql.cursors

# switch on QString in Python3

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

class Ui_Dialog(object):
    def addTable(self):
        connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='booking',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        try:
            with connection.cursor() as cursor:
                sql = "SELECT ID,NAME,AVAILABLE_ROOMS,RATE,LOCATION FROM HOTELS"
                cursor.execute(sql)
                result = cursor.fetchall()
                self.tableWidget.setRowCount(0)
                
                self.tableWidget.setHorizontalHeaderLabels(("Id;Hotel Name;Available;Price;City").split(";"))
                #self.tableWidget.setVerticleHeaderLabels((";;").split(";"))
                print(result)
                for row_number, row_data in enumerate(result):
                    print(row_data)
                    self.tableWidget.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.tableWidget.setItem(row_number, column_number, QtGui.QTableWidgetItem(str(row_data[data])))               
        finally:
            connection.close()

    def cellClick(self,row,col):
        print(self.tableWidget.item(self.tableWidget.currentRow(),col).text())
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(883, 589)
        self.tableWidget = QtGui.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(10, 160, 705, 325))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMaximumSize(QtCore.QSize(705, 300))
        self.tableWidget.setBaseSize(QtCore.QSize(705, 300))
        self.tableWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tableWidget.setMouseTracking(True)
        self.tableWidget.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tableWidget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
#####################
        self.addTable();
        self.tableWidget.cellClicked.connect(self.cellClick)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)




    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

