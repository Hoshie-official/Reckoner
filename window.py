from tkinter import *
top = Tk()  #通过Tk()方法建立一个根窗口，top是自定义的名字
top.title("计算")  #窗口的标题
top.geometry('500x300')  #设置主窗口大小，注意中间对的符号是小写字母x
#创建文本标签Label,top是第一个参数为父窗口，text是标签内容
#设置位置参数，使用place方法可将控件放在指定位置，
#place()方法中窗口显示区左上角是(0,0),x是向右递增，y是向下递增
#随便加点东西
Label(top,text = "标签测试").place(x = 200,y = 100)

#创建按钮，text是功能按钮的名称

Button(top,text = "enter").place(x = 220,y = 150)
top.mainloop()
