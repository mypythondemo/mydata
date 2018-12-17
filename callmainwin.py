#!/usr/bin/env python3
import os
import sys
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtSql import (QSqlDatabase, QSqlQuery, QSqlRelation,QSqlRelationalDelegate, QSqlRelationalTableModel,QSqlTableModel)   
import time
#from PyQt5.QtCore import QDate
#导入外部自定窗体文件
from mainwin_ui import Ui_mainWin    #Mdi主信息窗体
from setinfowin_ui import Ui_infoWin #设置基本信息窗体
from workwin_ui import Ui_Form       #业务办理窗体
from selectdate_ui import Ui_selectdate  #选择时间段
from optDb import *                  #数据库connect，model,query,相关模块 operator database
from demoprint import *

#class 初始化主窗体===================================
class MainForm(QMainWindow,Ui_mainWin):
    def __init__(self):
        super(MainForm,self).__init__()
        self.setupUi(self)

        #定义mainwindow信号
            #menu信号
        self.action_J.triggered.connect(self.workwin_show)
        self.action_C.triggered.connect(self.open_msg)
        self.action_M.triggered.connect(self.PrintRb)
        self.action_Y.triggered.connect(self.selectdtwin_show)
        self.action_B.triggered.connect(self.save_msg)
        self.action_T.triggered.connect(self.callupdaetb)
        self.action_L.triggered.connect(self.infowin_show)
        self.action_D.triggered.connect(self.infowin_show)
        self.action_Z.triggered.connect(self.infowin_show)
        self.action_F.triggered.connect(self.infowin_show)
        self.action_R.triggered.connect(self.infowin_show)
        self.action_N.triggered.connect(self.initDate)
        self.action_H.triggered.connect(self.open_msg)
        self.action_C.setVisible(False)   #人员
        self.action_N.setEnabled(False)   #初始化
        self.setIcon() 
        self.resize(1024, 680)
        screen=QDesktopWidget().screenGeometry()
        size=self.geometry()
        self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2-30)
#开启新进程,每一分钟更新两个库的work表
        self.up=UpdateTb()
        self.up.beginUp()
        
    def setIcon(self):
        palette1 = QPalette()
        # palette1.setColor(self.backgroundRole(), QColor(192,253,123))   # 设置背景颜色
        palette1.setBrush(self.backgroundRole(), QBrush(QPixmap(r'.\ico\rr.jpg')))   # 设置背景图片
        self.setPalette(palette1)
    def initDate(self):
        if QMessageBox.question(self,  "初始化", "确定要初始化数据库吗?\r\n数据将丢失!")==QMessageBox.Yes:
            initdt=SaveNewData_py()
            initdt.save_data('DELETE FROM del_recd')
            initdt=SaveNewData_py()
            initdt.save_data('DELETE FROM dict_cldq')
            initdt=SaveNewData_py()
            initdt.save_data('DELETE FROM dict_cllb')
            initdt=SaveNewData_py()
            initdt.save_data('DELETE FROM dict_jfje')
            initdt=SaveNewData_py()
            initdt.save_data('DELETE FROM work')
            initdt=SaveNewData_py()
            initdt.save_data('DELETE FROM work_id')
            initdt=SaveNewData_py()
            initdt.save_data('DELETE FROM tmp_worker_yjb')
            initdt=SaveNewData_py()
            initdt.save_data('DELETE FROM tmp_worker_yjb')
            QMessageBox.information(self, "初始化完成", "初始化数据库完成!", QMessageBox.Yes)
        else:
            QMessageBox.information(self, "初始化失败", "终止初始化数据库!", QMessageBox.Yes)
    def callupdaetb(self):
        r1, r2=tbTotbUpdate()
        self.sb.showMessage('成功导出:{}条数据, 成功导入:{}条数据'.format(r1, r2))
    #业务窗体show的SLOT
    def workwin_show(self):
        try:
            if  not self.workForm.isVisible():
                self.workForm=InitWin_work()  #办理业务窗体初始化
                self.MaingridLayout.addWidget(self.workForm)
                self.workForm.show()
        except:
                self.workForm=InitWin_work()  #办理业务窗体初始化
                self.MaingridLayout.addWidget(self.workForm)
                self.workForm.show()
    #基本信息窗体show的SLOT
    def infowin_show(self):
        try:
            #判断窗口是否存在,如果不存在,说明第一次打开,会报错,在EXCEPT里初始化,若存在,什么也不做
            if  not self.setForm.isVisible(): 

                sender=self.sender()
                str=sender.text()[:-4]
                print(str)
                if str=="人员维护":
                    tableName="user"
                elif str=="站点维护":
                    tableName="dict_zd"
                elif str=="车辆类别":
                    tableName="dict_cllb"
                elif str=="车牌地区":
                    tableName="dict_cldq"
                else:
                    tableName="dict_jfje"

                self.setForm=InitWin_setInfo()  #基本信息窗体初始化
                self.setForm.openDb_table(tableName) #传入表格，设置MODEL
                self.MaingridLayout.addWidget(self.setForm)
                self.setForm.show()                  #基本信息子窗体显示
        except:
            sender=self.sender()
            str=sender.text()[:-4]
            print(str)
            if str=="人员维护":
                tableName="user"
            elif str=="站点维护":
                tableName="dict_zd"
            elif str=="车辆类别":
                tableName="dict_cllb"
            elif str=="车牌地区":
                tableName="dict_cldq"
            else:
                tableName="dict_jfje"

            self.setForm=InitWin_setInfo()  #基本信息窗体初始化
            self.setForm.openDb_table(tableName) #传入表格，设置MODEL
            self.MaingridLayout.addWidget(self.setForm)
            self.setForm.show()                  #基本信息子窗体显示
        #self.MaingridLayout.addWidget(self.setinfo)
    def selectdtwin_show(self):
        try:
            if  not self.seldt.isVisible():
                self.seldt=InitWin_seldt()
                self.seldt.show()
            else:
                self.seldt.show()
        except:
            self.seldt=InitWin_seldt()
            self.seldt.show()
    def save_msg(self):
