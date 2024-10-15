import os

# os.rename(r"F:\os_test\1.txt",r"F:\os_test\250525052505.txt") # 重命名

# os.remove(r"F:\os_test\垃圾.txt") # 删除
# os.rmdir(r"F:\os_test\a\empty") # 删除空文件夹

# os.mkdir(r'F:\os_test\python_maded') # 创建空文件夹

# print(__file__) # C:\Users\机械革命\Desktop\HTML\Python\.vscode\os\os-1.py
# print(os.getcwd()) # c:\Users\机械革命\Desktop\HTML\Python  # get current working directory

# print(os.listdir(r'F:\os_test'))  # 返回指定文件夹内的文件名列表

#print(os.path.isfile(r"F:\os_test\1.txt")) # True  判断是不是文件（非文件夹）

# print(os.path.exists(r"F:\os_test\a\888888888.txt")) # True # 用于检查指定路径是否存在。这个函数返回一个布尔值，如果路径存在，则返回 True，否则返回 False
# print(os.path.exists(r"F:\os_test\a"))  # True

# print(os.path.getsize(r"E:\Qingfeng\HeyboxAccelerator\454f8d67-88e8-401a-aceb-566676e08ecf.exe")/(1024**2)) # 文件大小，MB

# print(os.path.basename(r"F:\os_test\654.txt")) # 654.txt    获取文件名和路径



import re
str_1='1fe5f1.txt'
print(str_1[0:7])
def apart_file_name(str1:str):
    s=re.search(r'\.',str1)
    if s!=None:
        return s.span()[1]
print(apart_file_name(str_1))
"""
1fe5f1.
(6, 7)
请按任意键继续. . .
"""