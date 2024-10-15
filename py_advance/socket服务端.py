import socket

serve=socket.socket() # 创建socket对象
serve.bind(('localhost',2467)) # 绑定ip和端口
serve.listen(10) # 表示接收的连接数量，运行10个客户端和我服务端通讯

conn,address = serve.accept() # 返回二元元组，可以这样写来接收变量，
# 返回值是（链接对象，客户端地址信息）
# 如果没有客户端连接，程序会卡在这一行代码

print(f'接收到了客户端的链接，客户端信息是{address}')

data:str=conn.recv(1024).decode('UTF-8')# 缓冲区大小一般设置为1024，用decode解码byte数组
# recv没有接收的信息也会阻塞代码

print(f'接收到客户端的数据是：{data}')
msg=input("要给客户端的回复：").encode("UTF-8")
conn.send(msg)

conn.close()
serve.close()