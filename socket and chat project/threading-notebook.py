
import multiprocessing.managers
import multiprocessing.pool
import multiprocessing.queues
import threading,multiprocessing
import socket
import os,sys,time,random
import gevent.monkey
from progress.bar  import FillingCirclesBar
from collections.abc import Iterable
from collections.abc import Iterator
# 如果任务是 CPU 密集型的，那么使用进程池会更有效；如果是 I/O 密集型的，则线程池可能更加适合。
# I/O 密集型任务指的是那些需要大量进行输入输出操作的任务，这些操作包括但不限于文件读写、网络通信等。  使用管道或消息队列在不同进程之间传递数据。
# CPU 密集型任务是指那些主要消耗 CPU 资源的任务，这类任务的特点是计算量大，对 CPU 的依赖性强，而 I/O 操作相对较少。


"""
多核处理器的利用：
现代计算机通常配备多核处理器，这意味着可以同时执行多个任务。对于 CPU 密集型任务，使用进程池可以充分利用多核处理器的能力。每个进程可以在不同的核心上并行执行，从而最大化 CPU 的利用率。
Python 的 multiprocessing 模块通过创建多个进程来实现这一点。每个进程都有自己的 Python 解释器实例，因此可以独立地执行任务，不受 GIL（全局解释器锁）的限制。
避免 GIL 限制：
在多线程环境中，由于 Python 的 GIL 存在，即使有多核处理器，同一时刻也只有一个线程能执行 Python 字节码。这意味着多线程在 CPU 密集型任务中并不能真正实现并行计算。
进程之间没有共享内存，每个进程有自己的 GIL，因此可以真正实现并行计算。
I/O 密集型任务与线程池
阻塞和等待时间：
I/O 密集型任务的主要特点是存在大量的等待时间，例如等待网络响应、文件读写等。在这段时间内，CPU 并没有做太多的工作。
使用线程池可以有效地管理这些等待时间。当一个线程在等待 I/O 操作完成时，其他线程可以继续执行其他任务，从而提高整体的效率。
轻量级和资源占用：
线程比进程更轻量级，创建和切换的成本更低。对于 I/O 密集型任务，频繁的创建和销毁线程不会带来太大的性能开销。
线程共享同一个进程的内存空间，因此在数据共享和通信方面更加方便和高效。
"""


def sing():
    for a in range(2):
        time.sleep(1)
        print('singing')
def dance():
    for a in range(5):
        time.sleep(1)
        print('dancing')
def 同时跑连个函数():
    threading1=threading.Thread(target=sing) # 创建了一个线程的对象
    threading2=threading.Thread(target=dance)
    threading1.start() # 真正的创建了线程，并执行
    threading2.start()
    while True:
        print(threading.enumerate()) # 一个列表，每个元素表示一个线程，一个主线程和一些子线程
        if len(threading.enumerate())<=1:
            break
        time.sleep(0.5)
        """
        [<_MainThread(MainThread, started 8124)>, <Thread(Thread-6 (sing), started 12420)>, <Thread(Thread-7 (dance), started 16604)>]
        [<_MainThread(MainThread, started 8124)>, <Thread(Thread-6 (sing), started 12420)>, <Thread(Thread-7 (dance), started 16604)>]
        dancingsinging
        [<_MainThread(MainThread, started 8124)>, <Thread(Thread-6 (sing), started 12420)>, <Thread(Thread-7 (dance), started 16604)>]        
        [<_MainThread(MainThread, started 8124)>, <Thread(Thread-6 (sing), started 12420)>, <Thread(Thread-7 (dance), started 16604)>]
        dancing
        singing
        [<_MainThread(MainThread, started 8124)>, <Thread(Thread-7 (dance), started 16604)>]
        [<_MainThread(MainThread, started 8124)>, <Thread(Thread-7 (dance), started 16604)>]
        dancing
        [<_MainThread(MainThread, started 8124)>, <Thread(Thread-7 (dance), started 16604)>]
        [<_MainThread(MainThread, started 8124)>, <Thread(Thread-7 (dance), started 16604)>]
        dancing
        [<_MainThread(MainThread, started 8124)>, <Thread(Thread-7 (dance), started 16604)>]
        [<_MainThread(MainThread, started 8124)>, <Thread(Thread-7 (dance), started 16604)>]
        dancing
        [<_MainThread(MainThread, started 8124)>]
        """