#        file,ok=QFileDialog.getOpenFileName(self,"open","d:/","All Files(*);;Text Files (*.txt)")
        #pathn=
        fileName, ok = QFileDialog.getSaveFileName(self,r"选择数据库",r".\data\backup\\",r"SQL DATE Files(*.db)")
        if ok:
            backupSqlite(fileName)
            self.sb.showMessage('备份成功!')
        else:
            self.sb.showMessage('备份失败!')
    def open_msg(self):
        fileName,ok=QFileDialog.getOpenFileName(self,"选择同步的数据库",r"c:/",r"SQL DATE Files(*.db)")
        #pathn=
#        fileName, ok = QFileDialog.getSaveFileName(self,r"选择数据库",r".\data\backup\\",r"SQL DATE Files(*.db)")
        if ok:
            setDbPath(fileName)
            self.sb.showMessage('设置成功!')
        else:
            self.sb.showMessage('设置失败!')
#自定义信号
#class Mysignal(QLineEdit):
#        showtabdata=pyqtSignal() #显示table数据
#        gettabdata=pyqtSignal()   #获取表格数据

    #业务窗体初始化
    #日报表
    def PrintRb(self):
        try:
            self.prtybb=Printer()
            #sqlstr, tit_pt,subtit_pt, date_pt,colsize,ltop_pt,rbot_pt
            self.title=' 每 日 报 表 '
            self.subtit= time.strftime('%Y-%m-%d',time.localtime(time.time())) + ' '*50
            self.datept="制表时间:" + time.strftime('%Y-%m-%d',time.localtime(time.time()))+ "     制表人:" + setworker.worker
            self.colsize=[8, 10, 6, 6, 8]
            self.ltop=[1, 1]
            self.rbot=[3, 1]

            self.nowtime=time.strftime('%Y-%m-%d',time.localtime(time.time()))
            str1='''create table tmp_worker_yjb as select worker  as 收款人1,worker  as 收款人,车辆类别,缴费金额 as 收费项目,count(缴费金额) as 项目笔数,(缴费金额*count(缴费金额)) as 金额合计 from work where 0=1 group by worker,缴费金额 order by worker,缴费金额'''
            self.selDat=createnewtb('tmp_worker_yjb',str1)
            str1='''select worker  as 收款人1,worker  as 收款人,车辆类别,缴费金额 as 收费项目,count(缴费金额) as 项目笔数,(缴费金额*count(缴费金额)) as 金额合计  from work where date(opdate)=?  group by worker,缴费金额 order by worker,缴费金额 desc'''
            str2=self.nowtime
            self.selDat=Selectdata_py()
            self.tit, self.rec=self.selDat.select_data(str1,str2)
            if len(self.rec)==0:
                QMessageBox.information(self, "查询失败", '没有找到此时间段数据,请更改时间段再试',QMessageBox.Yes)
                return
            str1="insert into tmp_worker_yjb " + str1

            self.updtDt=SaveNewData_py()
            if self.updtDt.save_data(str1,str2):
                str2='select 收款人1,收款人,count(车辆类别) as 类别,count(车辆类别) as 项目,sum(项目笔数)as 笔数 ,sum(金额合计)as 金额 from tmp_worker_yjb group by 收款人'
                self.selDat=Selectdata_py()
                self.tit, self.rec=self.selDat.select_data(str2)
                str2='insert into tmp_worker_yjb (收款人1,收款人,车辆类别,收费项目,项目笔数,金额合计) values (?,?,?,?,?,?)'
                #sumhj=[]
                for rectdate in self.rec:
    #                    if len(sumhj)==0:
    #                        sumhj=[rectdate[4],rectdate[5]]
    #                    else:
    #                        sumhj=[sumhj[0]+rectdate[4],sumhj[1]+rectdate[5]]
                    rectdate=list(rectdate)
                    rectdate[1]= rectdate[1]+'(小计):'
                    rectdate=tuple(rectdate)
                    self.updtDt=SaveNewData_py()
                    self.updtDt.save_data(str2, *rectdate)
                #sumhj=[self.rec[0][3]+self.rec[1][3], self.rec[0][4]+self.rec[1][4]]
    #                sumhj.insert(0, '总 计:')
    #                sumhj.insert(0, 'z')
    #                sumhj=tuple(sumhj)
    #                str2='insert into tmp_worker_yjb (收款人1,收款人,项目笔数,金额合计) values (?,?,?,?)'
    #                
    #                self.updtDt=SaveNewData_py()
    #                self.updtDt.save_data(str2,*sumhj)
    #            
            else:
                QMessageBox(self, "查询失败", '数据更新出错,请联系管理员',QMessageBox.Yes)

            self.sqlstr_yb="SELECT 收款人,车辆类别,收费项目,项目笔数,金额合计 FROM tmp_worker_yjb order by 收款人,金额合计"
            self.prtybb.tablePt(self.sqlstr_yb,self.title,self.subtit,self.datept,self.colsize,self.ltop,self.rbot)
            #self.close()
        except:
            QMessageBox.warning(self, '错误', '今天还没有收费或者数据出错', QMessageBox.Yes)

