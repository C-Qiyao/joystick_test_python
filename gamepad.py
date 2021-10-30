import sys
import pygame
import time
import serial
import serial.tools.list_ports
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

        self.port_list = list(serial.tools.list_ports.comports())# 获取当前可用串口列表，serial模块函数
        if len(self.port_list) == 0:# 判断串口列表是否为空
            self.message.insertPlainText("未找到可用串口")# 弹出错误警告框，自建函数
        else:
            for i in range(0,len(self.port_list)):# 遍历可用串口列表
                self.comboBox_SerialSel.addItem(self.port_list[i][0])# 将可用串口添加至comboBox（复选框）控件
                # 串口参数设置
        self.serial = serial.Serial(timeout=1)  # 实例化串口类
        self.serial.baudrate = 38400  # 设置波特率（这里使用的是stc89c52）

        self.pushButton_SerialCon.clicked.connect(self.connectSerial)#连接串口按钮
        self.pushButton.clicked.connect(self.connectgamepad)#连接串口按钮
        self.disconnect.clicked.connect(self.discon)
        self.pushButton_stop.clicked.connect(self.stop)
        self.pushButton_start.clicked.connect(self.startread)


        pygame.init()
        pygame.joystick.init()
        self.done=False
        self.proData = threading.Thread(target=self.processData)#processdata设置单独线程
        self.proData.setDaemon(True)#设置为后台线程，关闭一起关闭
        self.show()
        
        

        self.message.insertPlainText('======CQY-手柄控制软件V1.0====\n') 


        self.xboxint=0
        self.serial.is_open=0

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
        self.stopflag=0
        self.quit=0
        self.startflag=0
        self.xboxint=1
        


    
    def processData(self):
        while self.quit==0:
            if self.done==False:
               for event in pygame.event.get(): # User did something
                  if event.type == pygame.QUIT: # If user clicked close
                   self.done=True
               str1='x5: '+str(int(self.xbox.get_axis(5)*100))+' x4:  '+str(int(self.xbox.get_axis(4)*100))+'  x3:  '+str(int(self.xbox.get_axis(3)*100))+'  x2:  '+str(int(self.xbox.get_axis(2)*100))+'  x1:  '+str(int(self.xbox.get_axis(1)*100))
               print(str1)
               if self.serial.is_open :
                    self.serial.write(bytes(str1+'\n',encoding='utf-8'))
            time.sleep(0.05)

    def discon(self):
        self.done=True
        self.quit=1
        self.xbox.quit()
        self.message.insertPlainText('已卸载手柄，请退出软件')

    def stop(self):
        if self.stopflag==0:
            self.done=True
            self.stopflag=1
            self.pushButton_stop.setText("继续读取")
        else:
            self.pushButton_stop.setText("暂停读取")
            self.done=False
            self.stopflag=0

    def startread(self):
        if self.xboxint==1:
         self.done=False
         self.message.insertPlainText('开始读取，请按下手柄按键\n')
         
         for num in range(0,50):
             i=int(self.xbox.get_axis(5)*100)
             if i==-100:
                 if self.proData.is_alive()==False:
                     self.proData.start()#线程启动
                 self.startflag=1
                 break
             time.sleep(0.1)       
         if self.startflag==1:
             self.message.insertPlainText('读取线程启动\n')
        else:
            self.message.insertPlainText('请先连接手柄\n')

  
    def connectSerial(self):
        # 按键‘连接’响应
        if self.pushButton_SerialCon.text()=='连接串口':# 判断当前按键文字是否为连接
            self.serial.port = self.comboBox_SerialSel.currentText() # 获取复选框中的串口名字
            try:#开启串口
                self.serial.open()# 打开串口
                if self.serial.is_open:# 判断串口是否打开
                    self.pushButton_SerialCon.setText('关闭串口')# 将按键文字设置为断开\
                    self.message.insertPlainText('串口打开成功')
                    self.serial.is_open=1

                else:
                    self.message.insertPlainText('串口连接失败')
            except Exception as err:
                self.message.insertPlainText("串口连接失败,请选择未占用串口")
        else:#关闭串口
            try:
                self.serial.write(b"Wait\r\n")# 向串口发送等待指令，用于停止单片机数据发送
                self.enableRevData = False# 禁止串口接收数据
                time.sleep(1)
                self.serial.flushInput()# 清除串口缓存
                self.serial.close()# 关闭串口
                if not self.serial.is_open:# 判断串口关闭状态
                    self.pushButton_SerialCon.setText('连接串口')
                    self.message.insertPlainText('串口关闭成功')
                    self.serial.is_open=0
                else:
                    self.message.insertPlainText('串口关闭失败')
            except Exception as err:
                self.message.insertPlainText("串口关闭失败")



                            
           
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
