# # os.walk()方法详解
# import os
# # walk(top, topdown=True, οnerrοr=None, followlinks=False)
# # top 是你所要便利的目录的地址
# # topdown 为真，则优先遍历top目录，否则优先遍历top的子目录(默认为开启)
# # onerror 需要一个 callable 对象，当walk需要异常时，会调用
# # followlinks 如果为真，则会遍历目录下的快捷方式(linux 下是 symbolic link)实际所指的目录(默认关闭)
# # os.walk 的返回值是一个生成器(generator),也就是说我们需要不断的遍历它，来获得所有的内容。

# # 每次遍历的对象都是返回的是一个三元组(root,dirs,files)
# # root 所指的是当前正在遍历的这个文件夹的本身的地址
# # dirs 是一个 list ，内容是该文件夹中所有的目录的名字(不包括子目录)
# # files 同样是 list , 内容是该文件夹中所有的文件(不包括子目录)
# # 如果topdown 参数为真，walk 会遍历top文件夹，与top文件夹中每一个子目录。
# os.chdir('D:\\a\\')
# for (root,dirs,files) in os.walk('.'):
#      print(root,dirs,files)


# # 练习：保持目录a的目录结构 在b中创建对应的文件夹 并把a中所有的文件加上后缀 _bak
# for (root,dir,files) in os.walk('.'):
#     new_root=root.replace('.','D:\\b\\',1)
#     # 每次都复制一次新路径 第一次root='.'替换成'D:\\b\\' 
#     # 第二次root='.\\b\\'替换成'D:\\b\\b' 其实就是把root每次前缀替换成new_root
#     if not os.path.exists(new_root):
#         os.mkdir(new_root)
#     # 得到新的root 在该目录下创建新的b目录
#     # python中的replace函数
#     # Python replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，
#     # 如果指定第三个参数max，则替换不超过 max 次。
#     for d in dirs:
#         d=os.path.join(new_root,d)
#         # 在b目录下创建这个目录
#         if not os.path.exists(d):
#             os.mkdir(d)
#     for d in filter((lambda str: str!='txt1.txt'),files):
#         # 运用方法把文件分解为 文件名+扩展名
#         # 在这里可以添加一个filter,过滤掉不想复制的文件类型
#         (shotname,extension)=os.path.splitext(d)
#         #原文件的路径：
#         old_path = os.path.join(root,d)
#         # 新文件的名字 路径
#         new_name = shotname + '_bak' + extension
#         new_path = os.path.join(new_root,new_name)
#         try:
#             # 复制文件
#             open(new_path,'wb').write(open(old_path,'rb').read())
#         except IOError as e:
#             pass
import os
for dir in os.walk('d:\\a'):
    for x in dir[-1]:
        print(x)