#class 初始化工作窗体======================================
class InitWin_work(QMainWindow,Ui_Form):
    def __init__(self):
        super(InitWin_work,self).__init__()
        self.oldtime=''
        self.setupUi(self)
        self.resiz_form()
    def view_pt(self):
        if not self.isVisible():
            self.showMaximized()
    #slot 计算（金额/收费标准=次数）
    def eva(self):
        try:
            self.txt_cs.setText(str(int(eval(self.txt_je.text() + '/' + self.txt_bz.text()))))
        except:
            self.msg(1, "数据错误", "录入数据 1.缴费标准  2。缴费金额 必须为数字！ 请查询输入数据")
            self.txt_je.setText('')
            self.txt_bz.setText('')
            self.txt_bz.setFocus()
            return
    #重构业务办理界面的 keyPressEvent。车辆类别、车牌输入 在助记码后回车调用showtable
    def keyPressEvent(self, e):
        #print('print key', e.text(), e.key(), "dict:", self.dict_pan.hasFocus(), "txt_lb:", self.txt_lb.hasFocus())
        #在dict_pan 获得焦点状态下，按ESC键时， 隐藏dict_pan，激活他的控件获得焦点
        if e.key()==Qt.Key_Escape and self.dict_pan.hasFocus():
            self.dict_pan.hide()
            act_txt.setFocus()
        #在dict_pan没有获得焦点状态下，判断焦点在哪个控件下按了回车键，然后调用showtable来激活dict_pan显示数据
        if e.key()==Qt.Key_Return:   #判断是不是按了回车
            #依据判断控件的焦点，来判断哪个控件按了回车，发送Signal ***hasFocus
            if self.txt_lb.hasFocus():       #车辆类别有焦点，showtable dict_cllb表
                self.showtable(self.txt_lb)
            elif self.dict_pan.hasFocus():   #dict_pan拥有焦点，按回车则说明确认了dict_pan数据，so发送signal,激活connect连接的slot(tbTotxt函数)
                self.mysig.set_data_signal.emit()  #     ******发送信号，激活connect 连接的 slot 函数*******
                                                   #函数初始化时，用自定义的信号连接到槽函数 self.mysig.set_data_signal.connect(self.tbTotxt)。在此时（回车）时激活(emit())此连接 
            elif self.txt_pz.hasFocus():     #牌照
                if self.txt_pz.text()!='' and ord(self.txt_pz.text()[0])>122:
                    self.txt_dw.setFocus()
                else:
                    self.showtable(self.txt_pz)
            elif self.txt_name.hasFocus():   #在name 回车后 类别获得焦点
                self.txt_lb.setFocus()
            elif self.txt_xh.hasFocus():     #在型号 回车后 牌照获得焦点
                self.txt_pz.setFocus()
            elif self.txt_mc.hasFocus():     #在单位名称 回车后 车主姓名获得焦点
                self.txt_name.setFocus()
            elif self.txt_serch.hasFocus():                            #查询work
                self.showtable(self.txt_serch)

    #业务办理界面窗体初始化
    def resiz_form(self):
        #设置窗体以及控件位置，格式等
        
        self.btn_del.hide()
        self.mydb=Selectdata_py()
        tit, record=self.mydb.select_data("select * from dict_zd")
        itemlist=[rec[1] for rec in record]
        self.comb_zd.addItems(itemlist)
        self.dict_pan.hide()
        self.dict_pan.setSelectionMode(QTableView.SingleSelection)
        self.dict_pan.setSelectionBehavior(QTableView.SelectRows)
        #self.tbv.setColumnHidden(id, True)
        self.dict_pan.resizeColumnsToContents()
        #self.showMaximized()
        screen=QDesktopWidget().screenGeometry()
        size=self.geometry()
        self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2-30)
        
        if setworker.worker=='管理员':
            self.btn_del.show()
            self.btn_del.setEnabled(True)
        #自定义信号和槽
        #三个按钮
        self.btn_save.clicked.connect(self.save_data)  #保存新录入数据
        self.btn_serch.clicked.connect(self.modify_save_data)  #保存修改后录入数据
        self.btn_del.clicked.connect(self.del_data)  #删除这条数据
        self.btn_clear.clicked.connect(self.clear_txt)  #删除这条数据
        #把查询，车牌，挂车车牌 改为大写字母
        self.txt_pz.editingFinished.connect(self.daxie)
        self.txt_gcpz.editingFinished.connect(self.daxie)
        self.txt_serch.editingFinished.connect(self.daxie)

        #编辑完成（失去焦点）时，自动除法计算得到通行次数dict_cs（金额/单价、收费标准=通行次数）
        self.txt_je.editingFinished.connect(self.eva)
        self.clear_txt()

        #测试用数据！！！！