# 同时跑连个函数()

# a=['gjg','xjtjt','ydjdj']
# print(enumerate(a))
# for aa in enumerate(a):
#     print (aa)
#     """
#     (0, 'gjg')
#     (1, 'xjtjt')
#     (2, 'ydjdj')
#     """


class 用类来跑多线程(threading.Thread):
    i=0
    def run(self): #重写thread里面的函数
        while self.i<3:
            print(f'class func1，this thread name is {self.name}') # name 里面保存了这个线程的名字
            time.sleep(1)
            self.i+=1
def 用类来跑多线程2():
    thread1=用类来跑多线程()
    thread1.start() # 自动调用run
#用类来跑多线程2()



list1=[1,2]
def 全局变量有时候可以不加globe():
    global list1 # 这里加不加globe下面都可以修改成功
    list1.append(0)
    list1[0]=0
#全局变量有时候可以不加globe()
# print(list1)

# num=123456.7890123
# print("%2.1f"%num) # 123456.8
# print("%5d"%num)   # %5.2f表示宽度控制为5(5表示至少为5，多于5就不删)，小数点精度控制为2 # 123456
# # %.2f 表示不限制宽度，精度控制为2
# num2=999.222
# print(f" my number is {num2}") # 不作精度控制，各种格式数字都可以输入 f:format    #  my number is 999.222
# print("%.2f"%(3.1415926**3)) # 31.01


a=0
def test1():
    global a
    a+=1
def test2():
    print(a) # 1
def 子线程共享全局变量():
    threading1=threading.Thread(target=test1)
    threading2=threading.Thread(target=test2)
    threading1.start() 
    time.sleep(1)
    threading2.start() 
    time.sleep(1)
    print(a) # 1
# 子线程共享全局变量()


def test3(a):
    print(a)
def 多线程传参():
    threading1=threading.Thread(target=test3,args=(10,))
    threading1.start()
# 多线程传参()


mutex=threading.Lock()
i3=0
def add1():
    global i3
    for a in range(10000000):
        mutex.acquire()
        i3+=1
        mutex.release()
def add2():
    global i3
    for a in range(10000000):
        mutex.acquire() # 没拿到锁的会被阻塞
        i3+=1
        mutex.release()
def 互斥锁():
    threading1=threading.Thread(target=add1)
    threading2=threading.Thread(target=add2)
    threading1.start() 
    threading2.start()
    time.sleep(10)
    print(i3) # 20000000
# 互斥锁()
# 主线程会等到所有子线程结束才结束



def sing2():
    for a in range(2):
        time.sleep(1)
        print('singing')
def dance2():
    for a in range(5):
        time.sleep(1)
        print('dancing')
def 同时跑连个函数2():
    process1=multiprocessing.Process(target=sing2)
    process2=multiprocessing.Process(target=dance2)
    process1.start() # 子进程会占用和主进程一样的资源，子线程会拷贝过去 ，进程里面跑线程 ,且进程之间独立的
    process2.start() 

# if __name__ == '__main__':
    # 同时跑连个函数2() # 多进程必须放到这里执行，不然报错： 试图在当前进程完成引导阶段之前启动新进程。


def Queue2():
    mq=multiprocessing.Queue(3)
    mq.put(3)
    mq.put(3)
    print(mq.full()) # f
    print(mq.empty()) # f 
    mq.put(3)
    print(mq.get()) # 3
    mq.put(4) # 装满了就要等
    print(mq.get()) # 3
    print(mq.get()) # 3
    print(mq.full()) # f
    print(mq.empty()) # f
#Queue2()

def timeNote():
    time1=time.time()
    time.sleep(2)
    time2=time.time()
    print(time2-time1) # 2.000816822052002


# 进程间通信

def 模拟产生数据(q:multiprocessing.Queue):
    while True:
        time.sleep(0.2)
        q.put('一个待处理的数据')
        print('一个待处理的数据已经产生！')
