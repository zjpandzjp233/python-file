
"""
常见路径表示法

当前目录 (.)
. 表示当前目录。
例如：./file.txt 表示当前目录下的 file.txt 文件。

父目录 (..)
.. 表示当前目录的上级目录（父目录）。
例如：../file.txt 表示当前目录的上级目录下的 file.txt 文件。

根目录 (/ 或 /)
/ 或 / 表示根目录（具体取决于操作系统）。
例如：/home/user/file.txt （Linux）或 C:/Users/user/file.txt （Windows）。

绝对路径
从根目录开始的完整路径。
例如：/home/user/documents/file.txt （Linux）或 C:/Users/user/Documents/file.txt （Windows）。

相对路径
从当前工作目录开始的路径。
例如：documents/file.txt 表示当前目录下的 documents 文件夹中的 file.txt 文件。


示例
假设当前工作目录是 C:/Users/user/Documents，以下是一些路径示例及其含义：
当前目录
./file.txt 表示 C:/Users/user/Documents/file.txt 。
父目录
../Downloads/file.txt 表示 C:/Users/user/Downloads/file.txt 。
根目录
C:/Windows/System32/cmd.exe 表示 C:/Windows/System32/cmd.exe 。
绝对路径
C:/Users/user/Documents/file.txt 表示 C:/Users/user/Documents/file.txt 。
相对路径
projects/project1/file.txt 表示 C:/Users/user/Documents/projects/project1/file.txt 。
"""



import json
import random
# from time import sleep # 只导入time里面的sleep

# from time import * 可以导入time的全部，然后就不需要time.sleep(10)了,直接可以sleep(10)
import time
# from time import sleep as s999 # 然后就可以s999(999)
# s999(999)
import timeit

import pyecharts.charts


