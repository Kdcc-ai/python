# 操作文件和目录 
# 如果我们要操作文件、目录,可以在命令行下面输入操作系统提供的各种命令来完成。
# 比如 dir cp等命令。
# 如果在python程序中执行这些木库和文件的操作怎么办？
# 其实3行的命令也是调用了操作系统提供的接口函数 python的os模块也可以直接调用操作系统提供的接口函数。
import os
print(os.name)
# 操作系统类型
#  如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。

# print(os.uname()) uname()函数在Windows上不提供 所以说os模块的默写函数是跟操作系统相关的

# 操作文件和目录
# 操作文件与目录的函数一部分放在os模块中,一部分放在os.path模块中
print(os.path.abspath('.'))
# 获得当前目录的绝对路径:通常是从盘符开始的路径(在vscode里面是资源管理器里面的路径)

print(os.path.join('D:\\','new test dir'))
# 在某个目录下创建一个新目录 首先把新目录的完整路径表示出来
os.mkdir('D:\\new test dir')
# 然后创建一个目录 可以在D盘中找到了
os.rmdir('D:\\new test dir')
# 删掉一个目录
# 记好了 把两个路径合成一个时 不要直接拼字符串 而是通过os.path.join()函数
# 这样可以正确 处理 不同操作系统 的路径分隔符(理解好)

# 同样 要拆分路径时 也不要直接去拆字符串,而是通过os.path.split()函数
# 输出一个元组 拆分成两个部分 后一个部分总是最后级别的目录或文件名。
print(os.path.split('D:\\new test dir'))
print(os.path.splitext('D:\\hhh\\t.txt'))
# 获取文件的拓展名

# 通过以上python os模块 了解到了合并拆分路径、创建删除目录的函数
# 文件操作使用下面的函数。假设当前目录下有一个test.txt文件：
# # 对文件重命名:
# os.rename('test.txt', 'test.py')
# # 删掉文件:
# >>> os.remove('test.py')
# 还可以重命名文件 删掉文件



# 但是  复制文件的函数居然在os模块中不存在！原因是复制文件并非由操作系统提供的系统调用。

# 幸运的是shuil模块提供了copyfile()的函数
# 你还可以在shutil模块中找到很多使用函数 他们是os模块的补充
import shutil

# 最后看看如何利用python的特性来过滤文件。比如我们要列出当前目录(python程序目录)下的所有目录
print([x for x in os.listdir('.') if os.path.isdir(x)])
# 看需求 列出当前目录下(D盘)的所有目录。。目录 所以后面那个是用来判断是不是目录的
# 列出当前目录(python程序目录)所有的python文件
print([x for x in  os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])



# 练习 1.利用os模块编写一个能实现dir-l输出的程序。
#      2.编写一个程序，能在当前目录的 所有子目录下 查找文件名包含指定字符串的文件 并打印出相对路径
        #第二题用递归    
# 练习1：



# 练习2：查找d:\a目录下包含某一字符串的文件 并输出了绝对路径和相对路径
import os
cha_file=input("输入查找的字符串：\n")
# walk()函数用于通过在目录树中游走输出在目录中的文件名 向上或向
for dir in os.walk(os.path.abspath('.')):
        for x in dir[-1]:
                # 文件目录
           if x.find(cha_file)!=-1:
                y=os.path.join(dir[0],x)
                # 获得文件的绝对路径y
                print('绝对路径为:',y)
                k=y.replace(os.path.abspath('.'),'')
                print('相对路径为:',k)



# import os
# def initial_dir():  #定义一个输入定位到查找目标目录的对象
#     while True:
#         try:
#             search_dir = input('请输入定位目录：\n')
#             os.chdir(search_dir)
#             # 改变当前工作目录到指定路径
#         except FileNotFoundError:
#             print('Error:您输入的内容不是路径地址，或地址不存在，请重新输入\n')
#         else:
#             # os.chdir(search_dir)
#             print('当前路径地址是：' + os.getcwd() + '\n')
#             break
#     return search_dir
# def keywords():  #定义一个让用户输入关键字的对象
#     pass

# def search_folder(kw, i_dir):
#     search_files(kw, i_dir)
#     a = [os.path.abspath(x) for x in os.listdir('.') if os.path.isdir(x)]
#     for y in a:
#         search_folder(kw, y)

# def search_files(kw, i_dir):
#     try:
#         os.chdir(i_dir)
#     except PermissionError:
#         print('部分文件或文件夹不可访问！已跳过！')
#     finally:
#         b = [x for x in os.listdir('.') if os.path.isfile(x) and kw in x]
#         for x in b:
#             print(os.path.abspath(x))
# search_folder(keywords(), initial_dir())