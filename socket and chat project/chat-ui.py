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
        self.setWindowTitle("主机")
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
        self.down.clicked.connect(lambda:self.chat_area.scrollToBottom())
        self.readLog()
        threading3=threading.Thread(target=self.peopleNum)
        threading3.start()
        self.enter()
    def peopleNum(self):
        while True:
            time.sleep(0.5)
            self.label.setText('当前聊天室人数为：'+str(self.clientNum))
            for socket1 in self.clientList:
                    if socket1==0:
                        continue
                    socket1.sendall(('*'+str(self.clientNum)).encode('utf-8'))
    chatLog=''
    clientNum=1
    clientList=[]
    socketTCP=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    def readLog(self):
        try:
            with open('chatLog.txt','r',encoding="UTF-8") as f:
                self.chatLog=f.read()
        except Exception as e:
            with open('chatLog.txt','w',encoding="UTF-8") as f:
                return
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
    def singleClient(self,socket_object, address_info,i):
        self.clientNum+=1
        data=''
        while True:
            try:
                data=socket_object.recv(1024)
            except Exception as e:
                print(e)
            print('message address_info: ',address_info)
            if data: 
                data=data.decode('utf-8')
                print('data: ',data)
                self.otherPeopleMessageToList(datas=data)
                self.chatLog+=data
                self.chatLog+='\n'
                for socket1 in self.clientList:
                    if socket1==0 or socket1==socket_object:
                        continue
                    socket1.sendall(data.encode('utf-8'))
                data=''
                print('chatLog:','\n',self.chatLog)
            else:
                self.clientList[i]=0
                self.clientNum-=1
                break
        socket_object.close()
        self.mutex.acquire()
        self.currentClientNum-=1
        self.mutex.release()
    def ifAnyOneHere(self):
        i=0
        while True:
            # socket_object, address_info=socketTCP.accept()
            newGuy=self.socketTCP.accept()
            self.clientList.append(newGuy[0])
            self.mutex.acquire()
            self.currentClientNum+=1
            self.mutex.release()
            print('new connnect:',newGuy[1])
            t=threading.Thread(target=self.singleClient,args=(newGuy[0],newGuy[1],i))
            t.start()
            i+=1
    def enter(self):
        self.socketTCP.bind(('',8888))
        self.socketTCP.listen(128)
        t1=threading.Thread(target=self.ifAnyOneHere)
        t1.start()

    def closeEvent(self, event):
        # 在这里添加你想要执行的代码
        with open('chatLog.txt','w',encoding="UTF-8") as f:
            f.write(self.chatLog)
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
        self.chatLog=self.chatLog+'我'+'：'+text+'\n'
        # is_me = self.is_me_checkbox.isChecked()
        # 构造QListWidgetItem
        item = QListWidgetItem()
        is_me=True
        if is_me:
            item.setTextAlignment(Qt.AlignRight)  # 右对齐
            item.setBackground(Qt.lightGray)  # 设置背景色
            message='钟吉平：'+text
            for socket1 in self.clientList:
                    if socket1==0:
                        continue
                    socket1.sendall(message.encode('utf-8'))
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