def 模拟处理数据(q:multiprocessing.Queue):
    while True:
        time.sleep(1)
        while True:
            time.sleep(0.03)
            if not q.empty():
                print(q.get()+'已被处理！')
            else:break
def 同时跑连个函数3():
    q=multiprocessing.Queue() # 没带参数不限大
    process1=multiprocessing.Process(target=模拟产生数据,args=(q,))
    process2=multiprocessing.Process(target=模拟处理数据,args=(q,))
    process1.start() 
    process2.start() 
    process1.join()
    process2.join()
# if __name__ == '__main__':
#     同时跑连个函数3()


# 进程池  进程创建和销毁需要大量时间，而且电脑一时间能有的进程数具有限制，所以创建三个进程让他们重复共同工作


def work(a,ii,q1:multiprocessing.Queue):
    i=a
    while i<10:
        # print('第 ',ii,'个work开始工作,pID是',os.getpid())
        time.sleep(0.2)
        i+=1
        q1.put(1) # 每加入一个元素表示一个进程工作完成1/10
    

def pool2():
    bar = FillingCirclesBar('Processing', max=60)
    i=0
    pool1=multiprocessing.Pool(3) #  最大进程数三,进程代码错误不会报错，直接停掉 报错的 进程 
    q1=multiprocessing.Manager().Queue() # 这种队列的实现是基于网络连接的，因此它可以跨多个进程甚至跨机器使用。
    for a in range(6):
        pool1.apply_async(work,(0,i,q1)) # 进程池会自己占满所有进程来主线任务，如果所有进程都在工作，这条代码本身不会阻塞，即使进程池已经满了，然后空闲自动添加进进程,
        i+=1
    pool1.close() # 使进程池不再接收新任务，但是线程池还在工作
    # pool1.join() # 等待线程池，如果没有这个代码，主线程代码走完如果线程池还在工作就会强制关闭导致报错
    iii=0
    while True:
        if not q1.empty():
            q1.get() # 如果队列为空，调用 get 方法的线程将会阻塞
            iii+=1
            bar.next()
            if iii==60:
                break
    bar.finish()

# if __name__ == "__main__":
#     pool2()

def iterable2():
    
    print(isinstance([1, 2, 3, 4, 5, 4], Iterable)) # True    [1, 2, 3, 4, 5, 4]是否可迭代, isinstance检查列表 [1, 2, 3, 4, 5, 4] 是否是 Iterable 的实例
    print(isinstance(5, Iterable)) # False


# raise ZeroDivisionError("除数不能为零") # 抛出异常的写法
# 迭代器
def Iteration2():
    class classMenberName():
        nameList=[]
        def __init__(self) -> None:
            self.nameList=['zjp','kdo','lks','jkf','gsd']
        def addName(self,name):
            self.nameList.append(name)
        def __iter__(self):
            return 迭代器(self) # 将自己的应用传给迭代器，方便迭代器来使用这里的东西
    class 迭代器():
        def __init__(self,obj1:classMenberName) -> None:
            self.obj=obj1
            self.index=0
        def __iter__(self):
            pass
        def __next__(self):
            if self.index<len(self.obj.nameList):
                ret=self.obj.nameList[self.index]
                self.index+=1
                return ret
            else:
                raise StopIteration  # 抛出停止异常，停止迭代

    # print(isinstance(classMenberName(), Iterable)) # True
    # print(iter(classMenberName())) # 得到一个可迭代对象的迭代器 <__main__.迭代器 object at 0x00000237844A5610>   
    # print(isinstance(iter(classMenberName()), Iterator)) # True 判断是不是迭代器

    # 迭代器1=iter(classMenberName())
    # print(next(迭代器1)) # 11 调用迭代器的next方法

    for a in classMenberName():
        print( a)

# 下面是上面的简练提升版