#        self.txt_mc.setText("mingcheng")
#        self.txt_name.setText("name")
#        self.txt_lb.setText("lb")
#        self.txt_xh.setText("xhh")
#        self.txt_pz.setText("jing J")
#        self.txt_dw.setText("dw")
#        self.txt_bz.setText("20")
#        self.txt_je.setText("2000")
#        self.txt_cs.setText("10")
#        self.txt_gcpz.setText("gcpz H")
#        self.txt_gcdw.setText("2000")

        #自定义信号
        self.mysig = Mysignal()   #实例化一个自定义信号类（Mysignal)
        self.mysig.set_data_signal.connect(self.tbTotxt) #类变量set_data_signal(一个自定义信号,类型：pyqtSignal)，连接到槽函数
        '''===================================================================
                              关于自定义信号的用法：

        1.定义一个类，该类对应QObject（可否对应其他？控件）  class Mysignal(QObject)
        2.类里定义一个类变量，类型为信号                        set_data_signal = pyqtSignal()
        3.在应用该信号类的初始化里实例化该信号类             mysig=Mysignal()
        4.信号类实例通过类变量连接到槽                     self.mysig.set_data_signal.connect(self.tbTotxt)
        5.在需要发送信号的地方(keyPressEvent)用emit发送信号 self.mysig.set_data_signal.emit
        注：需要在开始前引入Qpyqtsignal QObject                   from PyQt5.QtCore import *
        ==================================================================='''

    #清除控件的字符
    def clear_txt(self):
        self.txt_serch.setText("")
        self.txt_mc.setText("")
        self.txt_name.setText("")
        self.txt_lb.setText("")
        self.txt_xh.setText("")
        self.txt_pz.setText("")
        self.txt_dw.setText("")
        self.txt_bz.setText("")
        self.txt_je.setText("")
        self.txt_cs.setText("")
        self.txt_gcpz.setText("")
        self.txt_gcdw.setText("")
        #set of time ,id ,worker
        self.txt_id.setText("")
        self.txt_worker.setText("")
        self.txt_time.setText('')
        self.txt_serch.setFocus()

    #slot  LineEdit的回车键后，show dict_pan table的slot函数，设置表格根据助记码得到的数据并调整位置
    def showtable(self, objtxt):
        global act_txt
        txtname=objtxt.objectName()
        txt=objtxt.text()
        act_txt=objtxt
        txt=txt.replace(' ', '').upper()
        if txt=="":                   #输入助记码是否为空*************        
            QMessageBox.information (self,'提示', "请输入助记码 或者 对应数据", QMessageBox.Yes)
            return
        #查询助记码
        col_format="车牌照号,车主姓名,opdate as 缴费时间,缴费金额,通行次数,缴费标准,车辆类别,车辆型号,吨位座位,挂车车牌, 挂车吨位,单位名称,站点,worker,effective,remarks,id"
        if txtname=="txt_serch":      #查询work表********************
            if self.openQy_table(col_format, "work", txt):   #是否找到数据
                self.txt_serch.setFocus
            else:
                self.dict_pan.show()
                self.dict_pan.move(self.txt_serch.geometry().x()-120,self.txt_serch.geometry().y()+80)
                self.dict_pan.resize(self.width(),400)
                self.dict_pan.setFocus()
        elif txtname=="txt_lb":      #查询车辆类别表****************
            if  self.openQy_table("车辆类别,缴费标准", "dict_cllb", txt):
                self.txt_lb.setFocus
            else:
                self.dict_pan.show()
                print("F",self.openQy_table("车辆类别,缴费标准", "dict_cllb", txt))
                self.dict_pan.move(self.txt_lb.geometry().x()+30,self.txt_lb.geometry().y()+160)
                self.dict_pan.resize(235,250)
                self.dict_pan.setFocus()
        else:                        #查询车辆牌照地区******************
            if  self.openQy_table("车辆地区", "dict_cldq", txt):
                self.txt_pz.setFocus
            else:
                self.dict_pan.show()
                self.dict_pan.move(self.txt_pz.geometry().x()+30,self.txt_pz.geometry().y()+160)
                self.dict_pan.resize(235,300)
                self.dict_pan.setFocus()

    #建立query模型
    def openQy_table(self,col, tbname, zjm):
        flg=False
        if tbname=='work':
            sql_str="select {0} from {1} where 车牌照号 like '%{2}%' order by opdate desc".format(col, tbname, zjm)
        else:
            sql_str="select {0} from {1} where 助记码 like '%{2}%'".format(col, tbname, zjm)
        self.mod=modQy() #create model modQy 定义于optDb类模块
        self.tmod=self.mod.createMod(sql_str)  #setup sqlquery  of model
        self.dict_pan.setModel(self.tmod)  # setup  model of tableview
        print(sql_str,"mod count=", self.tmod.rowCount())
        if self.tmod.rowCount()==0:  #如果RECORD 为空，则返回True
            flg=True
            return flg

    #slot  在dict_pan被按下回车后，读取对应数据到 linetext控件
    def tbTotxt(self):
        #print(act_txt,self.tmod.rowCount(), self.dict_pan.currentIndex().row(), self.dict_pan.currentIndex().data(), self.tmod.record(self.dict_pan.currentIndex().row()).value(1))#, "item",self.tmod.item(0, 1).text())
        print("act_txt.objectName()=", act_txt.objectName(), "=======")
        if self.tmod.rowCount == 0: #若表为空
            print('model is null!!!!')
            return
        else:
            act=act_txt.objectName()
        if act=="txt_serch":   #serch位置激活
            self.loadDataToTb()
            self.dict_pan.hide()
            self.txt_mc.setFocus()
        elif act=="txt_lb":    #txt_lb位置激活
            self.txt_lb.setText(self.tmod.record(self.dict_pan.currentIndex().row()).value(0))
            self.txt_bz.setText(str(self.tmod.record(self.dict_pan.currentIndex().row()).value(1)))
            self.dict_pan.hide()
            self.txt_xh.setFocus()
        else:                      #txt_pz位置激活
            self.txt_pz.setText(self.tmod.record(self.dict_pan.currentIndex().row()).value(0))
            self.dict_pan.hide()
            self.txt_pz.setFocus()
    #将serch里查找到的表格数据到工作界面，根据dict_pan.currentIndex.row()从MODEL读取数据到界面。tbTotxt(self)调用的
    def loadDataToTb(self):
        currentIndex=self.dict_pan.currentIndex().row()
        #self.tmod.record(currentIndex).value("车主姓名")
        self.tmod.record(currentIndex).value("车主姓名")
        self.txt_serch.setText(self.tmod.record(currentIndex).value("车牌照号"))
        self.txt_mc.setText(self.tmod.record(currentIndex).value("单位名称"))
        self.txt_name.setText(self.tmod.record(currentIndex).value("车主姓名"))
        self.txt_lb.setText(self.tmod.record(currentIndex).value("车辆类别"))
        self.txt_xh.setText(self.tmod.record(currentIndex).value("车辆型号"))
        self.txt_pz.setText(self.tmod.record(currentIndex).value("车牌照号"))
        self.txt_dw.setText(self.tmod.record(currentIndex).value("吨位座位"))
        self.txt_bz.setText(str(self.tmod.record(currentIndex).value("缴费标准")))
        self.txt_je.setText(str(self.tmod.record(currentIndex).value("缴费金额")))
        self.txt_cs.setText(str(self.tmod.record(currentIndex).value("通行次数")))
        self.txt_gcpz.setText(self.tmod.record(currentIndex).value("挂车车牌"))
        #隐藏控件，存储  【时间，ID,worker】  数据
        self.txt_time.setText(str(self.tmod.record(currentIndex).value("缴费时间")))
        self.txt_id.setText(str(self.tmod.record(currentIndex).value("id")))
        self.txt_worker.setText(self.tmod.record(currentIndex).value("worker"))
        self.oldtime=self.txt_time.text()
    #slot  带返回值的验证录入信息是否合格函数，(合格返回T,否则为F)以便保存 save 或者 modify到数据库
    def verify_data(self):
        flg=False
        if self.comb_zd.currentText()=="":   #1站点
            self.msg(1,"错误", "录入入内容不完整！请检查各个录入数据！")
            self.comb_zd.setFocus()
            return flg
        if self.txt_name.text()=="":  #2车主姓名
            self.msg(1,"错误", "录入入内容不完整！请检查各个录入数据！")
            self.txt_name.setFocus()
            return flg
        if self.txt_lb.text()=="":  #车类别
            self.msg(1,"错误", "录入入内容不完整！请检查各个录入数据！")
            self.txt_lb.setFocus()
            return flg
        if self.txt_pz.text()=="":  #3牌照
            self.msg(1,"错误", "录入入内容不完整！请检查各个录入数据！")
            self.txt_pz.setFocus()
            return flg
        if self.txt_bz.text()=="":  #4标准
            self.msg(1,"错误", "录入入内容不完整！请检查各个录入数据！")
            self.txt_bz.setFocus()
            return flg
        if self.txt_je.text()=="":  #5金额
            self.msg(1,"错误", "录入入内容不完整！请检查各个录入数据！")
            self.txt_je.setFocus()
            return flg
        if self.txt_cs.text()=="":  #6次数
            self.msg(1,"错误", "录入入内容不完整！请检查各个录入数据！")
            self.txt_cs.setFocus()
            return flg
        return True

    #车牌转大写
    def daxie(self):
        if self.txt_pz.text()!='':
            self.txt_pz.setText(self.txt_pz.text().upper())
        if self.txt_gcpz.text()!='':
            self.txt_gcpz.setText(self.txt_gcpz.text().upper())
        if self.txt_serch.text()!='':
            self.txt_serch.setText(self.txt_serch.text().upper())
    #保存新录入数据
    def save_data(self):
        findda=Selectdata_py()
        str="select * from work where substr(opdate,1,7)='{}'and 车牌照号='{}'".format(time.strftime('%Y-%m-%d',time.localtime(time.time()))[0:7],self.txt_pz.text().strip())
        tit, rec=findda.select_data(str)
        if len(rec)>0:
            self.msg(1, '提示', '该车辆本月已经办理过缴费业务,请查证!')
            return 
        if self.verify_data():
            id=get_workid()  #workid()从optDb 里get_workid()获得
            zdname=self.comb_zd.currentText()
            dwmc=self.txt_mc.text()
            zzxm=self.txt_name.text()
            cllb=self.txt_lb.text()
            clxh=self.txt_xh.text()
            clpz=self.txt_pz.text()
            dw=self.txt_dw.text()
            bz=int(self.txt_bz.text())
            je=int(self.txt_je.text())
            cs=int(self.txt_cs.text())
            gcpz=self.txt_gcpz.text()
            gcdw=self.txt_gcdw.text()
            opdate=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            effective=0
            remarks=''
            #17个字段
            sql_str1="insert into work (id,站点, 单位名称, 车主姓名, 车辆类别, 车辆型号,车牌照号,吨位座位,缴费标准,通行次数,缴费金额,挂车车牌, 挂车吨位, opdate, worker,effective,remarks) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
            sql_str2=id, zdname,dwmc,zzxm,cllb,clxh,clpz,dw,bz,cs,je,gcpz,gcdw,opdate,setworker.worker,effective,remarks
            self.sav=SaveNewData_py()
             #插入 worker表数据！
            if not self.sav.save_data(sql_str1, *sql_str2):
                self.msg(1, "error!", "更新  work  表不成功请与管理员联系！")
                return
            #更新work_id，id+1
            if not set_workid():
                msg(1, "error!", "更新  work_id  表不成功请与管理员联系！")
                return
            #数据处理完成，是否马上打印
            #if self.msg(2, "成功", '保存数据成功，是否打印？')==QMessageBox.Yes:
            tstr=[]
            opdate=opdate.split()
            for i in opdate[0].split('-'):
                tstr.append(i)
            opdate=tstr[0] + "年" + tstr[1] +'月'+tstr[2] +'日'
            #开始打印
            prt=Printer()
            prt.fastPrt(clpz,opdate, gcpz)
