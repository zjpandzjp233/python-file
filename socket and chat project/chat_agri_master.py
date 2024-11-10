import socket
import time
import os,threading
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import sys


chatLog=''
clientList=[]
socketTCP=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socketTCP.bind(('127.0.0.1',8888))
socketTCP.listen(128)
mutex=threading.Lock()
currentClientNum=0
def splitData(data):
    for line in data.splitlines():# 按行切分
        print(line)
        li=line.split(',')
        for l in li:
            print(l)
def ifAnyOneHere():
    i=0
    while True:
        global socketTCP,currentClientNum,clientList
        # socket_object, address_info=socketTCP.accept()
        newGuy=socketTCP.accept()
        clientList.append(newGuy[0])
        
        mutex.acquire()
        currentClientNum+=1
        mutex.release()
        print('new connnect:',newGuy[1])
        t=threading.Thread(target=singleClient,args=(newGuy[0],newGuy[1],i))
        t.start()
        i+=1
def saveFile():
    with open('chatLog.txt','w',encoding="UTF-8") as f:
        f.write(chatLog)
def radioToEachOne():
    pass
def singleClient(socket_object, address_info,i):
    global currentClientNum,chatLog,clientList
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
            
            chatLog=chatLog+address_info[0]+','
            chatLog+=data
            chatLog+='\n'
            socket_object.sendall('**ok**'.encode('utf-8'))
            for socket1 in clientList:
                if socket1==0 or socket1==socket_object:
                    continue
                socket1.sendall(data.encode('utf-8'))
            data=''
            print('chatLog:','\n',chatLog)
        else:
            clientList[i]=0
            break
    socket_object.close()
    mutex.acquire()
    currentClientNum-=1
    mutex.release()
t1=threading.Thread(target=ifAnyOneHere)
t1.start()



