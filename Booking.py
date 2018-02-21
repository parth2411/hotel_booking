# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Booking.ui'
#
# Created: Sat Sep 30 01:08:01 2017
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

class Ui_Bookig_MainWindow(object):
    def cancelAllBooking(self):

            connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='root',
                                 db='booking',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
            try:
                with connection.cursor() as cursor:
                    count =  self.booking_table.rowCount()
                    print(count)
                    i = 0
                    while i <self.booking_table.rowCount():
                        print(i)
                        id = self.booking_table.item(i,0).text()
                        print(id)
                        hot_id = self.booking_table.item(i,7).text()
                        rooms = self.booking_table.item(i,10).text()        
                        self.booking_table.removeRow(i);                    
                        sql = ("DELETE FROM ROOM_BOOKING WHERE ID=%s" %(id))  
                        cursor.execute(sql)
                        connection.commit()
                        sql = ("SELECT * FROM HOTELS WHERE ID = '%s' "%(hot_id))
                        cursor.execute(sql)
                        result = cursor.fetchall()
                        for row_number, row_data in enumerate(result):
                            for column_number, data in enumerate(row_data):
                                if(data=='available_rooms'):
                                    available_rooms = int(row_data[data])
                                elif(data=='booked_rooms'):
                                    booked_rooms = row_data[data]
                        available_rooms = int(available_rooms) + int(rooms);
                        booked_rooms = int(booked_rooms) - int(rooms);
                        sql = ("UPDATE HOTELS SET AVAILABLE_ROOMS = '%s',BOOKED_ROOMS='%s' WHERE id = %s" %(available_rooms,booked_rooms,hot_id))
                        cursor.execute(sql)
                        connection.commit()
                    
            finally:
                connection.close()
        
    def cancelBooking(self):
        count =  self.booking_table.rowCount()
        print(count)
        print(self.booking_table.item(0,0).text() )
        id = self.booking_table.item(self.booking_table.currentRow(),0).text() 
        hot_id = self.booking_table.item(self.booking_table.currentRow(),7).text()
        rooms = self.booking_table.item(self.booking_table.currentRow(),10).text()        
        self.booking_table.removeRow(self.booking_table.currentRow());
        connection = pymysql.connect(host='localhost',
                            user='root',
                            password='root',
                            db='booking',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
        try:
            with connection.cursor() as cursor:
                sql = ("DELETE FROM ROOM_BOOKING WHERE ID=%s" %(id))  
                cursor.execute(sql)
                connection.commit()
                sql = ("SELECT * FROM HOTELS WHERE ID = '%s' "%(hot_id))
                cursor.execute(sql)
                result = cursor.fetchall()
                for row_number, row_data in enumerate(result):
                    for column_number, data in enumerate(row_data):
                        if(data=='available_rooms'):
                            available_rooms = int(row_data[data])
                        elif(data=='booked_rooms'):
                            booked_rooms = row_data[data]
                available_rooms = int(available_rooms) + int(rooms);
                booked_rooms = int(booked_rooms) - int(rooms);
                sql = ("UPDATE HOTELS SET AVAILABLE_ROOMS = '%s',BOOKED_ROOMS='%s' WHERE id = %s" %(available_rooms,booked_rooms,hot_id))
                cursor.execute(sql)
                connection.commit()                
        finally:
            connection.close()
            
        
    def bookedRooms(self):
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
                        if(data=='username'):
                            username = row_data[data]
                        elif(data=='password'):
                            password = row_data[data]
                sql = ("SELECT id FROM CUSTOMER WHERE USERNAME = '%s' AND PASSWORD = '%s'"%(username,password))
                cursor.execute(sql)
                result = cursor.fetchall()
                for row_number, row_data in enumerate(result):
                    for column_number, data in enumerate(row_data):
                        if(data=='id'):
                            custid = int(row_data[data])

                sql = ("SELECT * FROM room_booking WHERE cust_id=%d" %(custid))  
                cursor.execute(sql)
                result = cursor.fetchall()
                self.booking_table.setRowCount(0)            
                self.booking_table.setHorizontalHeaderLabels(("Id;First Name;Last Name;Email;Mob No;Check In;Check Out;Hotel_id;Hotel Name;Hotel City;Rooms;Room Type;Rate;Total").split(";"))
                for row_number, row_data in enumerate(result):
                    self.booking_table.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        if(data=='id'):
                            self.booking_table.setItem(row_number,0, QtGui.QTableWidgetItem(str(row_data[data])))
                        elif(data=='fname'):
                            self.booking_table.setItem(row_number,1, QtGui.QTableWidgetItem(str(row_data[data])))
                        elif(data=='lname'):
                            self.booking_table.setItem(row_number,2, QtGui.QTableWidgetItem(str(row_data[data])))
                        elif(data=='email'):
                            self.booking_table.setItem(row_number,3, QtGui.QTableWidgetItem(str(row_data[data])))
                        elif(data=='mobno'):
                            self.booking_table.setItem(row_number,4, QtGui.QTableWidgetItem(str(row_data[data])))
                        elif(data=='checkIn'):
                            self.booking_table.setItem(row_number,5, QtGui.QTableWidgetItem(str(row_data[data])))
                        elif(data=='checkOut'):
                            self.booking_table.setItem(row_number,6, QtGui.QTableWidgetItem(str(row_data[data])))
                        elif(data=='hotel_id'):
                            self.booking_table.setItem(row_number,7, QtGui.QTableWidgetItem(str(row_data[data])))
                        elif(data=='hotel_name'):
                            self.booking_table.setItem(row_number,8, QtGui.QTableWidgetItem(str(row_data[data])))
                        elif(data=='hotel_city'):
                            self.booking_table.setItem(row_number,9, QtGui.QTableWidgetItem(str(row_data[data])))
                        elif(data=='rooms'):
                            self.booking_table.setItem(row_number,10, QtGui.QTableWidgetItem(str(row_data[data])))
                        elif(data=='room_type'):
                            self.booking_table.setItem(row_number,11, QtGui.QTableWidgetItem(str(row_data[data])))
                        elif(data=='rate'):
                            self.booking_table.setItem(row_number,12, QtGui.QTableWidgetItem(str(row_data[data])))
                        elif(data=='total'):
                            self.booking_table.setItem(row_number,13, QtGui.QTableWidgetItem(str(row_data[data])))

        finally:
            connection.close()
    
    def setupUi(self, Bookig_MainWindow):
        Bookig_MainWindow.setObjectName(_fromUtf8("Bookig_MainWindow"))
        Bookig_MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(Bookig_MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.booking_table = QtGui.QTableWidget(self.centralwidget)
        self.booking_table.setGeometry(QtCore.QRect(55, 250, 1242, 251))
        self.booking_table.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.booking_table.setMouseTracking(True)
        self.booking_table.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.booking_table.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.booking_table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.booking_table.setProperty("showDropIndicator", False)
        self.booking_table.setDragDropOverwriteMode(False)
        self.booking_table.setAlternatingRowColors(True)
        self.booking_table.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.booking_table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)       
        self.booking_table.setColumnCount(14)
        self.booking_table.setObjectName(_fromUtf8("booking_table"))
        self.booking_table.setColumnHidden(7,True)
        self.booking_table.setColumnHidden(0,True)
        self.booking_table.setRowCount(0)
        self.logout_btn = QtGui.QPushButton(self.centralwidget)
        self.logout_btn.setGeometry(QtCore.QRect(680, 100, 91, 31))
        self.logout_btn.setObjectName(_fromUtf8("logout_btn"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1400, 131))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        #self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        #self.label.setStyleSheet("background:blue;color:white")
        self.label.setStyleSheet("background-image:url(images.jpg);background-size:cover;color:white;text-align:left;padding-left:500px;;")

        self.search_btn = QtGui.QPushButton(self.centralwidget)
        self.search_btn.setGeometry(QtCore.QRect(1190, 210, 101, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.search_btn.setFont(font)
        self.search_btn.setObjectName(_fromUtf8("search_btn"))
        self.search_btn.setStyleSheet("border-radius:3px;background:#4CAF50;color:white")

        self.search_btn.clicked.connect(self.cancelAllBooking)
        
        self.bookedlist_btn = QtGui.QPushButton(self.centralwidget)
        self.bookedlist_btn.setGeometry(QtCore.QRect(1190, 135, 101, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bookedlist_btn.setFont(font)
        self.bookedlist_btn.setObjectName(_fromUtf8("bookedlist_btn"))
        self.bookedlist_btn.setStyleSheet("border-radius:3px;background:#4CAF50;color:white")
        self.bookedlist_btn.clicked.connect(self.cancelBooking)

        
        Bookig_MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(Bookig_MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Bookig_MainWindow.setStatusBar(self.statusbar)
        self.bookedRooms()
        self.retranslateUi(Bookig_MainWindow)
        QtCore.QMetaObject.connectSlotsByName(Bookig_MainWindow)

    def retranslateUi(self, Bookig_MainWindow):
        Bookig_MainWindow.setWindowTitle(_translate("Bookig_MainWindow", "MainWindow", None))
        Bookig_MainWindow.setStyleSheet("background-image:url(img11.jpg);background-attachment:cover")
        self.logout_btn.setText(_translate("Bookig_MainWindow", "PushButton", None))
        self.bookedlist_btn.setText(_translate("MainWindow", "Cancel", None))
        self.search_btn.setText(_translate("MainWindow", "Cancel All", None))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Bookig_MainWindow = QtGui.QMainWindow()
    ui = Ui_Bookig_MainWindow()
    ui.setupUi(Bookig_MainWindow)
    Bookig_MainWindow.show()
    sys.exit(app.exec_())

