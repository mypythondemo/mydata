# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectdate_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_selectdate(object):
    def setupUi(self, selectdate):
        selectdate.setObjectName("selectdate")
        selectdate.resize(387, 145)
        selectdate.setMaximumSize(QtCore.QSize(390, 145))
        self.t1 = QtWidgets.QLineEdit(selectdate)
        self.t1.setGeometry(QtCore.QRect(42, 30, 122, 24))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.t1.setFont(font)
        self.t1.setText("")
        self.t1.setObjectName("t1")
        self.label = QtWidgets.QLabel(selectdate)
        self.label.setGeometry(QtCore.QRect(182, 32, 35, 19))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.t2 = QtWidgets.QLineEdit(selectdate)
        self.t2.setGeometry(QtCore.QRect(222, 30, 126, 24))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.t2.setFont(font)
        self.t2.setText("")
        self.t2.setObjectName("t2")
        self.Qdate = QtWidgets.QCalendarWidget(selectdate)
        self.Qdate.setGeometry(QtCore.QRect(106, 60, 237, 151))
        self.Qdate.setObjectName("Qdate")
        self.bt1 = QtWidgets.QPushButton(selectdate)
        self.bt1.setGeometry(QtCore.QRect(74, 94, 89, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.bt1.setFont(font)
        self.bt1.setObjectName("bt1")
        self.bt2 = QtWidgets.QPushButton(selectdate)
        self.bt2.setGeometry(QtCore.QRect(226, 94, 89, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.bt2.setFont(font)
        self.bt2.setObjectName("bt2")
        self.line = QtWidgets.QFrame(selectdate)
        self.line.setGeometry(QtCore.QRect(26, 62, 335, 27))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.s1 = QtWidgets.QPushButton(selectdate)
        self.s1.setGeometry(QtCore.QRect(146, 30, 19, 26))
        self.s1.setObjectName("s1")
        self.s2 = QtWidgets.QPushButton(selectdate)
        self.s2.setGeometry(QtCore.QRect(330, 30, 19, 26))
        self.s2.setObjectName("s2")
        self.line.raise_()
        self.t1.raise_()
        self.label.raise_()
        self.t2.raise_()
        self.bt1.raise_()
        self.bt2.raise_()
        self.s1.raise_()
        self.s2.raise_()
        self.Qdate.raise_()

        self.retranslateUi(selectdate)
        self.bt2.clicked.connect(selectdate.close)
        QtCore.QMetaObject.connectSlotsByName(selectdate)

    def retranslateUi(self, selectdate):
        _translate = QtCore.QCoreApplication.translate
        selectdate.setWindowTitle(_translate("selectdate", "Dialog"))
        self.label.setText(_translate("selectdate", "至"))
        self.bt1.setText(_translate("selectdate", "确 定"))
        self.bt2.setText(_translate("selectdate", "取 消"))
        self.s1.setText(_translate("selectdate", "↓"))
        self.s2.setText(_translate("selectdate", "↓"))

