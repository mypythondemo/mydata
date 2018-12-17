#!/usr/bin/env python3
#!格式表格打印模块,MICKEY 2018.11.28
import math
import sys
import html


from PyQt5.QtPrintSupport import QPrinter,QPrintDialog,  QPrintPreviewDialog
from PyQt5.QtCore import (QDate, QRectF, Qt)
from PyQt5.QtWidgets import (QApplication,QDialog, QWidget,QMainWindow,  
        QHBoxLayout,QVBoxLayout, QAction)
from PyQt5.QtGui import (QFont,QFontMetrics,QPainter,QTextCharFormat,
                         QTextCursor, QTextDocument, QTextFormat,
                         QTextOption, QTextTableFormat,
                         QPixmap,QTextBlockFormat, QPen)
from optDb import *

class Printer(QMainWindow):
    def __init__(self):
        super(Printer, self).__init__()
        self.setWindowTitle("开始打印")
        self.resize(1024, 700)
        self.createMenus()
        self.Pt_data=[]
        self.Pt_tit=[]
    def createMenus(self):  # 创建动作一 
        pass
#        self.printAction1 = QAction(self.tr("打印无预"), self)  
#        self.printAction1.triggered.connect(self.noview_pt)  # 创建动作二  
#        self.printAction2 = QAction(self.tr("打印有预"), self)  
#        self.printAction2.triggered.connect(self.tablePt)  # 创建动作三  
#        self.printAction3 = QAction(self.tr("直接打印"), self)  
#        self.printAction3.triggered.connect(self.fast_pt)  # 创建菜单，添加动作  fastPrt
#        self.printAction3.triggered.connect(self.callfastPrt)  # 创建菜单，添加动作  fastPrt
#        self.printMenu = self.menuBar().addMenu(self.tr("打印"))  
#        self.printMenu.addAction(self.printAction1)  
#        self.printMenu.addAction(self.printAction2)  
#        self.printMenu.addAction(self.printAction3)
    #def paintEvent(self, e):
        
    def setdat(self, sql_str):
        self.cn=Selectdata_py()
        tit, recordset=self.cn.select_data(sql_str)
        #global self.Pt_data, self.Pt_tit
        self.Pt_data=recordset
        self.Pt_tit=tit
    def noview_pt(self):
        printer =QPrinter(QPrinter.HighResolution)
        printer.setFontEmbeddingEnabled(True)
        dialog = QPrintDialog(printer, self)
        if not dialog.exec_():
            return
        self.paintpic(printer)
    def callfastPrt(self):
#        prt =QPrinter(QPrinter.HighResolution)
#        prt.setFontEmbeddingEnabled(True)
#        dialog = QPrintDialog(prt, self)
#        if not dialog.exec_():
#            return
#        #self.paintpic(printer)
#        self.fastPrt(prt,'冀B668HJ', '2018年12月1日', "冀B999HJ")
        
        #self.fastPrt('冀B668HJ', '2018年12月1日')
#    def fast_pt(self):
#        #pass
        prt =QPrinter(QPrinter.HighResolution)
        prt.setFontEmbeddingEnabled(True)
        prev=QPrintPreviewDialog(prt)
        prev.paintRequested.connect(self.fastPrt)
        prev.exec_()
        
    def tablePt(self,sqlstr, tit_pt,subtit_pt, date_pt,colsize,ltop_pt,rbot_pt):#preview print

        self.sqlstr=sqlstr
        self.tit_pt=tit_pt     #主标题
        self.subtit_pt=subtit_pt    #子标题
        self.date_pt=date_pt        #打印日期
        self.colsize=colsize        #每列宽
        self.ltop_pt=ltop_pt     #左.上点坐标,及左边界,上边界
        self.rbot_pt=rbot_pt    #右.下点坐标,及右边界,下边界
        self.setdat(self.sqlstr) #取数据
        
#自定义表头,表格内文字  测试用

#        self.tit_font_class=tit_font_class
#        self.tb_font_class=tb_font_class

# ===============debug printer =============
#    def tablePt(self):    
#        
#        self.sqlstr="select id,单位名称,车主姓名,车牌照号,车辆类别,缴费金额 from work"
#        self.setdat(self.sqlstr)
#        self.tit_pt='左.上点坐标,及左边界,上边界'   #主标题
#        self.subtit_pt='子标题'    #子标题
#        self.date_pt='date_pt'        #打印日期
#        self.colsize=[5, 8, 6, 8, 6, 9]        #每列宽
#        self.ltop_pt=[3, 5,]     #左.上点坐标,及左边界,上边界
#        self.rbot_pt=[4, 3]    #右.下点坐标,及右边界,下边界
        
        
        printer =QPrinter(QPrinter.HighResolution)
        printer.setFontEmbeddingEnabled(True)
        preview =QPrintPreviewDialog(printer)
        preview.paintRequested.connect(self.paintpic)
        preview.resize(1024, 720)
        preview.exec_()
    #打印月票
    def fastPrt(self, zpz, ptdate, *argv):
