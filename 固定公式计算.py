import tkinter as tk
# 导入 tkinter 模块

# 定义 calculate 函数，用于计算结果并在标签中展示
def calculate():
 # 获取输入框 entry1、entry2 和 entry3 中的值，并将其转化为浮点数类型
    x = float(entry1.get())
    y = float(entry2.get())
    z = float(entry3.get())
    # 计算结果，并保留一位小数
    result = round(x + 2*y + z/10, 1)
    # 将计算结果展示在标签 display 中（将浮点数转换成字符串）
    
    # 如果计算结果非空，则显示边框并设置文本内容
    if result:
        display.config(text=str(result), bd=2, relief='groove')
    # 否则，隐藏边框
    else:
        display.config(text="", bd=0)

# 定义 clear 函数，用于清空输入框和标签中的内容
def clear():
    # 清空输入框 entry1、entry2 和 entry3 中的内容
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)
    # 清空标签 display 中的内容
    display.config(text="")

# 创建一个窗口 window，设置标题和大小
window = tk.Tk()
window.title("计算工具")
window.geometry("500x500")

# 创建三个输入框，分别对应 x、y 和 z 的值
entry1 = tk.Entry(window)
entry1.pack(pady=15)

entry2 = tk.Entry(window)
entry2.pack(pady=15)

entry3 = tk.Entry(window)
entry3.pack(pady=15)

# 创建两个按钮，分别对应计算和清除操作
# 将计算和清除按钮居中对齐，并添加一定间隔
button1 = tk.Button(window, text="计算", command=calculate)
button1.place(relx=0.35, rely=0.7, anchor=tk.CENTER) 

button2 = tk.Button(window, text="清除", command=clear)
button2.place(relx=0.65, rely=0.7, anchor=tk.CENTER)

# 创建一个标签 display，用于展示计算结果
# 将计算结果标签居中显示，并增大尺寸
display = tk.Label(window, bd=0, width=20, height=4, font=("Arial", 16))
display.place(relx=0.5, rely=0.45, anchor=tk.CENTER)

# 进入窗口的主循环，等待用户操作
window.mainloop()
