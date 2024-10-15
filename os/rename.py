import os
import tkinter as tk
from tkinter import filedialog
import re
def select_folder():
    # 创建一个 Tkinter 根窗口，但不显示
    root = tk.Tk()
    root.withdraw()

    # 打开文件夹选择对话框
    folder_path = filedialog.askdirectory()

    # 如果用户取消选择，folder_path 将为 ''
    if folder_path:
        print(f"用户选择的文件夹路径是: {folder_path}")
    else:
        print("用户取消了选择")
    return folder_path

def apart_file_name(str1:str):
    s=re.search(r'\.',str1)
    if s!=None:
        return s.span()[1]


input('按下任意键开始选择一个要批量修改文件后缀的文件夹：')
back_name=input('输入要改成的后续：')
folder_path=select_folder() # C:/Users/机械革命/Downloads/LANDrop/VNU_OUTPUT
for one in os.listdir(folder_path):
    file_path=folder_path+r'/'+one
    if os.path.isfile(file_path) :
        dot_index=apart_file_name(one)
        fore_name=one[0:dot_index]
        new_file_name_path=folder_path+r'/'+fore_name+back_name
        print(new_file_name_path,'new_file_name_path')
        os.rename(file_path,new_file_name_path)

