import socket
import time
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
# UDP

# 局域网：
# 10.0.0.0 - 10.255.255.255 (前缀10/8)
# 172.16.0.0 - 172.31.255.255 (前缀172.16/12)
# 192.168.0.0 - 192.168.255.255 (前缀192.168/16)

# 127 打头的是回环，本机测试用 。回环地址主要用于测试本机上的网络软件，它让主机能够向自身发送网络数据包，就像与其他网络设备通信一样。

def sender():
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  # AF_INET ipv4      SOCK_STREAM流  TCP      SOCK_D GRAM电子的电报 数据报   UTP
    
    dest=('182.102.203.137', 15774)
    message='收到'
    # s.sendto(b'test_sendTo',dest) # 内容  对方的ip和端口的元组   b用来转二进制
    s.sendto(message.encode('UTF-8'),dest) 
    s.close() 



def litener():
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    local_address=('',8777) # 空字符串表示自己的ip 
    s.bind(local_address)
    time.sleep(5) # 如果你绑定好了端口号，还没开始recvfrom，那么你的系统会为你保存一部分，你recvfrom时一次性全给你
    while True:
        data=s.recvfrom(10000) # data 接收到的也是元组，第一个是数据，第二个是对方的ip与端口    
        print(data[0].decode('UTF-8'))
        print(data[1])
        s2=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        message='收到'
        s2.sendto(message.encode('UTF-8'),data[1]) 
        s2.sendto(message.encode('UTF-8'),(data[1][0],15774)) 
        print(data[1])
        if data[0].decode('UTF-8')=='close':
            break
    s.close()
    s2.close() 

def TCPsocket():
    socketTCP=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    connectServe=("127.0.0.1",8888)
    socketTCP.connect(connectServe)
    socketTCP.send(b'123456')
# TCPsocket()


def TCPsocketServe():
    socketTCP=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socketTCP.bind(('',8777))
    socketTCP.listen(128) # 非阻塞 设置监听队列长度为 128
    while True:
        # 每次调用 accept 方法时，都会从正在排队等待处理的客户端连接请求中取出一个
        socket_object, address_info=socketTCP.accept()  #   堵塞：等待连接  socket_object是socketTCP产生的专为客户端提供服务的小socket，address_info是客户端的地址
        while True:
            try:
                data=socket_object.recv(1024) #  阻塞：等待发送 返回的是数据 ，如果对方在我们等待接收时断开连接，这里会报错
            except Exception as e:
                print(e)
            print(data)
            print(address_info)
            if data: # 字符串空表示假 列表等容器空也同理 另外0表示假
                socket_object.sendall(b'ok') # sendall 方法确保所有数据都被发送出去，适用于需要保证数据完整性传输的场景。
                data=''
            else:
                break
        socket_object.close()
    socketTCP.close()
TCPsocketServe()

def TCP_sendTextFile():
    socketTCP=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socketTCP.bind(('',8777))
    socketTCP.listen(128) # 非阻塞 设置监听队列长度为 128
    socket_object, address_info=socketTCP.accept()
    while True:
        data=socket_object.recv(1024*1024*100) # 1MB
        if data:
            with open('./dataBinary.bin','ab') as f: # 或者用read来发文本文件 rb模式
                f.write(data)
        else:
            break
    socket_object.close()
    socketTCP.close()
# TCP_sendTextFile()








