# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Homepage.ui'
#
# Created: Fri Sep 22 13:20:09 2017
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import pymysql.cursors
from Booking import Ui_Bookig_MainWindow
from feedback import Ui_Feedback
import sys
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

class Ui_MainWindow(object):
    def feedbackShow(self):
        self.feedbackWindow = QtGui.QDialog()
        self.ui = Ui_Feedback()
        self.ui.setupUi(self.feedbackWindow)
        self.feedbackWindow.show()
        
    def showMessageBox(self,title,message):
        msgBox = QtGui.QMessageBox()
        msgBox.setIcon(QtGui.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
        msgBox.exec_()

    def welcomeWindowShow(self):
        self.bookingWindow = QtGui.QMainWindow()
        self.ui = Ui_Bookig_MainWindow()
        self.ui.setupUi(self.bookingWindow)
        self.bookingWindow.show()
        
    def sarchHotels(self):
        city = self.city_lineEdit.text()
        rooms = self.rooms_lineEdit.text()
        nights = self.nights_lineEdit.text()
        if(city==""and rooms==""and nights==""):
            self.showMessageBox('Warnning','Please Enter Details correctly')
        else:
            rooms = int(rooms)
            connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='root',
                                 db='booking',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
            try:
                with connection.cursor() as cursor:
                    sql = ("SELECT id,name,available_rooms,rate,location,rating FROM HOTELS WHERE LOCATION = '%s' AND AVAILABLE_ROOMS >= %d ORDER BY RATING DESC" %(city,rooms))  
                    cursor.execute(sql)
                    result = cursor.fetchall()
                    self.tableWidget.setRowCount(0)
                    
                    self.tableWidget.setHorizontalHeaderLabels(("Id;Hotel Name;Available;Price;City;Ratings").split(";"))
                    for row_number, row_data in enumerate(result):
                        self.tableWidget.insertRow(row_number)
                        for column_number, data in enumerate(row_data):
                            if(data=='id'):
                                self.tableWidget.setItem(row_number,0, QtGui.QTableWidgetItem(str(row_data[data])))
                            elif(data=='name'):
                                self.tableWidget.setItem(row_number,1, QtGui.QTableWidgetItem(str(row_data[data])))
                            elif(data=='available_rooms'):
                                self.tableWidget.setItem(row_number,2, QtGui.QTableWidgetItem(str(row_data[data])))
                            elif(data=='rate'):
                                self.tableWidget.setItem(row_number,3, QtGui.QTableWidgetItem(str(row_data[data])))
                            elif(data=='location'):
                                self.tableWidget.setItem(row_number,4, QtGui.QTableWidgetItem(str(row_data[data])))
                            elif(data=='rating'):
                                self.tableWidget.setItem(row_number,5, QtGui.QTableWidgetItem(str(row_data[data])))                                
            finally:
                connection.close()

    def cellClick(self,row,col):
        print(self.tableWidget.item(self.tableWidget.currentRow(),col).text())

    def bookRoom(self):
         id = self.tableWidget.item(self.tableWidget.currentRow(),0).text()       
         name = self.tableWidget.item(self.tableWidget.currentRow(),1).text()       
         available_rooms = self.tableWidget.item(self.tableWidget.currentRow(),2).text()       
         rate = self.tableWidget.item(self.tableWidget.currentRow(),3).text()       
         location = self.tableWidget.item(self.tableWidget.currentRow(),4).text()
         roomtype = str(self.rooms_type.currentIndex())
         checkIn = self.checkin_cal.selectedDate()
         checkOut = self.checkout_cal.selectedDate()
         rooms = int(self.rooms_lineEdit.text())
         nights = int(self.nights_lineEdit.text())
         checkIn = checkIn.toString()
         checkOut = checkOut.toString()
         rooms = int(rooms)
         connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='booking',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
         try:
            with connection.cursor() as cursor:
                 id1 = 111;
                 sql = ("SELECT * FROM SESSION WHERE ID = %d"%(id1))
                 cursor.execute(sql)
                 result = cursor.fetchall()
                 for row_number, row_data in enumerate(result):
                     for column_number, data in enumerate(row_data):
                         if(data=='username'):
                             username = row_data[data]
                         elif(data=='password'):
                             password = row_data[data]
                 sql = ("SELECT * FROM CUSTOMER WHERE USERNAME = '%s' AND PASSWORD = '%s'"%(username,password))
                 cursor.execute(sql)
                 result = cursor.fetchall()
                 for row_number, row_data in enumerate(result):
                     for column_number, data in enumerate(row_data):
                         if(data=='id'):
                             custid = int(row_data[data])
                         elif(data=='fname'):
                             fname = row_data[data]
                         elif(data=='lname'):
                             lname = row_data[data]
                         elif(data=='email'):
                             email = row_data[data]
                         elif(data=='mobno'):
                             mobno = row_data[data]
                         elif(data=='city'):
                             city = row_data[data]
                 guest = 1
                 sql = ("SELECT * FROM HOTELS WHERE ID = '%s' AND NAME = '%s'"%(id,name))
                 cursor.execute(sql)
                 result = cursor.fetchall()
                 for row_number, row_data in enumerate(result):
                     for column_number, data in enumerate(row_data):
                         if(data=='available_rooms'):
                             available_rooms = int(row_data[data])
                         elif(data=='booked_rooms'):
                             booked_rooms = row_data[data]
                 if(available_rooms>=rooms):
                     available_rooms = int(available_rooms)-int(rooms)
                     booked_rooms = int(booked_rooms)+int(rooms)
                     sql = ("UPDATE HOTELS SET AVAILABLE_ROOMS = '%s',BOOKED_ROOMS='%s' WHERE id = %s" %(available_rooms,booked_rooms,id))
                     cursor.execute(sql)
                     connection.commit()
                     sql = ("INSERT INTO room_booking (cust_id,fname,lname,email,mobno,checkIn,checkOut,hotel_id,hotel_name,hotel_city,rooms,room_type,rate,total) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
                     extra = 1;
                     if(int(roomtype)==1):
                         extra=float(rate)*30
                         extra=float(extra)/100
                     elif(int(roomtype)==2):
                         extra=float(rate)*50
                         extra=float(extra)/100
                     total = int(rooms) * float(rate)
                     total = total * nights;
                     total=total+extra;
                     roomtype = str(self.rooms_type.currentText())
                     cursor.execute(sql,(custid,fname,lname,email,mobno,checkIn,checkOut,id,name,location,rooms,roomtype,rate,total))
                     connection.commit()
                     self.showMessageBox('Warnning','Room Booked Successfully!')

                     sql = ("UPDATE SESSION SET HOTEL_ID = '%s' WHERE id= %s" %(id,111))
                     cursor.execute(sql)
                     connection.commit()
                     
                     self.city_lineEdit.setText("")
                     self.nights_lineEdit.setText("")
                     self.rooms_lineEdit.setText("")
                     self.feedbackShow()
                 else:
                    self.showMessageBox('Warnning','Rooms are not available Please Tyr again')                    

         finally:
             connection.close()
         

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1200, 700)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        
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
        self.label.setStyleSheet("background-image:url(images.jpg);color:white;text-align:left;padding-left:500px;;")
        self.checkin_cal = QtGui.QCalendarWidget(self.centralwidget)
        self.checkin_cal.setGeometry(QtCore.QRect(420, 210, 264, 155))
        self.checkin_cal.setObjectName(_fromUtf8("checkin_cal"))
        self.checkin_cal.setStyleSheet("background:none;color:black;")
        
        self.city_lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.city_lineEdit.setGeometry(QtCore.QRect(35, 210, 175, 30))
        self.city_lineEdit.setObjectName(_fromUtf8("city_lineEdit"))
        self.city_lineEdit.setStyleSheet("border-radius:4px")
        self.city_lineEdit.setStyleSheet("background:none")

        self.nights_lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.nights_lineEdit.setGeometry(QtCore.QRect(230, 210, 175, 30))
        self.nights_lineEdit.setObjectName(_fromUtf8("nights_lineEdit"))
        self.nights_lineEdit.setStyleSheet("border-radius:4px")
        self.nights_lineEdit.setStyleSheet("background:none")

        self.checkout_cal = QtGui.QCalendarWidget(self.centralwidget)
        self.checkout_cal.setGeometry(QtCore.QRect(700, 210, 264, 155))
        self.checkout_cal.setObjectName(_fromUtf8("checkout_cal"))
        self.checkout_cal.setStyleSheet("background:none") 
        self.rooms_lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.rooms_lineEdit.setGeometry(QtCore.QRect(980, 210, 175, 30))
        self.rooms_lineEdit.setObjectName(_fromUtf8("rooms_lineEdit"))
        self.rooms_lineEdit.setStyleSheet("border-radius:4px")        
        self.rooms_lineEdit.setStyleSheet("background:none")
        self.search_btn = QtGui.QPushButton(self.centralwidget)
        self.search_btn.setGeometry(QtCore.QRect(1190, 210, 101, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.search_btn.setFont(font)
        self.search_btn.setStyleSheet("border-radius:3px;background-colr:#4CAF50")
        self.search_btn.setObjectName(_fromUtf8("search_btn"))

        ###############
        self.search_btn.clicked.connect(self.sarchHotels)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(35, 170, 175, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_2.setStyleSheet("background:none")

        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(230, 170, 175, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_6.setStyleSheet("background:none")


        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(420, 170, 175, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_3.setStyleSheet("background:none")
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(700, 170, 175, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_4.setStyleSheet("background:none")
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(980, 170, 175, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_5.setStyleSheet("background:none")

        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(400, 380, 600, 250))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMaximumSize(QtCore.QSize(705, 300))
        self.tableWidget.setBaseSize(QtCore.QSize(1100, 600))
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
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
#####################
        
        self.tableWidget.cellClicked.connect(self.cellClick)


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
        self.bookedlist_btn.clicked.connect(self.welcomeWindowShow)
        ###############
        self.search_btn.clicked.connect(self.sarchHotels)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        self.book_btn = QtGui.QPushButton(self.centralwidget)
        self.book_btn.setGeometry(QtCore.QRect(620, 635, 100, 30))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.book_btn.setFont(font)
        self.book_btn.setObjectName(_fromUtf8("book_btn"))
###############
        self.book_btn.clicked.connect(self.bookRoom)
        self.book_btn.setStyleSheet("color:white;border-radius:3px;background:#4CAF50")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
##### DropDown
        self.rooms_type = QtGui.QComboBox(self.centralwidget)
        self.rooms_type.setGeometry(QtCore.QRect(980, 260, 181, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.rooms_type.setFont(font)
        self.rooms_type.setObjectName(_fromUtf8("rooms_type"))
        self.rooms_type.addItem(_fromUtf8(""))
        self.rooms_type.addItem(_fromUtf8(""))
        self.rooms_type.addItem(_fromUtf8(""))


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        MainWindow.setStyleSheet("background-image:url(img11.jpg);background-attachment:cover")
        #self.label.setText(_translate("MainWindow", "Welcome To Hotel Booking", None))       

        self.search_btn.setText(_translate("MainWindow", "Search", None))
        self.bookedlist_btn.setText(_translate("MainWindow", "Bookings", None))
        self.search_btn.setStyleSheet("background-color:#fff")
        self.label_2.setText(_translate("MainWindow", "City", None))
        self.label_6.setText(_translate("MainWindow", "Nights", None))
        self.label_3.setText(_translate("MainWindow", "Check In", None))
        self.label_4.setText(_translate("MainWindow", "Check Out", None))
        self.label_5.setText(_translate("MainWindow", "Rooms", None))
        self.book_btn.setText(_translate("MainWindow", "Book", None))
        self.rooms_type.setItemText(0, _translate("Bookig_MainWindow", "Single Room", None))
        self.rooms_type.setItemText(1, _translate("Bookig_MainWindow", "Double Room", None))
        self.rooms_type.setItemText(2, _translate("Bookig_MainWindow", "Family Rooms", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