"""
#python 的文件操作三种打开模式，w：写入，文件不存在会自动创建，存在则清空内容再写入，
#a 是追加模式，指针放在末尾，r 是读模式，
f=open("C:/Users/机械革命/Desktop/HTML/Python/lirics.txt","r",encoding="UTF-8")
#num表示要读的长度，单位是字节，没传入参数读全部
# f_str=f.read()
# print(f_str)

#readlines()可以一行一行的读，然后将每一行放到list里，返回list
 #连续使用read操作，下一次的read会再前一次read的读取过的后面
# f_li=f.readlines()
# print(f_li)
# line1=f.readline()
# print(line1)

# f.seek(0,2)   # 移动到文件开头
# current_position = f.tell() 
# print(current_position) #268 
 #汉字占3字节

# seek(offset, whence) 方法用于改变文件位置指针的位置。参数offset是相对于位置移动的偏移量，whence指示参考点：
# 0：文件开头（默认值）
# 1：当前位置
# 2：文件结尾
# 例如，如果你想将文件指针移动到文件开头，可以这样做：
# file = open('example.txt',  'r+')
# file.seek(0)   # 移动到文件开头
# tell() 方法返回文件指针的当前位置，可以用来确定当前的位置：
# current_position = file.tell() #返回int 的字节数
# print(current_position)

#遍历文件方法
i=0
for line in f:
    i+=1
    if i==10:
        print(line)
    else:
        print(line,end="")
f.close() #不close的话，python会一直占用此文件，使其他应用无法修改此文件

#自动close：
with open("C:/Users/机械革命/Desktop/HTML/Python/lirics.txt","r",encoding="UTF-8") as f:
    print(f.read())
#跳出范围就自动close

# "w"模式写入
f=open("E:/test10.txt","w",encoding="UTF-8")#"w"改成"a"就是追加模式，追加模式不会清空原文件再写
f.write("hhh")
f.flush() #flush:齐刷刷地保存，从缓冲器到存储器
f.close()# close内置flush（）功能

# 经典错误
ff=None
try :
    ff=open("E:/txttxt.txt","r",encoding="UTF-8")
    content=ff.read()
except Exception as e:
    print(f"错误，原因是：{e}")
finally:
    if ff:
        ff.close() #如果try里面出现错误，ff将不会open，则ff.close()就报错，所以加一个if判断，None表示假

try:
    f=open("E:/txt.txt","r",encoding="UTF-8")
    f.close()
    print(f.read())
except Exception as ex: # Exception可捕获任何异常 
    print(f'异常是：{ex}')
    f2=open("E:/txt.txt","w",encoding="UTF-8")
    f2.write("write able")
    
    
    f=open("E:/txt.txt","r",encoding="UTF-8")
    print(f.read())
finally:
    f2.close()
    f.close()

try:
    print(MY_NAME)
except NameError as NE:  # 进变量名等名字未定义的bug才会执行这个except
    print(f"出现异常，异常为{NE}")# 出现异常，异常为name 'MY_NAME' is not defined
try:
    
    a=100/0
except( NameError,ZeroDivisionError) as NE2:  # 进变量名等名字未定义的bug才会执行这个except
    print(f"出现异常，异常为{NE2}") # 出现异常，异常为division by zero
else:
    print("没有异常我会执行，出现异常跑except")
finally:
    print("无论如何我都执行")

# 如果A函数内部有函数B，那么B出现异常会传递给A，然后A可以触发except


def 猜时间_准不准():
    while True:
        time_is=random.randint(1,2) #1-2的随机数
        print(f"你要猜的时间是{time_is}")
        input("输入任意字开始：")
        time_now=time.time() #计时精确度高
        input("输入任意字结束：")
        end=time.time()
        D=(end-time_now)-time_is
        if D<0:
            D=0-D
        D2=1/D
        D2=int(D2)
        if D2>=10000:
            D2=10000
        print(f"你的分数是             {D2:1.0f}","\n")
猜时间_准不准()


# 包
from my_module import * 
a=-999
绝对值(-100)

from my_package import * 

# import my_package.mouduel_1  as mm1
# 也可以 from my_package import mouduel_1 as mm1
# 也可以 from my_package.mouduel_1 import who_i_am1

mouduel_1.who_i_am1()
moduel_2.who_i_am2()

import numpy as np
import pandas as pp


import json
list_a=[{"用户":"王美美","年龄":18},{"用户":"王天岸","年龄":11}]
json_str=json.dumps(list_a,ensure_ascii=False) # 如果json内容包含中文就不要true，不然中文会变成ASCII编码
print(json_str)
json_to_list=json.loads(json_str)
print(json_to_list,type(json_to_list))

import pyecharts as pt
line_1=pt.charts.Line()
line_1.add_xaxis(["第一秒","第二秒","第三秒"])# 时间（s）
line_1.add_yaxis("我的财富",[0,300,8808])
line_1.set_global_opts( # 对图标的全局设置
title_opts=pt.options.TitleOpts(title="我的财富随时间的变化：",pos_left="center",pos_bottom="1%") ,# 对图表的标题设置
legend_opts=pt.options.LegendOpts(is_show=True), # 图例是否展示
toolbox_opts=pt.options.ToolboxOpts(is_show=True), # 工具箱
visualmap_opts=pt.options.VisualMapOpts(is_show=True) 
)
line_1.render()

import statistics 
# 假设这是你的数据列表
data = [1, 2, 3, 4, 5]
# 计算平均数
average = sum(data) / len(data)
print("平均数:", average) 
# 计算求和
total_sum = sum(data) 
print("求和:", total_sum) 
# 计算方差
variance = statistics.variance(data)  
print("方差:", variance) 

import statistics 
list_A=[]
list_D=[]
list_normal=[]
int_i=1
my_sum=100# 每组里面平均数的数量


while True:
    
    while True:
        i=0
        my_list=None
        my_list=[]
        while i<=my_sum:
            my_list.append(random.randint(0,1001)) # 组里数的取值范围
            i+=1
        average = sum(my_list) / len(my_list)
        print(f"average:{average}")
        D = statistics.variance(my_list) 
        print(f"D:{D}")
        break
    list_A.append(average)
    list_D.append(D)
    list_normal.append(int_i)
    int_i+=1 # 平均数组数
    if(int_i==100):
        break
import pyecharts as pt
line_1=pt.charts.Line()
line_1.add_xaxis(list_normal)# 组 以100为组 
line_1.add_yaxis("Average:",list_A)
line_1.set_global_opts( # 对图标的全局设置
title_opts=pt.options.TitleOpts(title="random平均数生成100个数的平均：",pos_left="center",pos_bottom="1%") ,# 对图表的标题设置
legend_opts=pt.options.LegendOpts(is_show=True), # 图例是否展示
toolbox_opts=pt.options.ToolboxOpts(is_show=True), # 工具箱
visualmap_opts=pt.options.VisualMapOpts(is_show=True) 
)
line_1.render()


f=open("C:/Users/机械革命/Desktop/HTML/Python/.vscode/折线图数据/美国.json","r",encoding="UTF-8")
f_jp=open("C:/Users/机械革命/Desktop/HTML/Python/.vscode/折线图数据/日本.json","r",encoding="UTF-8")
str_json=f.read()
str_json_jp=f_jp.read()
J=json.loads(str_json)
J_jp=json.loads(str_json_jp)
#print(type(J)) # dict
trend=J["data"][0]["trend"]
trend_jp=J_jp["data"][0]["trend"]
day=400
option=3
list_x=trend["updateDate"][0:day] # 列表里共有543个数据
Y_option=trend["list"]
Y_option_jp=trend_jp["list"]
Y_list=Y_option[option]['data'][0:day]
Y_list_jp=Y_option_jp[option]['data'][0:day]
# 0
# name : "确诊"
# data
# 1
# name : "治愈"
# data
# 2
# name : "死亡"
# data
# 3
# name : "新增确诊"
# data
#print(list_x)
f.close()
f_jp.close()
import pyecharts
Line1=pyecharts.charts.Line()
Line1.add_xaxis(list_x)
Line1.add_yaxis("美国确诊人数:",Y_list,label_opts=pyecharts.options.LabelOpts(is_show=False))
Line1.add_yaxis("日本确诊人数:",Y_list_jp,label_opts=pyecharts.options.LabelOpts(is_show=False))# 关闭折线图上点的数据标注
Line1.set_global_opts( 
title_opts=pyecharts.options.TitleOpts(title="确诊人数随时间变化图",pos_left="center",pos_bottom="1%") ,
legend_opts=pyecharts.options.LegendOpts(is_show=True), 
toolbox_opts=pyecharts.options.ToolboxOpts(is_show=True), 
visualmap_opts=pyecharts.options.VisualMapOpts(is_show=True) 
)
Line1.render()

import pyecharts
maps=pyecharts.charts.Map()
Data=[
    ("北京市",100),
    ("上海市",55),
    ("广东省",33)
    ]
maps.add("中国地图测试",Data,"china")
maps.set_global_opts(
    visualmap_opts=pyecharts.options.VisualMapOpts(is_show=True,# 不True就单纯地图标点，True的话就会给整个省份上色
    is_piecewise=True, # piecewise:  分段, 分段地, 逐段的 ; 分段显示颜色
    pieces=[
        {"min":1,"max":33,"label":"1-33","color":"#ff0000"}, #广东省将显示为红色
        {"min":34,"max":66,"label":"34-66","color":"#88ff88"},
        {"min":67,"max":100,"label":"1-33","color":"#0000ff"}
    ]
    ),
    
)
maps.render()

f=open("C:/Users/机械革命/Desktop/HTML/Python/.vscode/疫情.json","r",encoding="UTF-8")
map_data=f.read()
import json as jn
jn_map=jn.loads(map_data)
map_list=jn_map["areaTree"][0]['children']
new_list=[]
for one in map_list:
    province=one['name']# 遍历到省份名字
    if province=='上海' or province=='重庆':
        province+='市'
    elif province=='香港':
        province='香港特别行政区'
    elif province=='广西':
        province='广西壮族自治区'
    elif province=='天津':
        province='天津市'
    elif province=='北京':
        province='北京市'
    elif province=='澳门':
        province='澳门特别行政区'
    elif province=='内蒙古':
        province='内蒙古自治区'
    elif province=='西藏':
        province='西藏自治区'
    elif province=='新疆':
        province='新疆维吾尔自治区'
    elif province=='宁夏':
        province='宁夏回族自治区'
    else:
        province+='省'
    # print(province)
    
    province_confirm=one['total']['confirm']# 遍历到各个省份的确诊数
    # print(province_confirm)
    new_list.append((province,province_confirm))
import pyecharts
maps=pyecharts.charts.Map()
Data=new_list
maps.add("中国各个省确诊数",Data,"china") # 把china改成河南省就可以以河南省为图，再以市为元组作为图的子数据
maps.set_global_opts(
    visualmap_opts=pyecharts.options.VisualMapOpts(is_show=True,
    is_piecewise=True, # piecewise:  分段, 分段地, 逐段的 ; 分段显示颜色
    pieces=[
        {"min":1,"max":1000,"label":"1","color":"#5500FF"}, #广东省将显示为红色
        {"min":1001,"max":2000,"label":"2","color":"#9900DD"},
        {"min":2001,"max":3000,"label":"3","color":"#AA00AA"},
        {"min":3001,"max":4000,"label":"4","color":"#DD0099"},
        {"min":4001,"label":"5","color":"#FF0055"}
    ]
    )
)
maps.render("全国疫情地图.html")

import pyecharts as pc
from pyecharts.globals import ThemeType #导入的函数就可以避免点了，有时候点不出来的函数也需要提前导入
bars=pc.charts.Bar() # 柱状图
bars.add_xaxis(["小明","小张","笑笑"])
bars.add_yaxis(
"2001年 他们的钱：",
[999,555,777],
label_opts=pc.options.LabelOpts(position="right")# right即数据从右往左依次按[999,555,777]排序           
)
bars.reversal_axis() 

bars1=pc.charts.Bar()
bars1.add_xaxis(["小明","小张","笑笑"])
bars1.add_yaxis(
"2011年 他们的钱：",
[1999,1555,1777],
label_opts=pc.options.LabelOpts(position="right")
)
bars1.reversal_axis()

bars2=pc.charts.Bar()
bars2.add_xaxis(["小明","小张","笑笑"])
bars2.add_yaxis(
"2041年 他们的钱：",
[3999,3555,3777],
label_opts=pc.options.LabelOpts(position="right")
)
bars2.reversal_axis()

timeLine=pc.charts.Timeline(
    {"theme": ThemeType.DARK} #为时间线系列图表设置主题色
)
timeLine.add(bars,"点0")
timeLine.add(bars1,"点1")
timeLine.add(bars2,"点2")
timeLine.add_schema(
    play_interval=1000, #循环播放时间间隔ms
    is_auto_play=True,
    is_timeline_show=True,
    is_loop_play=True
)
timeLine.render("时间线_基础柱状图.html ")# 渲染带时间线的图表
"""
# num='5.433E+11'
# print(float(num)) # 543300000000.0
from pyecharts.globals import ThemeType
import pyecharts as pc
f=open(".vscode/1960-2019全球GDP数据.txt","r",encoding="UTF-8")
lines=f.readlines()
lines.pop(0)# 删除第一条数据，标头。
dict={} # 按照{1960:[[美国,12300000],[中国,121300000].....],1961:[[美国,112300000],[中国,221300000].....],}的格式存数据
for line in lines:
    list1=line.split(",")
    year=int(list1[0])
    coutry=list1[1]
    GDP=float(list1[2])
    try:
        dict[year].append([coutry,GDP]) # 特别的导入数据方法
    except Exception as E:
        dict[year]=[]
        dict[year].append([coutry,GDP])
years=dict.keys() #取出dict里面的全部key
sorted_years=sorted(years)
# print(sorted_years) # [1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
timeLine=pc.charts.Timeline(
    {"theme": ThemeType.DARK} #为时间线系列图表设置主题色
    )
timeLine.add_schema(
    play_interval=2000,
    is_auto_play=True,
    is_timeline_show=True,
    is_loop_play=True
)

for year1 in sorted_years:
    big_list=dict[year1]
    big_list.sort(key=lambda elament:elament[1],reverse=False)
    top_20=big_list[0:20]
    X_data=[]
    Y_data=[]
    for top in top_20:
        X_data.append(top[0])
        Y_data.append(top[1]/100000000)
    bars=pc.charts.Bar()
    bars.set_global_opts(
        title_opts=pc.options.TitleOpts(title=f"{year1}全球GDP前20排名表")
    )
    bars.add_xaxis(X_data)
    bars.add_yaxis("GDP(单位 亿)",Y_data,label_opts=pc.options.LabelOpts(position='right'))# 柱状图上的数据靠右
    bars.reversal_axis()
    timeLine.add(bars,str(year1))
timeLine.render("1960-2019全球GDP前20排名表.html")