#    def fastPrt(self,prt):
        prt =QPrinter(QPrinter.HighResolution)
        prt.pageRect
        prt.setFontEmbeddingEnabled(True)
        dialog = QPrintDialog(prt, self)
        if not dialog.exec_():
            return
#        zpz='冀B668HJ' 
#        ptdate='2018年12月1日'
#        argv=("冀B999HJ挂", )
        qp=QPainter(prt)
        ratio=23.62626
        small=35
        big=135
        qp.begin(self)
        fastfont=QFont('宋体', 20) #小字
        fastfont.setBold(True)
        
        bigft=QFont('宋体', 80)     #大字
        bigft.setBold(True)
        bigft.setItalic(True)
        qp.setFont(fastfont)
        fastPen=QPen(Qt.black)
        bigPen=QPen(Qt.black)
        pageRect =prt.pageRect()
        #========================左侧
        qp.setPen(fastPen)
        qp.drawText(190, 670, zpz)  #小字主车
        if len(argv)!=0:
            qp.drawText(190, 800,argv[0])  #小字挂车
            
        qp.setFont(QFont('宋体', 20))
        qp.drawText(190, 940, ptdate)  #时间1
        #========================右侧
        qp.setFont(bigft)
        qp.drawText(870, 660, zpz)       #打字主车
        if len(argv)!=0:
            qp.drawText(870, 890, argv[0])  #打字挂车
            
        qp.setFont(QFont('宋体', 22))
        qp.drawText(1400, 1000, ptdate)    #时间2
        
        qp.end()
        qp.restore()
        #self.print(self.prt)
        #self.prt.printer()
        #qp.restore()
        #paperect=prt.pageRect()
#        print(paperect)
    def paintpic(self, printer):   #,tb_font_class,tit_font_class):
    #def paintpic(self, printer,):

        
        p=QPainter(printer)
