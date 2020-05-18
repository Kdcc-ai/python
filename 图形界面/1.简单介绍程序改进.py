# 改进一下 加入一个文本框 让用户可以输入文本—>点击按钮->弹出消息对话框
from tkinter import*
import tkinter.messagebox as messagebox
class Application(Frame):
    def __init__(self):
        # 指定这个控件的master
        Frame.__init__(self,master)
        # 几何状态管理方法 包装
        self.pack()
        self.creatWidgets()
    def creatWidgets(self):
        # 输入控件 用于显示简单的文本内容
        # Entry(master,option...)
        # master文本框的父容器 options可选项
        # 例如Entry(self,text='  ') 设置了文本框的属性名
        self.nameInput=Entry(self)
        self.nameInput.pack()

        # Button(master,option=value,...) 
        # master是按钮的父容器 后边可选text：按钮的文本内容...  command按钮关联的函数 按钮被点击执行该函数
        self.alertButto=Button(self,text='Hello',command=self.hello)
        self.alertButto.pack()
    def hello(self):
        # Entry.get()获取文本框的值
        name=self.nameInput.get() or 'world'
        # messagebox用于显示你应用程序的消息框
        messagebox.showinfo('Message','Hello,%s'%name)
app=Application()
# 设置窗口标题
app.master.title('Hello world')
# 主消息循环
app.mainloop()
    
