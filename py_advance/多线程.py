# import threading

# thread_obj =threading. Thread([group [， target [， name [， args [， kwargs]]]]] 

# —group：暂时无用，未来功能的预留参数

# —target：执行的目标任务名

# —args：以元组的方式给执行任务传参—kwargs：以字典方式给执行任务传参—name：线程名，一般不用设置

# 启动线程，让线程开始工作thread_obj.start() 


import time
import threading

def T1(msg):
    while True:
        print(msg)
        time.sleep(1)
def T2(msg,msg2):
    while True:
        print(msg,msg2)
        time.sleep(1)

# args 参数是一个元组，用于传递位置参数给目标函数。args 元组可以包含多个元素，每个元素对应目标函数的一个参数。
# 你之前的代码中，args=('T1运作了一遍。',) 只传递了一个参数，但这并不意味着 args 元组只能有一个元素。
th1=threading.Thread(target=T1,args=('T1运作了一遍。',))
th2=threading.Thread(target=T2,kwargs={'msg':'T2运行了一遍。','msg2':'T2的第二个参数'})  #key的名字和函数参数相同
th1.start()
th2.start()
# args=('T1运作了一遍。',)：
# 这是一个包含一个元素的元组，元素是字符串 'T1运作了一遍。'。
# 当线程启动时，T1 函数接收到的 msg 参数就是这个字符串。

# kwargs={'msg': 'T2运行了一遍。'}：
# 这是一个字典，键是 'msg'，值是字符串 'T2运行了一遍。'。
# 当线程启动时，T2 函数接收到的 msg 参数就是这个字符串。