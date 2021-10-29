import sys
import pygame
import time
import threading  # 导入threading包
from io import BytesIO
from Ui_gamepad import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,QPushButton, QPlainTextEdit,QLabel,QMessageBox

class myclass():
    def __init__(self) -> None:
        pass
class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.connectgamepad)#连接串口按钮
        pygame.init()
        pygame.joystick.init()
        self.done=False
        self.proData = threading.Thread(target=self.processData)#processdata设置单独线程
        self.proData.setDaemon(True)#设置为后台线程，关闭一起关闭
        self.show()


    def connectgamepad(self):

        
        self.joystick_count = pygame.joystick.get_count()
        self.message.insertPlainText('获取手柄按键信息\n')
        
        print(self.joystick_count)
        self.message.insertPlainText('检测到手柄数量:')
        self.message.insertPlainText(str(self.joystick_count))
        self.message.insertPlainText("\n")
        if self.joystick_count==0:
            self.echo("请连接手柄")
        else:

             self.xbox = pygame.joystick.Joystick(0)
             self.xbox.init()
             print (self.xbox.get_numaxes())
             self.message.insertPlainText('检测到手名称:')   
             self.message.insertPlainText(self.xbox.get_name() )      
             self.message.insertPlainText("\n")      
             self.message.insertPlainText('检测到手柄轴:')
             self.message.insertPlainText(str(self.xbox.get_numaxes()))
             self.message.insertPlainText("\n") 
             self.proData.start()#线程启动
    
    def processData(self):
        while self.done==False:
          for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                self.done=True
          self.x_axis.setText(str(int(self.xbox.get_axis(5)*100)))
          time.sleep(0.1)


                            
           
    def echo(self,info):
        '''显示对话框返回值'''
        QMessageBox.information(self, "错误",info, QMessageBox.Yes)

if __name__ == "__main__":  # 主函数执行
    app = QApplication(sys.argv)
    globFont = QtGui.QFont()
    globFont.setFamily('Microsoft YaHei')
    globFont.setPointSize(10)
    app.setFont(globFont)
    MainUI = MainWindow()  # 将主界面定义为欢迎界面，程序运行至此处开始调用MainWindow()类
    sys.exit(app.exec_())  # 程序执行完毕后关闭
