# 前面讲到了 函数也是个对象。
# 函数对象赋值给变量
# 所以我们可以通过变量来调用函数
# 函数对象有__name__


# 很多时候 数据读写不一定是文件，也可以在内存中读写。
# StringIO就是在内存中读写str。
# 要把str写入StringIO 需要先创建一个StringIO
from io import StringIO
f=StringIO()
print(f.write('hello'))
print(f.write(' '))
print(f.write('world!'))
print(f.getvalue())

f.seek(-1,1)
print(f.tell())
print(f.read())
# 读的话可以用StringIO本身getvalue()方法 用于获取写入之后的str
# 但是我发现了 如果用read方法 readline方法查看的时候 数据为空！！
# 这时候需要我们修改下文件的指针位置：利用这几条语句
# f.seek(0,0)
# print(f.tell())
# for i in f.readlines():
#   print(i.strip())
# 这能打印出内容 这就涉及了两个方法seek和tell
# tell方法用于获取当前文件读取指针的位置
# seek方法用于移动文件读写指针到指定位置 第一个参数offset偏移量：将文件读取指针到指定位置
# 第二个whence可选值默认为0表示文件开头 1表示相对于当前的位置 2表示文件末尾
# f.seek(p,0) 读取文件指针移动到文文件的第p个字节处
# f.seek(p,1) 在当前位置将文件读取指针移动p个字节 表示相对位置

# 读
f=StringIO('Hello\nHi\nGoodBye')
f2=StringIO('水面细风生，\n菱歌慢慢声\n')
# 读的话可以也可以用StringIO本身getvalue()方法
while True:
    s=f.readline()
    s2=f2.readline()
    if s=='':
        break
    print(s.strip())
    print(s2.strip())
    # 除去那个换行符


# StringIO操作的只能是str,如果要操作二进制数据,就需要使用BytesIO
# BytesIO就是在内存中读写bytes
from io import BytesIO
f=BytesIO()
print(f.write('中文'.encode('utf-8')))
# 写入的不是str而是通过UTF-8编码的bytes
print(f.getvalue())

data='人闲桂花落 夜静春山空'.encode('utf-8')
f=BytesIO(data)
print(f.read())


