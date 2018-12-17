import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon
import os, re  
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import uuid
from optDb import *
from callmainwin import MainForm

# execute command, and return the output  
#def execCmd(cmd):  
#    r = os.popen(cmd)  
#    text = r.read()  
#    r.close()  
#    return text  

# write "data" to file-filename  
def writeFile(filename, data):  
    f = open(filename, "w")  
    f.write(data)  
    f.close()  
    
# 获取计算机MAC地址和IP地址  
#def get_ip():
#    cmd = "ipconfig /all"  
#    result = execCmd(cmd)  
#    pat1 = "Physical Address[\. ]+: ([\w-]+)"
#    pat2 = "IP Address[\. ]+: ([\.\d]+)"  
#    MAC = re.findall(pat1, result)[0]       # 找到MAC  
#    IP = re.findall(pat2, result)[0]        # 找到IP  
#    print("MAC=%s, IP=%s" %(MAC, IP))

# 获取计算机MAC地址和IP地址  

def get_macID():
    ID=uuid.UUID(int = uuid.getnode()).hex[-12:][-4:]
    if ID!='':
        return ID
    print(ID)
def set_macID():
    getid=Selectdata_py()
    tit, record=getid.select_data("select * from work_id")
    
    if len(record)==0: #新机器表中无数据，输入 id=1,cpu=getid
        val=(1, get_macID())
        setid=SaveNewData_py()
        if not setid.save_data("insert into work_id (id,cpu) values (?,?)",*val):
            print("cpuid insert error!")
            exit(1)
        
    else:         #更新macID为当前机器 ，id不变
        val=(get_macID(), )
        setid=SaveNewData_py()
        if not setid.save_data("update work_id set cpu=?", *val):
            print("cpuid modify error!")

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        set_macID()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(386, 127)
        MainWindow.setWindowIcon(QIcon('logo.png'))
        MainWindow.setStyleSheet("background-image:url(Background.jpg)")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setGeometry(QtCore.QRect(250, 20, 100, 20))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 50, 100, 20))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(200, 24, 24, 12))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(200, 54, 24, 12))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 90, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 90, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralWidget)
        self.lineEdit.returnPressed.connect(self.lineEdit_2.setFocus)
        self.lineEdit_2.returnPressed.connect(self.word_get)
        
        self.pushButton.clicked.connect(self.word_get)
        self.pushButton_2.clicked.connect(MainWindow.close)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.lineEdit.setFocus()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "车辆信息管理"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "请输入帐号"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "请输入密码"))
        self.label.setText(_translate("MainWindow", "帐号"))
        self.label_2.setText(_translate("MainWindow", "密码"))
        self.pushButton.setText(_translate("MainWindow", "确定"))
        self.pushButton_2.setText(_translate("MainWindow", "取消"))
    
    def word_get(self):
        login_user = self.lineEdit.text()
        login_password = self.lineEdit_2.text()
        query="select * from user where 助记码='{0}' and 密码='{1}'"
        str=query.format(login_user,login_password)
        db=Db(Constr)
        tit,recd=db.open_sql(str)
        if len(recd)>0:
            setworker.worker=recd[0][1]
            
            #worker=recd[0][1]
            if setworker.worker=='管理员':
                MForm.action_R.setEnabled(True)  #人员
                MForm.action_N.setEnabled(True)   #初始化数据库
            MForm.show()
            Win.close()
        else:
            QMessageBox.warning(self,
                    "警告",
                    "用户名或密码错误！",
                    QMessageBox.Yes)
            self.lineEdit.setFocus()
            
if __name__ == "__main__":
    Constr=dataBaseFilePath
    #set_cpuID()
    app = QtWidgets.QApplication(sys.argv)
    #login窗体INIT.
    Win = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(Win)
    #主界面INIT。。。
    MForm = MainForm()
    #login窗体show
    Win.show()
    #print(Win)
    sys.exit(app.exec_())
