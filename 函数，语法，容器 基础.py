import random

name="zjp"

"""
注释
"""
# 注释

"""
我们从一个具体的例子切入本节内容。假设现在有两个数字，我们希望获得其中较大的一个，那么可以使用 if else 语句，例如：
if a>b:
    max = a;
else:
    max = b;
但是 Python 提供了一种更加简洁的写法，如下所示：
max = a if a>b else b

print("1年费分23")
print(123)  # 123


a = 99
print("我的钱还有",a,"元")

type1=type(a)
print(type1)
print(type("fwbi"))


a=10
str_a=str(a) # 将a转字符串
print(type(str_a),str_a)



num1=999999219853
print(num1,"//541:",num1//541)
print(num1,"%541:",num1%541)
num2=2
num2**=3
print(num2)


name='"zjp"'
print(name)

name2='\'zjp\''  #斜杆
print(name2)


name2="df"+"fwf"+'fw1f'
print(name2)

name3="df"+"fwf"+123 #这个不行
print(name3)

name4="我是"
print("%szjp" %name4) # %表示字符串 s表示字符串
num7=13
p="p"
name="zj%s"%p
print("我是%s我今年%s岁"%(name,num7))

num11=123
print("将字符串转数字用d转成浮点用f，如：%d"%num11)
print()

#精度控制
num=123456.7890123
print("%2.1f"%num)
print("%5d"%num)   # %5.2f表示宽度控制为5(5表示至少为5，多于5就不删)，小数点精度控制为2
# %.2f 表示不限制宽度，精度控制为2
num2=999.222
print(f"my name is{name},and my number is {num2}") # 不作精度控制，各种格式数字都可以输入 f:format
print("%.2f"%(3.1415926**3))

numR=input("计算数的三次方：")
numR=int(numR)
numR**=3
print("三次方=%d"%numR)

print(f"is it true:{6>10}") #is it true:False

age=input("your age:")
age=int(age)
if(age>=150):
    print("wrong")

age=input("your age:")
age=int(age)
if age<=14:
    print("you are child")
elif age<=18:
    print("you are not adult")
else:
    print("you are adult")

while 1==1:
    sum=input("total number:")
    sum=int(sum)
    i=0
    my_list=[]
    while i<=sum:
        my_list.append(random.randint(0,sum))
        i+=1
    a=0
    for item in my_list:
        a+=item
    print(f"average:{a/sum}")
    average=a/sum
    D=0
    D_sum=0
    for item in my_list:
        D=item-average
        D_sum=D**2+D_sum
    print(f"D:{D_sum/sum}")


print("123",end="")
print("456",end="")         # 123456请按任意键继续. . .
print()

print("姓名\t年龄\t地点")
print("张三张\t25\t北京")
print("李四张\t30\t上海")#当你在控制台或文件中打印带有制表符的字符串时，它会在制表符的位置跳到下一个制表位，
                        #通常是8个字符的宽度，但这取决于终端或编辑器的设置。汉字占两个字符。
#姓名    年龄    地点
#张三    25      北京
#李四    30      上海

size=input("size:")  #99乘法表
size=int(size)
i=1
i2=1
while i2<=size:
    i=1
    while i<=i2:
        print(f"{i}*{i2}={i*i2}\t",end="")
        if i==i2:
            print()
        i+=1
    i2+=1

letter="a" #也可以提前定义
for letter in name:
    print(letter)   #遍历字符串
r1=range(10)  #获取得到0~9的列表
r2=range(5,10) #5,6,7,8,9
r3=range(0,100,4)
for r in r3:
    print(r,end=" ") #0 4 8 12 16 20 24 28 32 36 40 44 48 52 56 60 64 68 72 76 80 84 88 92 96 
for fors in range(0,100):  #一个跑了100遍的for循环
    print(fors,end=" ")


print(len(name))
def return_big(a,b):
    if a>=b:
        return a
    else:
        return b 
    return None
def none():
    print()
    
print(none)       # <function none at 0x0000019A054DB380>
if None :         #也有False的意思
    print()
if not None :         #not 取反
    print()


num1=0 #全局变量
def change_num1():
    num1=100 #变回局部变量
change_num1()
print(num1) #0 无法修改
def change_num1_2():
    global num1 #转全局变量
    num1=100 
change_num1_2()
print(num1) #100 修改成功



list=list()#空列表定义方法
list2=[1,2,3,4]#空列表定义方法
#列表内可以存储不同的数据类型
list=[1,"2货",True,list2]
print(list)#[1, '2货', True, [1, 2, 3, 4]]

print(list2[-1])#4 倒数第一
"""
230
456
789
"""
matrix=[[2,3,0],[4,5,6],[7,8,9]]
#若要取0，是：
print(matrix[0][2])

list=[2,2,2,2,2,2,2]
print(list.count(2)) #7 统计份数
print(len(list)) #7
list2=[1,2,3,4]
print(list2.index(2))
list2.insert(0,1)
print(list2)#[1, 1, 2, 3, 4]
list2.append(100)
print(list2)#[1, 1, 2, 3, 4, 100]
list2.extend(list)
print(list2)#[1, 1, 2, 3, 4, 100, 2, 2, 2, 2, 2, 2, 2]
del list2[5]
print(list2)#[1, 1, 2, 3, 4, 2, 2, 2, 2, 2, 2, 2]
num1=list2.pop(0)      # 删除元素的同时返回
print(num1)
print(list2)#[1, 2, 3, 4, 2, 2, 2, 2, 2, 2, 2]
list2.remove(1)
print(list2) #[2, 3, 4, 2, 2, 2, 2, 2, 2, 2] 删除第一个找到的1
list2.clear() #清空     

tp1=(1,)#单个数据的元组定义方法 ，不加这个逗号就变成int了
tp=tuple()
tp=(2,8,9,9,8)

#tp[0]=9 元组内元素不能修改，但是元组内的list里的元素可以修改

str9="abcdefghijklmnopqrstuvwxyz"
print(str9[1]) #b
print(str9[-1]) #z
#str9[0]=0  字符串像元组一样不可修改已经定义好的string
new_str=str9.replace("xy","00000000")
print(new_str)
wait_to_split_string="123,456,789,098,453,324"
splited_list=wait_to_split_string.split(",")
print(splited_list) #['123', '456', '789', '098', '453', '324']
print(splited_list[1]) #456
string1="\n\n\n   ajinsdibfgu   \n \n \n"
string2=string1.strip() #去除开头结尾换行符与空格
print(string1)
print(string2)
num_s="2121212121212126621261261621212616216262616262612162612621612621212121212121212121"
#去除上面的处在开头结尾的12，可以这样：
new_num_s=num_s.strip("12")
print(new_num_s)  #66212612616212126162162626162626121626126216126

string3="今天天气好热，我快要热成傻子了"
print(string3[0:6]) #不含第六个      #今天天气好热
print(string3[0:15:2]) #默认步长为1，现在设置为2 #今天好，快热傻了
print(string3[:]) #取全部
print(string3[::2]) #步长2                      今天好，快热傻了
print(string3[::-1])#了子傻成热要快我，热好气天天今
print(string3[6:0:-2]) # ，好天


#set的元素可以修改，不能重复
set1={99,1,2,3,4,5,6,7}#根据哈希值排列
print(set1)
set1.remove(1)
print(set1)
print(set1.pop())
set2={4,5,6,7}
print(set1.difference(set2))# 返回set1有的set2没有的，即差集，对set1不变
set1.difference_update(set2)# 更新set1为差集
print(set1)#{99, 3}
set3=set1.union(set2)
print(len(set1)) # 统计长度


dic1=dict()
dic1={"爱好":"男","性别":"女","存款":"0"} #key:value ,对于key不可以是字典，但是value可以
print(dic1["性别"])#nv
#新增加元素：
dic1["身高"]="165"
#删除key与value
str=dic1.pop("存款")#{'爱好': '男', '性别': '女', '身高': '165'}
print(dic1)
#获取全部key
keys=dic1.keys()
#遍历value
for one in keys :
    print(dic1[one])
#遍历key
for one in keys :
    print(one)
#字典长度
print("字典的长度",len(dic1))

print(dic1["身高"])#
score={
    "zjx":{
        "english":10
        ,"math":1
        ,"history":8
    },
    "zjp":{
        "english":8
        ,"math":8
        ,"history":8
    },
    "zlf":{
        "english":9
        ,"math":8
        ,"history":5
    }
}
print(score["zjp"]["english"])#8


#max(容器) min(容器) 可以得到容器内最大最小元素
#str() list() tuple() set() 可以将列表相互转换
#字典转列表会抛弃value
#字典转字符串可以保留value与key
#sorted(容器,reverse=True)可以排序，排序完容器变列表,reverse=True可以实现反转
set1={"a1","a2","a4","a6","a5","a0","a11","a7"}
print(sorted(set1,reverse=True)) # ['a7', 'a6', 'a5', 'a4', 'a2', 'a11', 'a1', 'a0']


# 多个返回值
def return_3():
    return 3,"zjp",3
x,y,z=return_3()
#函数传参方式
def abc(a,b,c=1):
    return a*b*c
print(abc(8,b=7))

def sums(*args):  #元组 arguments
    sum_a=0
    for one in args:
        sum_a+=one
    print(sum_a)
sums(1,5,8,1,1,1,2)

def sum2(**kwargs): #keyword-arguments
    print(kwargs)
    for key, value in kwargs.items(): 
        print(f"{key}: {value}")
sum2(name="zjp",money=999,age=10)

def print_info(name, age, **kwargs):
    print("Name:", name)
    print("Age:", age)
    occupation = kwargs.get('occupation') #kwargs.get(key) 是字典的get方法，用于获取指定键对应的值。如果键不存在，则返回None
    city = kwargs.get('city') 
    print("Occupation:", occupation)
    print("City:", city)
print_info("Alice", 30, occupation="Engineer", city="New York")

def ab(**aa): 
    a1=aa.get('a')
    b1=aa.get('b')
    print(a1+b1) #4
ab(a=1,b=3)

#函数作为另一个函数的参数
def my_add(x,y):
    return x+y
def my_muti(x,y):
    return x*y
def couter_1(my_add,my_muti):
    print(my_add(1,2)+my_muti(2,3))
couter_1(my_add,my_muti)#9
"""

def couter_1(my_add,my_muti):
    print(my_add(1,2)+my_muti(2,3))
couter_1(lambda z,x:z+x,lambda z,x:z*x)#结果:9 lambda只能写一行，这一行的结果直接return


