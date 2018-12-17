import sys
import sqlite3 as sql
from PyQt5.QtSql import (QSqlDatabase, QSqlQuery, QSqlTableModel,QSqlQueryModel)
from PyQt5.QtCore import *
import pyodbc
import os
import shutil
#from callmainwin import *

dataBaseFilePath=r".\data\Mydb.db"
path2=r'd:\\app\\Mydb.db'
#拷贝数据库到指定目录
def backupSqlite(dirname):
    shutil.copyfile(dataBaseFilePath,dirname)
#    conn = sql.connect(dataBaseFilePath)
#    #with open(dirname,'w') as f:
#    with open(dirname,'wb+') as f:
#        for line in conn.iterdump():
#            data = line + '\n'
#            data = data.encode("utf-8")
#            print(data)
#            f.write(data)
def setDbPath(dirname):
    if dirname!='':
        con=sql.connect(dataBaseFilePath)
        cursor=con.cursor()
        cursor.execute('select * from dbpath')
        rec=cursor.fetchall()
        if len(rec)==0:
            str1="insert into dbpath (asynpath) values('" + dirname + "')"
            cursor.execute(str1)
            con.commit()
        else:
            cursor.execute("update dbpath set asynpath='%s'"%dirname)
            con.commit()
    else:
        print('asynpath is none')
    cursor.close()
    con.close()
    
#新建线程同步表数据  tbTotbUpdate
class UpdateTb():
    def __init__(self):
        self.timer=QTimer()
        self.th1=ThreadUp()
        self.timer.timeout.connect(self.th1.start)
    def beginUp(self):
        self.timer.start(60000) #更新频率默认1分钟
class ThreadUp(QThread):
    def __init__(self):
        super(ThreadUp,self).__init__()
    def run(self):
        tbTotbUpdate()
        
#更新两个表里的数据同步
def tbTotbUpdate():
    try:
        row1=0; row2=0
        conn=sql.connect(dataBaseFilePath)
        cur=conn.cursor()
        str1="select asynpath from dbpath"
        cur.execute(str1)
        rec1=cur.fetchall()
        if len(rec1)==0:
            path=path2
        else:
            path=rec1[0][0]
        #附加异地库
        #path='c:\\Mydb.db'
        cur.execute("ATTACH DATABASE '" + path + "' as other")
        #确定库里有没有表,如果有删除后重建临时表
        str1="select count(*) from sqlite_master where type='table' and name='{}'".format('tmp_trans')
        str2="select count(*) from other.sqlite_master where type='table' and name='{}'".format('tmp_trans')
        cur.execute(str1)
        rec1=cur.fetchall()
        cur.execute(str2)
        rec2=cur.fetchall()
        if rec1[0][0]>0:
            cur.execute("drop table tmp_trans")
        if rec2[0][0]>0:
            cur.execute("drop table other.tmp_trans")
            
        str1='create table tmp_trans as select * from  work where effective=0'
        str2='create table other.tmp_trans as select * from  other.work where effective=0'
        cur.execute(str1)
        cur.execute(str2)
        #error !!!!!
        str1='update work set effective=1 where effective=0'
        str2='update other.work set effective=1 where effective=0'
        cur.execute(str1)
        print(cur.rowcount)
        cur.execute(str2)
        print(cur.rowcount)
        str1='update tmp_trans set effective=1'
        str2='update other.tmp_trans set effective=1'
        cur.execute(str1)
        cur.execute(str2)
        #error222222222222
        str1='insert into other.work  select * from tmp_trans' #导出
        str2='insert into work select * from other.tmp_trans'  #导入
        cur.execute(str1)
        row1=cur.rowcount
        cur.execute(str2)
        row2=cur.rowcount
        
        str1='update  work set effective=1' 
        str2='update  other.work set effective=1'
        cur.execute(str1)
        cur.execute(str2)
        
        print('update success!! out:', row1,'in:', row2)
        conn.commit()
    except:
        conn.rollback()
        row1="数据库同步出错!0"
        row2='数据库同步出错!0'
