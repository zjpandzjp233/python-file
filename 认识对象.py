import random
import typing
"""

import winsound
class student:
    def __init__(self,str,genders,age2): # 类被创建的时候自动执行 ，接受传入参数
        self.name=str
        self.age=age2 # 成员变量，也可以放在__init__函数内，同样属于类里面的成员

    def __str__(self) -> str: # 当类被当做字符串对待时，或类被转成字符串时，就变成以下的字符串
        return f"I'm student, my name is {self.name}, i am {self.gender}"

    def __lt__(self,other): #使得python实现大于号和小于号的比较 
        return self.age<other.age
    # __gt__（大于）、__le__（小于等于）、__ge__（大于等于）、__eq__（等于）
    def __le__(self,other): #less equal #使得python实现大于等于号和小于等于号的比较 
        return self.age<=other.age
    def __eq__(self, other) -> bool: # 箭头 -> 用于指定函数的返回类型注解。这是一种可选的语法，可以帮助提高代码的可读性和可维护性。你想返回其他的也可以
        return self.age==other.age
    name="none"
    gender=None
    __my_girlFriend_name_ages_ago="myh" # 私有成员，类外都不能用
    __girlFriend_gender="woman"
    def __get_my_girlFriend_name_in_before(self)->str: # 私有方法，类外都不能用
        return self.__my_girlFriend_name_ages_ago
    def __am_I_gay(self)->bool:
        print(f"i love {self.__my_girlFriend_name_ages_ago}.")
        return not self.__girlFriend_gender=='woman'
    def say_hi(self,add): # self是必须存在的参数，但是调用此函数时可以不必赋予值给self
        print(f"hi,i am {self.name},{add}")
    def scream(self):
        winsound.Beep(5000,1000) # beep的频率与时间
    

stu999=student("zjp00","man",999)
stu1=student("zjp00","man",1)
stu1.name="zjp"
#print(stu1.name)
#stu1.say_hi("how are you.")
print(stu999<stu1) # False
print(stu999>stu1) # True
print(stu1>stu999) # False
print(stu1<stu999) # True
stu1.age=999 
print(stu1<=stu999) # True
print(stu1==stu999) # True 如果没有实现__eq__ 则==比较两个对象的内存地址

# print(stu1.__am_I_gay()) # 'student' object has no attribute '__am_I_gay'


class my_plus:
    ID=1
    def plus(self,a,b):
        print("父类的加法启动")
        return a+b
    def __say_my_name(self): # 私有函数不参与继承
        print("my_plus")
class my_multiply:
    ID=2
    def multiply(self,a,b):
        return a*b
class my_calculate(my_plus,my_multiply): # 多继承，继承了括号内两个对象的所有内容，如果两个对象的内容存在重复，优先选择前面的
    ID=3 #如果不想继承my_plus的ID,也可以自己覆写
    def my_father_ID(self):
        print(f"plus's ID={my_plus.ID}")
        b=1
        c=2
        f=my_plus.plus(self,b,c) # 调用父类已经被覆写的函数也是可以的，但是要记得加一个self
        # 下面是另一种写法
        c=999
        f=super().plus(b,c) # super即表示它的父类
        print(f"使用super调用父类ID时选的是：{super().ID}") # 使用super调用父类ID时选的是：1
        return f
    def plus(self,b,c): #覆写父类
        d=b+c
        f=my_plus.plus(self,b,c) # 覆写了父类的的函数的同时，在函数内调用了父类的函数
        return f

cal=my_calculate()
print(cal.ID) # 1 
cal.my_father_ID() # plus's ID=1
print(cal.plus(99,99)) # 198
print(cal.my_father_ID()) # 1000


num:int=10
num2:float=9.9999 # 表示num2是float的变量类型
my_name:str="zzjjpp"
box:list[int]=[5,3,9]
box4:list[typing.Union[int,str]]=[123,456,"abc"] # typing.Union[int,str]表示即包含int也包含str
box2:tuple[int,bool,float,str]=(1,False,8.1927,"name")
book:dict[str,int]={"zjp":15456325785,"zjx":15598532156}
bool2:dict[typing.Union[int,str],str]={159753:"不知道","合金弹头":"知道"}
class man:
    def I_am_man(self):
        print("I_am_man")

# 通过注释 '# type:list' 的格式也可以实现和上方一样的效果
A=list(range(1,11)) # type:list
B=9.99 # type: float
m:man=man() # 表示m是man类的变量

def my_subtract(a:int,b:int)->typing.Union[int,float]:
    return a-b
print(my_subtract(-99,1)) # -100


#多态
class 动物叫 : # 抽象类
    def speak (self): # 抽象方法
        pass
    def bark (self):
        print("父类动物叫")
class 狗(动物叫):
    def speak(self):
        print("狗不会说话")
class 人(动物叫):
    def speak(self):
        print("乖狗狗。")
def 吠(object:动物叫):
    object.bark()
    object.speak()

dog=狗()
human=人()
吠(dog) # 父类动物叫 # 狗不会说话
吠(human) # 父类动物叫 # 乖狗狗。
"""
list1=[1,2,3]
list2=[3,4,5]
list3=list1+list2
print(list3) # [1, 2, 3, 3, 4, 5]

