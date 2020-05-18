# python支持图形界面的第三方库 包括Tk wxWidgets等。。

# Tkinter是Python自带的 可以直接使用

# Python代码调用内置的Tkinter(Tkinter封装了访问Tk的接口)->Tk调用操作系统提供的本地GUI接口 完成最终的GUI
# Tk是一个图形库 支持多个操作系统 使用Tcl语言开发
from tkinter import *
class Application(Frame):
 def __init__(self,master=None):
    Frame.__init__(self,master=None)
    self.pack()
    self.creatWidgets()
    # self代表实例对象 调用类中方法
 def creatWidgets(self):
     self.helloLable=Label(self,text='Hello world!')
     self.helloLable.pack()
     self.quitButton=Button(self,text='Quit',command=self.quit)
     self.quitButton.pack()
# 和java差不多  Button、Lable、输入框等 都是一个Widget(装置)
#              Frame是容纳其他Wideget的Widget
# 故所有的Wideget组合起来就是一棵树
# pack方法把Widget加入到父容器中 并实现布局
# grid方法也可以实现布局

# 上面步骤：创建一个Lable和一个Button->Button被点击 出发self.quit()方法
app=Application()
# 设置窗口标题：
app.master.title('Hello world')
# 主消息循环
# app.mainloop()