#        QMessageBox.warning(self, "error", "更新没有成功!请联系管理员", QMessageBox.Yes)
    finally:
        cur.close()
        conn.close()
        return row1, row2
        
class setworker(object):
    worker=""
    getdatebegin=''
    getdateend=''
def openodbcbase():
    # Database connection string.
    #db_conn_str = Driver=SQLite3 ODBC Driver;Database=H:\dly\FloodForeCastV2\Data\TzxGIS.db;LongNames=0;Timeout=100;NoTXN=0;SyncPragma=NORMAL;StepAPI=0;
    #db_conn_str = driver=sql server;server=192.168.0.112;uid=sa;pwd=123;database=TzxGIS
    db_conn_str='DRIVER=Devart ODBC Driver for SQLite;Database=' + dataBaseFilePath
    try:
        cnxn = pyodbc.connect(db_conn_str)
        cursor  =  cnxn.cursor()
        cursor.execute('select * from worker')
        result=cursor.fetchall()
        print(result)
    except:
        print("odbc open error")
    finally:
        pass
#    if not db.open():
#        QMessageBox.warning(self, "数据库打开错误", "database open error!", QMessageBox.Yes)
#        sys.exit(1)
#        
class createnewtb():
    def __init__(self, tabName, sqlStr, *argv):
        self.argv=argv
        self.conn=sql.connect(dataBaseFilePath)
        self.cur=self.conn.cursor()
        self.tabName=tabName
        self.sqlStr=sqlStr
        self.existtb()
        self.createtb()
    def existtb(self):
        if len(self.argv)==0:
            str1="select count(*) from sqlite_master where type='table' and name='{}'".format(self.tabName)
        else:
            str1=self.argv[0].format(self.tabName)
        self.cur.execute(str1)
        self.rec=self.cur.fetchall()
        if self.rec[0][0]>0:
            self.cur.execute("drop table "+ self.tabName)
    def createtb(self):
        self.cur.execute(self.sqlStr)
        
#QtSql 打开pyqt数据库连接
def opendatabase():
    filename =dataBaseFilePath
    #create = not QFile.exists(filename)
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName(filename)
    if not db.open():
        QMessageBox.warning(self, "数据库打开错误", "database open error!", QMessageBox.Yes)
        sys.exit(1)
        
# 在新缴费保存时，获取当前id,work表的 cpu+id 为新id格式，最后 return id到 save_data
# id的工作方式为：把当前的work表里cpu+id格式用在当前新缴费里，当期缴费完成由set_workid()提前更新work表里id，id=id+1，为下一单做准备
def get_workid():
    getid=Selectdata_py()
    tit, record=getid.select_data("select * from work_id")
    nowid=int(record[0][0])
    id=record[0][1] + str(record[0][0])
    if len(id)==0:
        msg(1, "error", "从work_id中获取id失败！")
        exit(1)
    return id
    
#存储完毕更新ID  work  id
def set_workid():
    getid=SaveNewData_qt()
    if getid.save("update work_id set id=id+1"):
        print('更新成功')
        return True
    else:
        return False


class Db(object):
    
    def __init__(self,connstr):
        self.con=sql.connect(connstr)
    def open_sql(self,strsql):
        cur=self.con.cursor()
        cur.execute(strsql)
        resultList=cur.fetchall()
        titleList=[rec[0] for rec in cur.description]
        return titleList,resultList
        
#QtSql  表格模型
class modDb(object):
    
    def __init__(self):
        opendatabase()
    def createMod(self,tabName):
        self.TbMod=QSqlTableModel()
        self.TbMod.setTable(tabName)
        self.TbMod.select()
        print("modDb:", self.TbMod)
        return self.TbMod