#            print("print table!")
            #清空界面
            self.clear_txt()
    #修改录入信息，update 修改数据模块！除id,opdate,worker,effective,remarks 之外的数据都可以修改
    def modify_save_data(self):
        if self.txt_id.text()=="":
            QMessageBox.information(self, "错误", '新数据,请选择 缴费', QMessageBox.Yes)
            return
        if self.verify_data():
            zdname=self.comb_zd.currentText()
            dwmc=self.txt_mc.text()
            zzxm=self.txt_name.text()
            cllb=self.txt_lb.text()
            clxh=self.txt_xh.text()
            clpz=self.txt_pz.text()
            dw=self.txt_dw.text()
            bz=int(self.txt_bz.text())
            je=int(self.txt_je.text())
            cs=int(self.txt_cs.text())
            gcpz=self.txt_gcpz.text()
            gcdw=self.txt_gcdw.text()
            #从隐藏控件获得数据，不可更新！！！！
            id=self.txt_id.text()
            opdate=self.oldtime
            opdate=self.txt_time.text()
            #where id= 更新12个字段
            sql_str1="update work set 站点=?, 单位名称=?, 车主姓名=?, 车辆类别=?, 车辆型号=?,车牌照号=?,吨位座位=?,缴费标准=?,通行次数=?,缴费金额=?,挂车车牌=?, 挂车吨位=? where id=?"
            sql_str2=zdname,dwmc,zzxm,cllb,clxh,clpz,dw,bz,cs,je,gcpz,gcdw, id
            #update 修改数据模块！除id,opdate,worker,effective,remarks 之外的数据都可以修改
            self.sav=SaveNewData_py()
            if self.sav.save_data(sql_str1, *sql_str2):
