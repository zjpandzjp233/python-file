import tkinter as tk

def change_color_black():
    window.config(bg='black')
    window.after(1000, change_color_white)  # 显示黑色1秒后改变

def change_color_white():
    window.config(bg='white')
    window.after(1000, change_color_red)   # 显示白色1秒后改变

def change_color_red():
    window.config(bg='red')
    window.after(7, change_color_white_2) # 显示红色10毫秒后改变

def change_color_white_2():
    window.config(bg='white')
    window.after(10000, close_window)      # 显示白色10秒后关闭窗口

def close_window():
    root.destroy()

root = tk.Tk()
root.title("Color Change Example")
window = root
window.config(bg='black')

change_color_black()  # 开始颜色变化流程

root.mainloop()  # 进入消息循环