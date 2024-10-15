import socket

socket_client=socket.socket()
socket_client.connect(('localhost',2467))
socket_client.send('我是客户端。'.encode('UTF-8'))
recv_data=socket_client.recv(1024).decode('UTF-8') # 缓冲区
print(f'服务端回复的消息是：{recv_data}')
socket_client.close()