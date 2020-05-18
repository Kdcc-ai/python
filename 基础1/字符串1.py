# 字符串以及转义字符
# 字符串如果既包含' 又包含" 用转义字符标记
# 输出I'm "OK"!
print('I\'m \"OK\"!')
# 转义字符\可以转义很多字符，比如\n表示换行，\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\
# 可以在Python的交互式命令行用print()打印字符串看看,要理解转义字符

# 转义了n
str6="c:\now"
print(str6)
# 转义了\
str2="c:\\now"
print(str2)
# 输出\ 换行 \,理解好
print('\\\n\\')

# r''表示''内部的字符串默认不转义,输出c:\now
str3=r"c:\now" 
print(str3)

# 用'''...'''的格式表示多行内容,注意...是提示符，不是代码的一部分：
print('''line1
ooo line2
hhh line3''')
print(r'''hello,\n
world''')




print(1e10)
#Python中的变量转换函数 BIF转换函数 float() str() int()
# 不能将某一变量重复赋不同类型的值，这样会冲突
# 例如c已经是int型了 不能再将float型等数据赋值给它
a=5.99
b=int(a)
print(b)

c='520'
d=float(c)
d=5
print(d)

e=str(c)
print(e)

# type函数用于判断数据类型以及isinstance函数用于判断两个变量类型是否一致
print(isinstance("abc",str))

# 输出数据的类型
print(type("hhh"))
print(type(123))

#制表符是固定位置,这个要理解 
print('welcome\t\\')
print('shoot\t\\')