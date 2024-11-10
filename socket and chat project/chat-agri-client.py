import socket
import time
import os,threading
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import sys
chatLog=''
masterIP='127.0.0.1'
masterPort=8777

def TCPsocket():
    socketTCP=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    connectServe=(masterIP,masterPort)
    socketTCP.connect(connectServe)
    message='this is a test messsage.'
    socketTCP.send(message.encode('utf-8'))
