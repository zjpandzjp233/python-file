import timeit
import os
import platform

operating_system = platform.system() 
def clear_console():
    # 获取操作系统类型
    # 根据操作系统类型选择清屏命令
    if operating_system == "Windows":
        os.system("cls") 
    elif operating_system in ["Linux", "Darwin"]:  # Darwin 是 macOS 的内核名称
        os.system("clear") 
    else:
        print("不支持的操作系统")

path=input("请先输入你需要统计关键词出现次数的文本路径(可包含\"\"哦):")
path=path.strip()
path=path.strip('"')
clear_console()# 调用清屏函数
print(f"已经输入文本路径：{path}")
print()
target=input("请先输入你需要查找的文字，我将告诉其在文本出现的次数:")
clear_console()
def find_target():
    t_len=len(target)
    str1="空"
    index=0
    result=0
    with open(path,"r",encoding="UTF-8") as f:
        while 1==1:
            str1=f.read(1)
            if str1=="":
                break
            if str1==target[index]:
                index+=1
                if index==t_len:
                    result+=1
                    index=0
                else:
                    while 1==1:
                        str1=f.read(1)
                        if str1==target[index]:
                            index+=1
                        else:
                            index=0
                            break
                        if index==t_len:
                            result+=1
                            index=0
                            break
        print(f"关键字:{target}")
        print(f"一共出现 {target} 关键字 {result} 次。")

number_of_runs=1
stmt = f'find_target()'
setup = 'from __main__ import find_target'
    # 使用 timeit 模块进行计时
elapsed_time = timeit.timeit(stmt=stmt,  setup=setup, number=number_of_runs)

    # 计算平均耗时
average_time = elapsed_time / number_of_runs 
print(f"查找关键字的平均耗时：{average_time:.10f} 秒")

print()
if_=input("输入1查看源代码：")
if if_=="1":
    clear_console()
    f=open(__file__,"r",encoding="UTF-8")
    i=0
    while True:
        print(f.readline(),end="")
        i+=1
        if i==74:break
    f.close()

"""
评价、改进：
使用逐行读取代替逐字符读取：
逐字符读取文件会增加I/O操作的次数，而I/O操作通常比CPU操作要慢得多。改为逐行读取可以减少I/O操作的次数。

使用正则表达式：
使用re模块的正则表达式来匹配关键词可能会更高效，因为正则表达式引擎是经过优化的。

避免在循环中使用os.system()：
os.system("cls")或os.system("clear")调用会清除控制台，这在每次循环时都是不必要的，并且会降低性能。可以考虑在循环外调用一次，或者完全去掉。

减少函数调用：
在循环中调用clear_console()函数是不必要的，并且会增加额外的开销。可以考虑在需要的时候手动清理控制台。

使用with语句管理文件：
代码已经使用了with语句来管理文件，这是一个很好的做法，因为它可以确保文件在读取完毕后正确关闭。

缓存文件内容：
如果文件不是特别大，可以考虑将文件内容读入内存，然后对内存中的数据进行搜索，这样可以避免重复的文件I/O操作。

多线程或多进程：
如果文件非常大，可以考虑使用多线程或多进程来并行处理文件的不同部分。

避免使用全局变量：
在函数find_target中使用全局变量target可能会导致意外的副作用。最好将target作为参数传递给函数。

"""