# python_joystick

#### 介绍
基于pyQt5开发的手柄接收界面,目前针对Xbox one以及Xbox series系列手柄的摇杆功能开发
可用于手柄的摇杆测试以及手柄转串口发送的二次开发
![Image text](https://gitee.com/C-Qiyao/python_joystick/blob/master/running.png)
#### 软件架构
软件架构说明
1.  主体代码由python3完成编写
2.  Gui界面由qt生成
3.  绘图窗口由pyqtgraph创建
4.  手柄数据读取由pygame joystick完成

#### 使用说明

1.  连接上你的xbox手柄，打开gamepad.exe可执行文件
2.  正常情况下gui界面右侧绘图窗口开始运行
3.  选择连接手柄，出现当前手柄信息
4.  点击开始读取，随即按下手柄RT/LT键
5.  等待程序响应，若无曲线绘图则再次点击开始读取按钮
6.  附带串口发送按钮，可以选择串口号，将摇杆数据发送至串口以控制其他外围设备
7.  当前默认串口波特率为38400bps，手柄采样200级，约0.2s一次手柄摇杆采集，使用串口需注意模块的处理速度
#### 参与贡献

1.  提交代码 陈祺遥

#### 其余说明

1.  使用问题可联系开发者:
    QQ 1113938836 
    Email 1113938836@qq.com
