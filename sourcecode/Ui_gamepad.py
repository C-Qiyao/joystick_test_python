# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\11139\Documents\gitee\python_joystick\gamepad.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1668, 1047)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 500, 401, 501))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.comboBox_SerialSel = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_SerialSel.setObjectName("comboBox_SerialSel")
        self.verticalLayout.addWidget(self.comboBox_SerialSel)
        self.pushButton_SerialCon = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_SerialCon.setObjectName("pushButton_SerialCon")
        self.verticalLayout.addWidget(self.pushButton_SerialCon)
        self.pushButton_start = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_start.setObjectName("pushButton_start")
        self.verticalLayout.addWidget(self.pushButton_start)
        self.pushButton_stop = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.verticalLayout.addWidget(self.pushButton_stop)
        self.disconnect = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.disconnect.setObjectName("disconnect")
        self.verticalLayout.addWidget(self.disconnect)
        self.pushButton_quit = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_quit.setObjectName("pushButton_quit")
        self.verticalLayout.addWidget(self.pushButton_quit)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 10, 311, 51))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.message = QtWidgets.QTextEdit(self.centralwidget)
        self.message.setGeometry(QtCore.QRect(50, 70, 391, 401))
        self.message.setObjectName("message")
        self.widget_Cur_Thr = QtWidgets.QWidget(self.centralwidget)
        self.widget_Cur_Thr.setGeometry(QtCore.QRect(1050, 20, 591, 491))
        self.widget_Cur_Thr.setObjectName("widget_Cur_Thr")
        self.widget_Cur_Brk = QtWidgets.QWidget(self.centralwidget)
        self.widget_Cur_Brk.setGeometry(QtCore.QRect(450, 20, 591, 491))
        self.widget_Cur_Brk.setObjectName("widget_Cur_Brk")
        self.widget_Cur_x2y2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_Cur_x2y2.setGeometry(QtCore.QRect(1050, 520, 591, 491))
        self.widget_Cur_x2y2.setObjectName("widget_Cur_x2y2")
        self.widget_Cur_x1y1 = QtWidgets.QWidget(self.centralwidget)
        self.widget_Cur_x1y1.setGeometry(QtCore.QRect(450, 520, 591, 491))
        self.widget_Cur_x1y1.setObjectName("widget_Cur_x1y1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1668, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "连接手柄"))
        self.pushButton_SerialCon.setText(_translate("MainWindow", "连接串口"))
        self.pushButton_start.setText(_translate("MainWindow", "开始读取"))
        self.pushButton_stop.setText(_translate("MainWindow", "停止读取"))
        self.disconnect.setText(_translate("MainWindow", "断开连接"))
        self.pushButton_quit.setText(_translate("MainWindow", "退出程序"))
        self.label.setText(_translate("MainWindow", "超平机器人手柄连接软件"))