#                if self.msg(2, "成功", '保存数据成功，是否打印？')==QMessageBox.Yes:
                tstr=[]
                opdate=opdate.split()
                for i in opdate[0].split('-'):
                    tstr.append(i)
                opdate=tstr[0] + "年" + tstr[1] +'月'+tstr[2] +'日'
                #开始打印
                prt=Printer()
                prt.fastPrt(clpz,opdate, gcpz)
#                    prt.callfastPrt()
                self.clear_txt()
            else:
                self.msg(1,"发生错误！","无法保存数据！请与管理员联系！")
                return
    def del_data(self):
        if self.txt_id.text()=='':
            self.msg(1, "删除错误！", '只能删除已经录入的数据！\r\n该界面数据是新录入数据，如果想清空，请选择【清空界面】按键')
        else:
            if self.msg(2, "删除数据", "确定要删除" + self.txt_pz.text()+"的数据吗？")==QMessageBox.Yes:
                val=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                delete=SaveNewData_py()
                delete.save_data("insert into del_recd select * from work where id='"+self.txt_id.text()+"'" )
                delete=SaveNewData_py()
                delete.save_data("update  del_recd set remarks='{}' where id='{}'".format(val, self.txt_id.text()))
                delete=SaveNewData_py()
                delete.save_data("delete from work where id='"+self.txt_id.text()+"'")
                self.clear_txt()
   #自定义消息messageBox()
    def msg(self, Dialog_class, tit, message):

        if Dialog_class==1:   #录入不完整
            QMessageBox.warning(self, tit, message, QMessageBox.Yes)
            return
        if Dialog_class==2:   #选择提示
            return QMessageBox.warning(self, tit, message, QMessageBox.Yes|QMessageBox.No, QMessageBox.Yes) 