#QtSql  查询模型
class modQy(object):
    
    def __init__(self):
        opendatabase()
    def createMod(self,sqlStr):
        self.QyMod=QSqlQueryModel()
        self.QyMod.setQuery(sqlStr)
        print("modQy:", self.QyMod)
        return self.QyMod
        


#Qsql Query方式保存新数据到数据库
class SaveNewData_qt(object):
    
    def __init__(self):
        opendatabase()
    def save(self, sqlStr):
        self.myqury=QSqlQuery()
        self.myqury.exec(sqlStr)
        return True




#python 添加、删除、修改数据 。 添加时，execute() 添加一条记录.
#                                 executemany() 添加一个列表list=[(1,'张三',20，'唐山人'),
#                                                               (2,'李四',30，'乐亭人'),
#                                                               (3,'王五',35，'保定人')]
class SaveNewData_py(object):
    def __init__(self):
        self.conn=sql.connect(dataBaseFilePath)
        self.cur=self.conn.cursor()
        self.success=False
    #参数格式为：sqlstr 完整insert into SQL语句，*argv SQL语句中？站位付的值，发送类型为  *元祖格式
    def save_data(self, sqlstr, *argv):
        try:            
            if len(argv)==0:
                self.cur.execute(sqlstr)
            else:
                self.cur.execute(sqlstr, argv)
            #set_workid()
            self.success=True
            print("changed rowcount:{}".format(self.cur.rowcount))
            self.conn.commit()
            
        except:
            self.success=False
            self.conn.rollbak()
            
            print("changed rowcount:{}".format(self.cur.rowcount), "rollbak")
        finally:
            self.cur.close()
            self.conn.close()
            return self.success

            
#python 查找 fetchall() ,fetchone()
class Selectdata_py(object):
    def __init__(self):
        self.conn=sql.connect(dataBaseFilePath)
        self.cur=self.conn.cursor()
    def select_data(self, sqlstr, *arg):
        try:
            if len(arg) ==0 :
                self.cur.execute(sqlstr)
            else:
                self.cur.execute(sqlstr , arg)
            self.recordset=self.cur.fetchall()
            self.titleList=[recordCol[0] for recordCol in self.cur.description]
            return self.titleList, self.recordset
            print("title list :{0}  rowcount:{1}".format(self.titleList, self.recordset.rowcount()))
        except:
            print("select error!")
        finally:
            self.cur.close()
            self.conn.close()
            
            
#openodbcbase()
#tbTotbUpdate()
        
        
        
        
        
        
        
            
#python 删除,改  
#class Modifydata_py():
#    def __init__(self):
#        self.conn=sql.connect(dataBaseFilePath)
#        self.cur=self.conn.cursor()
#        self.success=False
#    def modify_data(self, sqlstr, *argv):
#        try:
#            self.cur.execute(sqlstr)
#            self.conn.commit()
#            
#            print("delete or modify rowcount:{}".format(self.cur.rowcount))
#            self.success=Ture
#        except:
#            self.success=False
#            self.conn.rollbak()
#            print("delete rowcount:{}".format(self.cur.rowcount), "rollbak")
#            
#        finally:
#            self.cur.close()
#            self.conn.close()
#            return success            
            
#        '''     
#
#
#    def closeDb():
#            try:
#                cur.close()
#                db.commit()
#                db.close()
#            except:
#                self.msg("无法关闭数据库"+ filename)
#                raise
#
#
#
#
#        def initDb(self,filename):
#        if  filename!='':
#            filename='./data/Mydb.db'
#            self.msg(filename)
#            try:
#                db=sql.connect(filename)
#                cur=db.cursor()
#                cur.execute("select * from user")
#                if len(cur.fetchall())==0:
#                    print('error')
#                else:
#                    print('ok')
#                # resultlist=cur.fetchall()
#                # print(resultlist)
#                # titlist=[tit[0] for tit in cur.description]
#                # print(titlist)
#            except:
#                self.msg("无法连接数据库"+ filename)
#                cur=None
#                raise
#    '''
