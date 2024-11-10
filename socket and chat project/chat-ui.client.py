import socket,threading
import time
import os

import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QListWidgetItem, QLineEdit, QPushButton, QCheckBox,QMessageBox
from PySide6.QtCore import Qt
from Ui_聊天界面 import Ui_Form

"""
from PySide6.QtWidgets import QApplication,QWidget,QVBoxLayout

from Ui_计算器 import Ui_Form
class Mywindow(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self) 
"""

class ChatWindow(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        
        self.setupUi(self) 
        self.setWindowTitle("聊天室")
        self.roomNumberLine=self.lineEdit_2
        self.nameLine=self.lineEdit_3
        self.checkNameButton=self.pushButton_2
        # 创建聊天区域
        self.chat_area = self.listWidget
        
        # 创建输入区域
        self.input_box = self.lineEdit
        self.send_button = self.pushButton
        # 连接信号和槽
        self.send_button.clicked.connect(self.send_message)
        self.checkNameButton.clicked.connect(self.enter)
        self.readLog()
        self.down.clicked.connect(lambda:self.chat_area.scrollToBottom())
        self.enter()
    chatLog=''
    clientList=[]
    socketTCP=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    name=''
    def readLog(self):
        try:
            with open('chatLog.txt','r',encoding="UTF-8") as f:
                self.chatLog=f.read()
        except Exception as e:
            with open('chatLog.txt','w',encoding="UTF-8") as f:
                pass
            return
            print(e)
        try:
            with open('name.txt','r',encoding="UTF-8") as f:
                self.name=f.read()
                self.nameLine.setText(self.name)
        except Exception as e:
            with open('name.txt','w',encoding="UTF-8") as f:
                pass
            print(e)
        for line in self.chatLog.splitlines():# 按行切分
            print(line)
            li=line.split('：')
            if li[0]=='我':
                item = QListWidgetItem()
                is_me=True
                if is_me:
                    item.setTextAlignment(Qt.AlignRight)  # 右对齐
                    item.setBackground(Qt.lightGray)  # 设置背景色
                else:
                    item.setTextAlignment(Qt.AlignLeft)  # 左对齐
                    item.setBackground(Qt.white)  # 设置背景色
                item.setText(li[1])
                # 添加到列表
                self.chat_area.addItem(item)
                self.chat_area.scrollToBottom()
            else:
                item = QListWidgetItem()
                is_me=False
                if is_me:
                    item.setTextAlignment(Qt.AlignRight)  # 右对齐
                    item.setBackground(Qt.lightGray)  # 设置背景色
                else:
                    item.setTextAlignment(Qt.AlignLeft)  # 左对齐
                    item.setBackground(Qt.white)  # 设置背景色
                item.setText(li[0]+' ：'+li[1])

                # 添加到列表
                self.chat_area.addItem(item)
                self.chat_area.scrollToBottom()


    mutex=threading.Lock()
    currentClientNum=0
    def otherPeopleMessageToList(self,datas):
        item = QListWidgetItem()
        print('new Line')
        is_me=False
        if is_me:
            item.setTextAlignment(Qt.AlignRight)  # 右对齐
            item.setBackground(Qt.lightGray)  # 设置背景色
        else:
            item.setTextAlignment(Qt.AlignLeft)  # 左对齐
            item.setBackground(Qt.white)  # 设置背景色
        item.setText(datas)
        # 添加到列表
        self.chat_area.addItem(item)
    isConnect=True
    def enter(self):
        #if self.nameLine.text()!='' and self.nameLine.text()!='':
        

        masterIP=self.roomNumberLine.text()
        masterIP='111.79.225.242'
        masterPort=8888
        connectServe=(masterIP,masterPort)
        try:
            self.socketTCP.connect(connectServe)
        except Exception as e:
            time.sleep(0.5)
            pass
        # message='this is a test messsage.'
        # self.socketTCP.send(message.encode('utf-8'))
        self.name=self.nameLine.text()
        self.isConnect=True
        print("new getMessage test")
        threading1=threading.Thread(target=self.getMessage)
        threading1.start()
    def getMessage(self):
        while True:
            print('before get a message')
            try:
                message=self.socketTCP.recv(1024)
            except Exception as e:
                print(e)
                time.sleep(0.5)
                continue
            message=message.decode('utf-8')
            messageList=list(message)
            try:
                if messageList[0]=='*':
                    messageList.pop(0)
                    print(messageList)
                    num=''
                    for a in messageList:
                        num+=a
                    self.label.setText('当前聊天室人数为：'+num)
                    
                    continue
            except Exception as e:
                print(e)
                continue
            self.chatLog+=message
            self.chatLog+='\n'
            print('get a message')
            print('********************')
            self.otherPeopleMessageToList(datas=message)
            num=0

    def closeEvent(self, event):
        # 在这里添加你想要执行的代码
        with open('chatLog.txt','w',encoding="UTF-8") as f:
            f.write(self.chatLog)
        with open('name.txt','w',encoding="UTF-8") as f:
            f.write(self.name)
        print("Window is about to close.")
        
        # 询问用户是否真的要关闭窗口
        reply = QMessageBox.question(self, '请问',
                                    "你确定要关闭窗口?", QMessageBox.Yes |
                                    QMessageBox.No, QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            # 如果用户选择是，则接受关闭事件
            event.accept()
        else:
            # 如果用户选择否，则忽略关闭事件
            event.ignore()

    def send_message(self):
        text = self.input_box.text()
        if text=='':
            return
        if self.isConnect:
            pass
        else:
            return
        self.chatLog=self.chatLog+'我'+'：'+text+'\n'
        # is_me = self.is_me_checkbox.isChecked()
        # 构造QListWidgetItem
        item = QListWidgetItem()
        is_me=True
        if is_me:
            item.setTextAlignment(Qt.AlignRight)  # 右对齐
            item.setBackground(Qt.lightGray)  # 设置背景色
            message=self.nameLine.text()+'：'+text
            self.socketTCP.send(message.encode('utf-8'))

        else:
            item.setTextAlignment(Qt.AlignLeft)  # 左对齐
            item.setBackground(Qt.white)  # 设置背景色
        item.setText(text)

        # 添加到列表
        self.chat_area.addItem(item)
        # self.chat_area.scrollToBottom()
        self.input_box.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChatWindow()
    window.show()
    sys.exit(app.exec())