def up2():
    class classMenberName():
        nameList=[]
        def __init__(self) -> None:
            self.nameList=['zjp','kdo','lks','jkf','gsd']
            self.index=0
        def addName(self,name):
            self.nameList.append(name)
        def __iter__(self):  # 有了这个函数叫可迭代，
            return self     # 返回自己，然后会取自己里面的next迭代器
        def __next__(self):
            if self.index<len(self.nameList):
                ret=self.nameList[self.index]
                self.index+=1
                return ret
            else:
                raise StopIteration  # 抛出停止异常，停止迭代
    for a in classMenberName():
        print( a)
# up2()



# 如果要几十亿个生成的数据，直接生成出来肯定很卡，但是如果用迭代器的方式，把生成这种列表的方法记下来，然后用方法一个个生成的话，就不用上来就存储一个大列表，可以随用随取

def 迭代器式斐波那契数列func():
    class 迭代器式斐波那契数列():
        nameList=[]
        def __init__(self,len) -> None:
            self.allNum=len
            self.a=0
            self.b=1
            self.index=1
        def __iter__(self):
            return self
        def __next__(self):
            if self.index==1:
                self.index+=1
                return 0
            elif self.index==2:
                self.index+=1
                return 1
            elif self.index<=self.allNum:
                wait_return=self.a+self.b
                self.a=self.b
                self.b=wait_return
                self.index+=1
                return wait_return
            if self.index>self.allNum:
                self.a=0
                self.b=1 # 重置参数 方便下次迭代
                self.index=1
                raise StopIteration

    fibo=迭代器式斐波那契数列(10)
    i=0
    for a in fibo:
        time.sleep(0.1)
        i+=1
        if i<15:
            print(a,end=',')
        else:
            print()
            print(a,end=',')
            i=0
    
    # 同样可迭代的对象也可以通过迭代变成列表等容器
    print(list(fibo))
# 迭代器式斐波那契数列func()







# 生成器
def next和send启动生成器():
    def li():
        li1=(a for a in range(10)) 
        for a in li1:
            print(a,end=',') # 0,1,2,3,4,5,6,7,8,9,

    def li99(Range):
        i=0
        while i<=Range:
            yield i # 有yield的函数叫生成器
            i+=1

    li3=li99(Range=10)
    print(next(li3)) # 0 执行li99函数到yield暂停，yield 一个值
    print(next(li3)) # 1 从上面的位置继续执行代码，再此跑到yield结束
    for a in li3:
        print(a,end=',') # 2,3,4,5,6,7,8,9,10, 会被上面的next影响


# send启动生成器可以传参():
def send启动生成器可以传参():
    def li99(Range):
        i=0
        while i<=Range:
            returnYield=yield i # 有yield的函数叫生成器
            i+=returnYield
            i+=1
    li10=li99(100)

    print(next(li10)) # 0  从函数开头跑到yield

    # 用于中途调整参数
    print(li10.send(10)) # 11   给returnYield赋了值，然后向下执行到下一次yield返回值
    print(next(li10)) # 报错，因为next使returnYield=None

# send启动生成器可以传参()



#yield实现多线程
def yield实现多线程():
    def task_1():
        while True:
            print("----1-----")
            time.sleep(0.1)
            yield      #为什么不改成return： 这样函数不必来回创建 ，也能实现状态保存，还能通过send中途改变状态

    def task_2():
        while True:
            print("----2-----")
            time.sleep(0.1)
            yield

    def main():
        t1 = task_1()
        t2 = task_2()
        while True: 
            next(t1)
            next(t2)

    if __name__ == "__main__":
        main()

# yield实现多线程()


#利用greenlet实现多线程
def 利用greenlet实现多线程():
    from greenlet import greenlet

    def test1():
        while True:
            print("---A---")
            gr2.switch() # 跳到test2执行
            time.sleep(0.5)

    def test2():
        while True:
            print("---B---")
            gr1.switch() # 跳到test1执行，然后就会开始来回跳
            time.sleep(0.5)

    gr1 = greenlet(test1)
    gr2 = greenlet(test2)

    # 切换到gr1中运行
    gr1.switch() # 使test1执行

#利用greenlet实现多线程()
"""
---A---
---B---
---A---
---B---
---A---
---B---
---A---
---B---
---A---
...
"""



