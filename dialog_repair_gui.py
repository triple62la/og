# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_repair_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OtherWindow(object):
    def setupUi(self, OtherWindow):
        OtherWindow.setObjectName("OtherWindow")
        OtherWindow.resize(826, 391)
        self.centralwidget = QtWidgets.QWidget(OtherWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_repair = QtWidgets.QPushButton(self.centralwidget)
        self.button_repair.setGeometry(QtCore.QRect(10, 320, 161, 23))
        self.button_repair.setObjectName("button_repair")
        self.button_get = QtWidgets.QPushButton(self.centralwidget)
        self.button_get.setGeometry(QtCore.QRect(190, 320, 161, 23))
        self.button_get.setObjectName("button_get")
        self.button_close = QtWidgets.QPushButton(self.centralwidget)
        self.button_close.setGeometry(QtCore.QRect(720, 320, 91, 23))
        self.button_close.setObjectName("button_close")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 290, 231, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.button_search = QtWidgets.QPushButton(self.centralwidget)
        self.button_search.setGeometry(QtCore.QRect(250, 290, 101, 23))
        self.button_search.setObjectName("button_search")
        self.list_zakaz = QtWidgets.QListView(self.centralwidget)
        self.list_zakaz.setGeometry(QtCore.QRect(10, 10, 801, 271))
        self.list_zakaz.setObjectName("list_zakaz")
        OtherWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(OtherWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 826, 21))
        self.menubar.setObjectName("menubar")
        OtherWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(OtherWindow)
        self.statusbar.setObjectName("statusbar")
        OtherWindow.setStatusBar(self.statusbar)

        self.retranslateUi(OtherWindow)
        self.button_get.clicked.connect(self.lineEdit.selectAll)
        self.button_get.clicked.connect(self.lineEdit.copy)
        QtCore.QMetaObject.connectSlotsByName(OtherWindow)

    def retranslateUi(self, OtherWindow):
        _translate = QtCore.QCoreApplication.translate
        OtherWindow.setWindowTitle(_translate("OtherWindow", "Восстановить"))
        self.button_repair.setText(_translate("OtherWindow", "Восстановить данные"))
        self.button_get.setText(_translate("OtherWindow", "Получить данные"))
        self.button_close.setText(_translate("OtherWindow", "Закрыть"))
        self.button_search.setText(_translate("OtherWindow", "Найти"))
