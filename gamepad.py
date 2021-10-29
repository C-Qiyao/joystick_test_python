import sys
import pygame
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
        #在此输入connect链接
        self.show()

        self.pushButton.clicked.connect(self.connectgamepad)#连接串口按钮
    def connectgamepad(self):
        pygame.init()
        pygame.joystick.init()
        
        self.joystick_count = pygame.joystick.get_count()
        self.message.insertPlainText('获取手柄按键信息\n')
        
        print(self.joystick_count)
        self.message.insertPlainText('检测到手柄数量:')
        self.message.insertPlainText(str(self.joystick_count))
        self.message.insertPlainText("\n")
        if self.joystick_count==0:
            self.echo("请连接手柄")
        self.xbox = pygame.joystick.Joystick(0)
        self.xbox.init()
        print (self.xbox.get_numaxes())
        self.message.insertPlainText('检测到手柄轴:')
        self.message.insertPlainText(str(self.xbox.get_numaxes()))
        self.message.insertPlainText("\n")       
           
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