#        tb_font_class=QFont("宋体, 12")
#        tit_font_class=QFont("宋体, 14")
        #tit_font.setPixelSize(18)
        pt_font = QFont("宋体", 18)
        tb_font = QFont("宋体", 12)
        pt_font.setBold(True)
        p.setFont(pt_font)   #setup font #####################
        p.setPen(QPen(Qt.black, 2))
        
        fm = QFontMetrics(tb_font)      #表内文字范围
        titFm= QFontMetrics(pt_font)    #标题字范围
        
        #pen=QPen(Qt.black, 8)
        
        #ft_h=fm.height()*10            #字高               #这个×10??????
        ft_h=fm.height()*2            #字高               #这个×10??????
        
        #tit_font_h=titFm.height()*10   #标题字高    #这个×10??????
        tit_font_h=titFm.height()*2   #标题字高    #这个×10??????
        
        #print(ft_h, tit_font_h)
        #ft_w=fm.width()     #字宽
        tb_h=ft_h        #行高
        print(tb_h)
        avg_tb_ft=(tb_h-ft_h)/2  #(行高-字高)/2
        
        
        #遍历传入列宽列表,计算出各个列打印宽度写入列表
        row_with=[]
        for linesize in self.colsize:
            row_with.append(linesize*30)
            
        #打印页面范围,
        pageRect = printer.pageRect()   #打印机纸张大小
        l_x=self.ltop_pt[0]*100         #起始x坐标
        tit_y=self.ltop_pt[1]*100         #打印起始y坐标
        r_x=pageRect.width()-self.rbot_pt[0]*100  #结束x坐标    
        r_y=pageRect.height()-self.rbot_pt[1]*100 #结束y坐标
        
        begin_tab=tit_y+tit_font_h+ft_h*2+tb_h    #表格上为主标题预留空位.(ft_font)+付标题(tit_font)+空一行+user时间行)+空一行+列表头预留格位.
        
        l_y=begin_tab
        #print('lly', l_y)
        #每页多少行
        rowperpage=int((r_y-l_y)//tb_h )   
        #计算表格总页数
        tb_row=len(self.Pt_data)  #打印数据一共多少行
        tb_col=len(self.Pt_tit)   #打印数据一共多少列
        #一共需要几页
        if tb_row%rowperpage>0:
            sumpage=(tb_row//rowperpage)+1 #有余数说明超页,则页数+1
        else:
            sumpage=(tb_row//rowperpage)   #整除,
        beginindex=0
        page=0   #页计数器
        k=0      #记录打印完当期页时,下一页面的开始行数 
        #开始制表
        p.begin(self)
        while 1:    #页数循环
            #表头
            begin_y=tit_y
            titx=(pageRect.width()-titFm.width(self.tit_pt)*5)/2
            subtx=(pageRect.width()-fm.width(self.subtit_pt))/2
            
            p.setFont(pt_font)   #setup font #####################
            #p.setPen(QPen(Qt.black, 8))
            
            p.drawText(titx, begin_y, self.tit_pt)  #主标题
            p.setFont(tb_font)
            begin_y+=+ft_h  #1
            p.drawText(subtx, begin_y, self.subtit_pt) #副标题
            begin_y+=ft_h*2 #3
            p.drawText(l_x, begin_y,self.date_pt)  #日期等其他内容
            begin_y+=tb_h  #4
            print("x:", l_x, "y:",  begin_y)
            
            #开始制表格和数据
            page+=1
            if rowperpage>tb_row:   #如果开始打印数据不足一页,则取tb_row,数据行数
                endindex=tb_row     #终点取整体记录
            else:
                endindex=page*rowperpage #整页的,行数乘以页数
            
            x=l_x  #输出开始X坐标
            y=l_y  #输出开始y坐标
            t_x=l_x #输出列标题开始X坐标
            
            print('第',page,'页', y)
            for i, linstr in enumerate(self.Pt_data[beginindex:endindex]):    #打印行循环
                for j in range(tb_col):   #打印列,tb_col:列数
                    #制作表格
                    p.drawRect(x, y, row_with[j], tb_h)
                    #break
                    #往表格填入数据
                    p.drawText(QRectF(x, y,row_with[j],tb_h),Qt.AlignCenter,str(linstr[j]))
                    if x+row_with[j]>r_x:  #如果列宽大于输出范围r_x,报错
                        print('报表宽度大于纸张宽度,第'+ str(j)+'列')
                        
                    x+=row_with[j]   #光标位置右移动到同行的.下一列及下一个字段  行4:字段1,字段2,字段3
                #break
                y+=tb_h  #光标下移一行,位置为 y+单行表格高度
                x=l_x #一行结束,回到起始位置X,准备输出下一行
                p.end
                #break
            #一页表完成,若
            if page<sumpage:  #如当期页码小于总页码,添加新叶,继续制表
                tb_font.setBold(True)
                p.setFont(tb_font)
                for t in range(tb_col):   #每页表制作完,打印列标题,tb_col:列数
                    #制作表格
                    p.drawRect(t_x, l_y-tb_h, row_with[t], tb_h)  
                    #往表格填入列标题
                    p.drawText(QRectF(t_x, l_y-tb_h,row_with[t],tb_h),Qt.AlignCenter,str(self.Pt_tit[t]))
                    t_x+=row_with[t]
                tb_font.setBold(0)
                beginindex=endindex
                if (tb_row-endindex)<rowperpage:  #如果剩下的数据不足一页
                    endindex=tb_row      #取剩下的数据
                
                p.drawText(QRectF(x, y,pageRect.width(),tb_h),Qt.AlignCenter, ' '*14 + "第" + str(page) +"页 共" + str(sumpage) + "页")
                
                printer.newPage()  #生成新叶
            elif page==sumpage:             #当期页=总页码数,打印完成,退出制表
                tb_font.setBold(True)
                p.setFont(tb_font)
                for t in range(tb_col):   #每页表制作完,打印列标题,tb_col:列数
                    #制作表格
                    p.drawRect(t_x, l_y-tb_h, row_with[t], tb_h)  
                    #往表格填入列标题
                    p.drawText(QRectF(t_x, l_y-tb_h,row_with[t],tb_h),Qt.AlignCenter,str(self.Pt_tit[t]))
                    p.drawText(QRectF(x, y,pageRect.width(),tb_h),Qt.AlignCenter, ' '*14 + "第" + str(page) +"页 共" + str(sumpage) + "页")
                    t_x+=row_with[t]
                tb_font.setBold(0)
                beginindex=endindex
                if (tb_row-endindex)<rowperpage:  #如果剩下的数据不足一页
                    endindex=tb_row      #取剩下的数
            else:
                break
        p.end
        p.restore()
        
        #print(tb_row,tb_col)
        #p.setFont(QFont("Helvetica", 10))
        #p.drawLine(0, 0, 300, 300)
        #p.drawRect(0, 0, 20, 10)
        #p.drawRect(QRect(0, 0, 20, 10))
        
        
if __name__=='__main__':
    app=QApplication(sys.argv)
    demo=Printer()
    demo.show()
    sys.exit(app.exec_())
    
    
    
    
    
    
    