def 利用gevent实现多线程():
    #利用gevent实现多线程()
    # 仍然是单线程，但是一个函数在浪费时间时会自动切换
    """
    网络 I/O 操作：任何涉及网络通信的操作，如发送和接收数据包、HTTP 请求等，通常会触发任务切换。例如，使用 gevent 的 socket 模块进行网络通信时，当等待数据到达或发送数据完成时，gevent 会自动切换到其他任务。
    python
    文件 I/O 操作：读写文件时，如果使用 gevent 的文件 I/O 模块，如 gevent.fileobject，同样会触发任务切换。
    数据库操作：使用 gevent 兼容的数据库连接库进行数据库操作时，当等待数据库响应时，gevent 会自动切换任务。
    定时器：使用 gevent 的 Timer 类设置定时器，当定时器到期时，会触发任务切换。
    其他阻塞操作：任何使用 gevent 的阻塞操作，如锁（gevent.lock）、事件（gevent.event）等，都会触发任务切换。
    """

    import gevent
    from gevent import monkey
    monkey.patch_all() # 使得原生python的阻塞操作也能使其自动切换,其原理是检查整个代码自己会把类似这种time.sleep(0.5)改成gevent.sleep(0.5)后再执行整个代码
    """
    monkey.patch_all() 需要配合在launch.json里加上
    "env": {
                    "GEVENT_SUPPORT": "True"
                }
    使其不报错  
    """

    def f1(n):
        for i in range(n):
            print(gevent.getcurrent(), 'f1:', i) # gevent.getcurrent() 运行此函数的gevent
            gevent.sleep(0.5)
            # time.sleep(0.5)  # monkey.patch_all() 后都可以
    def f2(n):
        for i in range(n):
            print(gevent.getcurrent(), 'f2:', i)
            time.sleep(0.5)

    def f3(n):
        for i in range(n):
            print(gevent.getcurrent(), 'f3:', i)
            time.sleep(0.5)

    #  print('---1---')
    #  g1 = gevent.spawn(f1, 2)
    #  print('---2---')
    #  g2 = gevent.spawn(f2, 2)
    #  print('---3---')
    #  g3 = gevent.spawn(f3, 2)
    #  print('---4---')
    #  
    #  g1.join() # 如果函数内有gevent延时，那么它会停下，并跳到其他的如g2和g3的函数来填补空闲
    #  g2.join()
    #  g3.join()
    gevent.joinall([gevent.spawn(f1, 2), # 等价与上面的
                    gevent.spawn(f2, 2),
                    gevent.spawn(f3, 2)
    ])
    print('主线程是否被阻塞测试') # 是
    """
    <Greenlet at 0x182999ec900: f1(2)> f1: 0
    <Greenlet at 0x18299a940e0: f2(2)> f2: 0
    <Greenlet at 0x18299abcae0: f3(2)> f3: 0
    <Greenlet at 0x182999ec900: f1(2)> f1: 1
    <Greenlet at 0x18299a940e0: f2(2)> f2: 1
    <Greenlet at 0x18299abcae0: f3(2)> f3: 1
    主线程是否被阻塞测试
    """



import urllib.request
from urllib.error import URLError, HTTPError

try:
    req = urllib.request.urlopen('https://file.moyublog.com/d/file/2024-09-18/f062674bf1571598ae52e0db0c381e8d.jpg')
    img = req.read()
    """
    urllib.request.urlopen 返回的是一个文件类对象，其 read 方法可以读取响应体中的所有数据，无论是文本还是二进制数据。
    """
    with open('gem.jpg', 'wb') as f:
        f.write(img)
    print("图片下载并保存成功")
except HTTPError as e:
    print(f"HTTP Error: {e.code} - {e.reason}")
except URLError as e:
    print(f"URL Error: {e.reason}")
except Exception as e:
    print(f"An error occurred: {e}")

# 然后就可以写一个下载图片的函数，然后参数是网址，用joinall来给同一个函数传不同的参数来实现多个不同参数的多线程，函数可以多开




# 如果某个线程被阻塞了它也能分到一定时间来给这个线程,而协程就不会给被阻塞的函数时间来执行,如果多线程多阻塞可以用协程（gevent），类似于
# 网站下东西