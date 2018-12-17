# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwin_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWin(object):
    def setupUi(self, mainWin):
        mainWin.setObjectName("mainWin")
        mainWin.resize(1024, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWin.sizePolicy().hasHeightForWidth())
        mainWin.setSizePolicy(sizePolicy)
        mainWin.setMaximumSize(QtCore.QSize(16777215, 16777215))
        mainWin.setBaseSize(QtCore.QSize(0, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWin.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(mainWin)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(2, 6, 1021, 637))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.MaingridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.MaingridLayout.setContentsMargins(0, 0, 0, 0)
        self.MaingridLayout.setObjectName("MaingridLayout")
        mainWin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 17))
        self.menubar.setObjectName("menubar")
        self.menu_B = QtWidgets.QMenu(self.menubar)
        self.menu_B.setObjectName("menu_B")
        self.menu_C = QtWidgets.QMenu(self.menubar)
        self.menu_C.setObjectName("menu_C")
        self.menu_S = QtWidgets.QMenu(self.menubar)
        self.menu_S.setObjectName("menu_S")
        self.menu_X = QtWidgets.QMenu(self.menubar)
        self.menu_X.setObjectName("menu_X")
        mainWin.setMenuBar(self.menubar)
        self.sb = QtWidgets.QStatusBar(mainWin)
        self.sb.setObjectName("sb")
        mainWin.setStatusBar(self.sb)
        self.action_J = QtWidgets.QAction(mainWin)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ico/rent-a-car.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_J.setIcon(icon1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.action_J.setFont(font)
        self.action_J.setMenuRole(QtWidgets.QAction.QuitRole)
        self.action_J.setIconVisibleInMenu(True)
        self.action_J.setPriority(QtWidgets.QAction.LowPriority)
        self.action_J.setObjectName("action_J")
        self.action_C = QtWidgets.QAction(mainWin)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("ico/analysis.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_C.setIcon(icon2)
        self.action_C.setObjectName("action_C")
        self.action_M = QtWidgets.QAction(mainWin)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("ico/业主中心-物业缴费.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_M.setIcon(icon3)
        self.action_M.setObjectName("action_M")
        self.action_Y = QtWidgets.QAction(mainWin)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("ico/已缴费 copy@1x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Y.setIcon(icon4)
        self.action_Y.setObjectName("action_Y")
        self.action_B = QtWidgets.QAction(mainWin)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("ico/usb.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_B.setIcon(icon5)
        self.action_B.setObjectName("action_B")
        self.action_T = QtWidgets.QAction(mainWin)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("ico/calenda.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_T.setIcon(icon6)
        self.action_T.setObjectName("action_T")
        self.action_L = QtWidgets.QAction(mainWin)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("ico/bus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_L.setIcon(icon7)
        self.action_L.setObjectName("action_L")
        self.action_D = QtWidgets.QAction(mainWin)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("ico/flag-china.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_D.setIcon(icon8)
        self.action_D.setObjectName("action_D")
        self.action_Z = QtWidgets.QAction(mainWin)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("ico/接车开单.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Z.setIcon(icon9)
        self.action_Z.setObjectName("action_Z")
        self.action_F = QtWidgets.QAction(mainWin)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("ico/充值缴费.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_F.setIcon(icon10)
        self.action_F.setObjectName("action_F")
        self.action_R = QtWidgets.QAction(mainWin)
        self.action_R.setEnabled(False)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("ico/teacher-male.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_R.setIcon(icon11)
        self.action_R.setObjectName("action_R")
        self.action_N = QtWidgets.QAction(mainWin)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("ico/精美主题.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_N.setIcon(icon12)
        self.action_N.setObjectName("action_N")
        self.action_H = QtWidgets.QAction(mainWin)
        self.action_H.setObjectName("action_H")
        self.menu_B.addSeparator()
        self.menu_B.addAction(self.action_J)
        self.menu_C.addAction(self.action_C)
        self.menu_C.addSeparator()
        self.menu_C.addAction(self.action_M)
        self.menu_C.addSeparator()
        self.menu_C.addAction(self.action_Y)
        self.menu_C.addSeparator()
        self.menu_S.addSeparator()
        self.menu_S.addAction(self.action_L)
        self.menu_S.addAction(self.action_D)
        self.menu_S.addSeparator()
        self.menu_S.addAction(self.action_Z)
        self.menu_S.addSeparator()
        self.menu_S.addAction(self.action_F)
        self.menu_S.addSeparator()
        self.menu_S.addAction(self.action_R)
        self.menu_S.addSeparator()
        self.menu_X.addAction(self.action_B)
        self.menu_X.addSeparator()
        self.menu_X.addAction(self.action_T)
        self.menu_X.addSeparator()
        self.menu_X.addAction(self.action_N)
        self.menu_X.addSeparator()
        self.menu_X.addAction(self.action_H)
        self.menu_X.addSeparator()
        self.menubar.addAction(self.menu_B.menuAction())
        self.menubar.addAction(self.menu_C.menuAction())
        self.menubar.addAction(self.menu_S.menuAction())
        self.menubar.addAction(self.menu_X.menuAction())

        self.retranslateUi(mainWin)
        QtCore.QMetaObject.connectSlotsByName(mainWin)

    def retranslateUi(self, mainWin):
        _translate = QtCore.QCoreApplication.translate
        mainWin.setWindowTitle(_translate("mainWin", "车辆缴费系统"))
        self.menu_B.setTitle(_translate("mainWin", "业务办理(&B)"))
        self.menu_C.setTitle(_translate("mainWin", "查询打印(&C)"))
        self.menu_S.setTitle(_translate("mainWin", "数据维护（&S)"))
        self.menu_X.setTitle(_translate("mainWin", "系统设置（&X)"))
        self.action_J.setText(_translate("mainWin", "车辆缴费(&J)"))
        self.action_C.setText(_translate("mainWin", "信息查询(&C)"))
        self.action_M.setText(_translate("mainWin", "每日清单(&M)"))
        self.action_Y.setText(_translate("mainWin", "月结清单(&Y)"))
        self.action_B.setText(_translate("mainWin", "数据库备份(&B)"))
        self.action_T.setText(_translate("mainWin", "数据库同步(&T)"))
        self.action_L.setText(_translate("mainWin", "车辆类别(&L)"))
        self.action_D.setText(_translate("mainWin", "车牌地区(&D)"))
        self.action_Z.setText(_translate("mainWin", "站点维护(&Z)"))
        self.action_F.setText(_translate("mainWin", "缴费金额(&F)"))
        self.action_R.setText(_translate("mainWin", "人员维护(&R)"))
        self.action_N.setText(_translate("mainWin", "数据初始化(&M)"))
        self.action_H.setText(_translate("mainWin", "异地数据库(D)"))