#class 自定义信号======================================
class Mysignal(QObject):
    set_data_signal = pyqtSignal()
#class 基本信息窗体初始化==================================
class InitWin_setInfo(QMainWindow,Ui_infoWin):
    def __init__(self):
        super(InitWin_setInfo,self).__init__()
        self.setupUi(self)

        self.tbv.setSelectionMode(QTableView.SingleSelection)
        self.tbv.setSelectionBehavior(QTableView.SelectRows)
        #self.tbv.setColumnHidden(id, True)
        self.tbv.resizeColumnsToContents()

        #定义infowindow 数据维护MENU信号
        self.tool_a.triggered.connect(self.addrow)
        self.tool_d.triggered.connect(self.delrow)
        self.tool_s.triggered.connect(self.savetb)
        self.tool_c.triggered.connect(self.close)

    def addrow(self):
        self.tmod.insertRows(self.tmod.rowCount(),1)
    def delrow(self):
        index = self.tbv.currentIndex()
        if not index.isValid():
            return
        # record = self.model.record(index.row())
        # category = record.value(CATEGORY)
        # desc = record.value(SHORTDESC)
        if (QMessageBox.question(self,"删除数据！","确定要删除这条数据吗？",QMessageBox.Yes|QMessageBox.No) ==QMessageBox.No):
            return
        self.tmod.removeRow(index.row())
        self.tmod.select()
    def savetb(self):
        self.tmod.submitAll()
        self.tmod.select()
    def formout(self):
        pass

    def openDb_table(self,tab_name):
        self.mod=modDb() #create model
        self.tmod=self.mod.createMod(tab_name)  #setup table name of model
        self.tbv.setColumnHidden(0, True)
        self.tbv.setModel(self.tmod)  # setup  model of tableview
#class 初始化选择时间窗口
class InitWin_seldt(QDialog,Ui_selectdate):
    def __init__(self):
        super(InitWin_seldt, self).__init__()
        self.flgname=''
        self.setupUi(self)
        self.Qdate.hide()
        self.t1.setText(time.strftime('%Y-%m-%d', time.localtime(time.time())))
        self.t2.setText(time.strftime('%Y-%m-%d', time.localtime(time.time())))
        self.Qdate.clicked.connect(self.settxt)
        self.bt1.clicked.connect(self.PrintYb)
        self.s2.clicked.connect(self.show_selectdate2)
        self.s1.clicked.connect(self.show_selectdate1)
        self.setWindowTitle("请选择月结日期")

    def show_selectdate1(self):
        self.Qdate.show()
        self.Qdate.move(0, 0)
        self.flgname='s1'
    def show_selectdate2(self):
        self.Qdate.show()
        self.Qdate.move(self.s1.x(), 0)
        self.flgname='s2'
    def settxt(self):
        if self.flgname=='s1':

            self.t1.setText(self.Qdate.selectedDate().toString("yyyy-MM-dd"))
            self.Qdate.hide()
        else:
            self.t2.setText(self.Qdate.selectedDate().toString("yyyy-MM-dd"))
            self.Qdate.hide()
