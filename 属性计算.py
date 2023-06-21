from tkinter import *
def show(a1):
	c1.delete(0,"end")
	e1 = a1.get()
	e1 = float(e1)
	#定义个E1来获取输入框的字符，然后转为浮点数
	e2 = a2.get()
	e2 = float(e2)
	e3 = a3.get()
	e3 = float(e3)
	
	e = (1.5*e1+e2)*(e3/10)
	#计算式尚未确定，这里是一个测试案例
	e = '{:.2f}'.format(e) #四舍五入，保留小数点后两位
	c1.insert(0,e)

top = Tk()  #通过Tk()方法建立一个根窗口，top是自定义的名字

top.title("计算")  #窗口的标题
top.geometry('500x300')  #设置主窗口大小，注意中间对的符号是小写字母x
#创建文本标签Label,top是第一个参数为父窗口，text是标签内容
#设置位置参数，使用place方法可将控件放在指定位置，
#place()方法中窗口显示区左上角是(0,0),x是向右递增，y是向下递增

Label(top,text = "这是一个标签").grid(row = 0,column = 0,padx=30,pady=5)

contentVar = StringVar(top, '')
# 创建单行文本框
c1 = Entry(top, textvariable=contentVar)
# 设置文本框为只读设为只读时似乎无法写入数据，当然可能有其他处理方法暂时不清楚。
#c1['state'] = 'readonly'
# 设置文本框坐标及宽高
c1.grid(row=0,column=0,padx=30,pady=5)




#创建按钮，text是功能按钮的名称

Button1 = Button(top,text = "enter",command=lambda:show(a1))
Button1.grid(row=2,column=1,padx=30,pady=5)
a1 = Entry(top,width=10)
a1.grid(row=1,column=0,padx=10,pady=5)
#因为 Entry 方法涉及人机交互，其后不能直接使用 grid 方法，要分开成两句
a2 = Entry(top,width=10)
a2.grid(row=1,column=1,padx=30,pady=5)
a3 = Entry(top,width=10)
a3.grid(row=1,column=2,padx=30,pady=5)
top.mainloop()
