# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'laptops.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

 
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_Laptop_window(object):
  
    def open_window(self):
        # Laptop_window.hide()
        # Ui.login_window.show()
        
        self.window = QtWidgets.QMainWindow()
        self.ui = self.Ui_login_window
        self.setupUi(self.window)
        self.window.show()

    def setupUi(self, Laptop_window):
        Laptop_window.setObjectName("Laptop_window")
        Laptop_window.resize(792, 561)
        self.centralwidget = QtWidgets.QWidget(Laptop_window)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 791, 541))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 791, 541))
        self.label.setStyleSheet("border-image: url(laptop.jpg);\n"
"\n"
"backgroung-color:rgba(0,0,0,180);\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(290, 10, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(50, 60, 691, 471))
        self.lineEdit.setStyleSheet("border-top-left-radius:50px;\n"
"border-top-right-radius:50px;\n"
"border-bottom-left-radius:50px;\n"
"border-bottom-right-radius:50px;\n"
"background-color: rgb(159,159, 159, 159);")
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setGeometry(QtCore.QRect(180, 120, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("border-top-left-radius:50px;\n"
"border-top-right-radius:50px;\n"
"border-bottom-left-radius:50px;\n"
"border-bottom-right-radius:50px;\n"
"background-color: rgb(190,190, 190, 200);")
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.widget)
        self.comboBox_2.setGeometry(QtCore.QRect(440, 120, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet("border-top-left-radius:50px;\n"
"border-top-right-radius:50px;\n"
"border-bottom-left-radius:50px;\n"
"border-bottom-right-radius:50px;\n"
"background-color: rgb(190,190, 190, 200);")
        self.comboBox_2.setEditable(False)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setGeometry(QtCore.QRect(80, 180, 611, 281))
        self.tableWidget.setStyleSheet("background-color: rgb(150,150, 150, 150);\n"
"")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.Lsave_btn = QtWidgets.QPushButton(self.widget)
        self.Lsave_btn.setGeometry(QtCore.QRect(280, 472, 81, 31))
        self.Lsave_btn.setObjectName("Lsave_btn")
        self.Lback_btn = QtWidgets.QPushButton(self.widget)
        self.Lback_btn.setGeometry(QtCore.QRect(440, 472, 81, 31))
        self.Lback_btn.setObjectName("Lback_btn")

        self.Lback_btn.clicked.connect(self.open_window)


        self.Lscrap_btn = QtWidgets.QPushButton(self.widget)
        self.Lscrap_btn.setGeometry(QtCore.QRect(290, 80, 151, 31))
        self.Lscrap_btn.setObjectName("Lscrap_btn")

        # self.Lsave_btn.clicked.connect(self.showmsg)

        # a = self.scrap()
        # if(a):
                

        Laptop_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Laptop_window)
        self.statusbar.setObjectName("statusbar")
        Laptop_window.setStatusBar(self.statusbar)

        self.retranslateUi(Laptop_window)
        QtCore.QMetaObject.connectSlotsByName(Laptop_window)

    def retranslateUi(self, Laptop_window):
        _translate = QtCore.QCoreApplication.translate
        Laptop_window.setWindowTitle(_translate("Laptop_window", "MainWindow"))
        self.label_2.setText(_translate("Laptop_window", "<html><head/><body><p><span style=\" font-size:24pt; color:#ffffff;\">LAPTOPS</span></p></body></html>"))
        self.comboBox.setCurrentText(_translate("Laptop_window", "Sorting Algorithms"))
        self.comboBox.setItemText(0, _translate("Laptop_window", "Sorting Algorithms"))
        self.comboBox.setItemText(1, _translate("Laptop_window", "Insertion Sort"))
        self.comboBox.setItemText(2, _translate("Laptop_window", "Merge Sort"))
        self.comboBox.setItemText(3, _translate("Laptop_window", "Quick Sort"))
        self.comboBox.setItemText(4, _translate("Laptop_window", "Bubble Sort"))
        self.comboBox.setItemText(5, _translate("Laptop_window", "Selection Sort"))
        self.comboBox.setItemText(6, _translate("Laptop_window", "Bucket Sort"))
        self.comboBox.setItemText(7, _translate("Laptop_window", "Tree Sort"))
        self.comboBox.setItemText(8, _translate("Laptop_window", "Sleep Sort"))
        self.comboBox.setItemText(9, _translate("Laptop_window", "Counting Sort"))
        self.comboBox.setItemText(10, _translate("Laptop_window", "Radix Sort"))
        self.comboBox_2.setCurrentText(_translate("Laptop_window", "Sorting Order"))
        self.comboBox_2.setItemText(0, _translate("Laptop_window", "Sorting Order"))
        self.comboBox_2.setItemText(1, _translate("Laptop_window", "Ascending Order"))
        self.comboBox_2.setItemText(2, _translate("Laptop_window", "Decsending order"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Laptop_window", "Model"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Laptop_window", "Color"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Laptop_window", "Rating"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Laptop_window", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Laptop_window", "GPU"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Laptop_window", "SSD"))
        self.Lsave_btn.setText(_translate("Laptop_window", "Save"))
        self.Lback_btn.setText(_translate("Laptop_window", "Back"))
        self.Lscrap_btn.setText(_translate("Laptop_window", "Start Scrapping"))
# import laptopform_rc

# '''
#     def showmsg(self):
#         msg = QMessageBox()
#         msg.setWindowTitle("Information of Scrapping")
#         msg.setText("Scrapping has been started!")
#         x = msg.exec_()
# '''
# '''
#     def scrap(self):
#         from selenium import webdriver 
#         from bs4 import BeautifulSoup
#         import pandas as pd
#         import pip._vendor.requests
#         from pip._vendor import requests
#         import time

#         # browser =  r"C:\Users\DELL\Desktop\web driver\chrome.exe"

#         # print(soup.prettify())
#         # print(soup)

#         url_list = []
#         # df = pd.read_csv('laptop.csv')
#         # df

#         url = 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2540003.m570.l1313&_nkw=macbook&_sacat=0'
#         Products=[] 
#         Prices=[]  
#         Shipping=[]
#         Location=[]
#         Item=[]
#         Sold=[]
#         Subtitle=[]

#         # content = driver.page_source
#         for i in range(1,101):
#                 print(i)
#                 url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=macbook&_sacat=0%27&_ipg=60&_pgn='+str(i)
#                 #     print(url)
#                 #     time.sleep(5)
#                 req = requests.get(url)
#                 time.sleep(10)
#                 soup = BeautifulSoup(req.content , 'html.parser')
#         for a in soup.findAll('div',attrs={'class':'s-item__info clearfix'}):
#                 products=a.find('span', attrs={'class':'BOLD'})
#                 print(products)
#                 price=a.find('div', attrs={'class':'s-item__detail s-item__detail--primary'})
#                 shipping=a.find('div', attrs={'class':'s-item__shipping s-item__logisticsCost'})
#                 location=a.find('span' , attrs={'class':'s-item__location s-item__itemLocation'})
#                 item=a.find('span',attrs={'class':'s-item__gsp-info s-item__gspInfo'})
#                 sold=a.find('span',attrs={'class':'BOLD'})
#                 subtitle=a.find('div',attrs={'class':'s-item__subtitle'})
#                 try:
#                         Products.append(products.text)
#                         products = products.text
#                 except:
#                         Products.append("Null")
#                         products = "Null"
#                 try:
#                         Prices.append(price.text)
#                         price = price.text
#                 except:
#                         Prices.append("Null")
#                         price = "Null"
#                 try:
#                         Shipping.append(shipping.value)
#                         shipping = shipping.text
#                 except:
#                         Shipping.append("Null")
#                         shipping = "Null"
#                 try:
#                         Location.append(location.text)
#                         location = location.text
#                 except:
#                         Location.append("Null")
#                         location = "Null"
#                 try:
#                         Item.append(item.text)
#                         item = item.text
#                 except:
#                         Item.append("Null")
#                         item = "Null"
#                 try:
#                         Sold.append(sold.text)
#                         sold = sold.text
#                 except:
#                         Sold.append("Null")
#                         sold = "Null"
#                 try:
#                         Subtitle.append(subtitle.text)
#                         subtitle = subtitle.text
#                 except:
#                         Subtitle.append("Null")
#                         subtitle = "Null"
                
                
#         #         print([products])
                
#                 df = pd.DataFrame({'Product Name':[products],'Price':[price] ,
#                                 'Shipping':[shipping],'Location':[location],
#                                 'Item':[item],'Sold':[sold],'Subtitle':[subtitle]})
#                 df.to_csv(r'products.csv', header=False, mode = 'a' ,index=False, encoding='utf-8')
#                 df.to_csv('macbook.csv', header=False, mode = 'a' ,index=False, encoding='utf-8')
# '''

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Laptop_window = QtWidgets.QMainWindow()
    ui = Ui_Laptop_window()
    ui.setupUi(Laptop_window)
    Laptop_window.show()
    sys.exit(app.exec_())