# 月报表窗体初始化 
    def PrintYb(self):
        try:
            if self.t1.text()!='' and self.t2.text()!='' and time.strptime(self.t1.text(), '%Y-%m-%d') and time.strptime(self.t2.text(), '%Y-%m-%d'):
                self.prtybb=Printer()
                #sqlstr, tit_pt,subtit_pt, date_pt,colsize,ltop_pt,rbot_pt
                self.title=' 月 结 报 表 '
                self.subtit= self.t1.text() + ' 至 ' + self.t2.text() + ' '*50
                self.datept="制表时间:" + time.strftime('%Y-%m-%d',time.localtime(time.time()))+ "     制表人:" + setworker.worker
                self.colsize=[8, 10, 7, 7, 8]
                self.ltop=[1, 1]
                self.rbot=[1, 1]

                str1='''create table tmp_worker_yjb as select worker  as 收款人1,worker  as 收款人,车辆类别,缴费金额 as 收费项目,count(缴费金额) as 项目笔数,(缴费金额*count(缴费金额)) as 金额合计 from work where 0=1 group by worker,缴费金额 order by worker,缴费金额'''
                self.selDat=createnewtb('tmp_worker_yjb',str1)
                str1='''select worker  as 收款人1,worker  as 收款人,车辆类别,缴费金额 as 收费项目,count(缴费金额) as 项目笔数,(缴费金额*count(缴费金额)) as 金额合计  from work where date(opdate)>=? and date(opdate)<=? group by worker,缴费金额 order by worker,缴费金额 desc'''
                str2=self.t1.text(),self.t2.text()
                self.selDat=Selectdata_py()
                self.tit, self.rec=self.selDat.select_data(str1,*str2)
                if len(self.rec)==0:
                    QMessageBox.information(self, "查询失败", '没有找到此时间段数据,请更改时间段再试',QMessageBox.Yes)
                    return
                str1="insert into tmp_worker_yjb " + str1

                self.updtDt=SaveNewData_py()
                if self.updtDt.save_data(str1,*str2):
                    str2='select 收款人1,收款人,count(车辆类别) as 类别,count(车辆类别) as 项目,sum(项目笔数)as 笔数 ,sum(金额合计)as 金额 from tmp_worker_yjb group by 收款人'
                    self.selDat=Selectdata_py()
                    self.tit, self.rec=self.selDat.select_data(str2)
                    str2='insert into tmp_worker_yjb (收款人1,收款人,车辆类别,收费项目,项目笔数,金额合计) values (?,?,?,?,?,?)'
                    sumhj=[]
                    for rectdate in self.rec:
                        if len(sumhj)==0:
                            sumhj=[rectdate[4],rectdate[5]]
                        else:
                            sumhj=[sumhj[0]+rectdate[4],sumhj[1]+rectdate[5]]
                        rectdate=list(rectdate)
                        rectdate[1]= rectdate[1]+'(小计):'
                        rectdate=tuple(rectdate)
                        self.updtDt=SaveNewData_py()
                        self.updtDt.save_data(str2, *rectdate)
                    #sumhj=[self.rec[0][3]+self.rec[1][3], self.rec[0][4]+self.rec[1][4]]
                    sumhj.insert(0, '总 计:')
                    sumhj.insert(0, 'z')
                    sumhj=tuple(sumhj)
                    str2='insert into tmp_worker_yjb (收款人1,收款人,项目笔数,金额合计) values (?,?,?,?)'

                    self.updtDt=SaveNewData_py()
                    self.updtDt.save_data(str2,*sumhj)

                else:
                    QMessageBox(self, "查询失败", '数据更新出错,请联系管理员',QMessageBox.Yes)

                self.sqlstr_yb="SELECT 收款人,车辆类别,收费项目,项目笔数,金额合计 FROM tmp_worker_yjb"
                self.prtybb.tablePt(self.sqlstr_yb,self.title,self.subtit,self.datept,self.colsize,self.ltop,self.rbot)

                self.close()
            else:
                QMessageBox.warning(self, '错误', '时间选择不正确,请选择正确开始,结束时间!', QMessageBox.Yes)
                self.t1.setFocus()
                return
        except:
            QMessageBox.warning(self, '错误', '时间选择不正确,请选择正确开始,结束时间!', QMessageBox.Yes)


