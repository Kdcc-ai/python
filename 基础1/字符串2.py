# 字符串和编码:

# Unicode出现原因,把所有语言都统一到一套编码里，这样就不会再有乱码问题了。
# ASCII编码是1个字节，而Unicode编码通常是2个字节。
# 如果把ASCII编码的A用Unicode编码，只需要在前面补0就可以，因此，A的Unicode编码是00000000 01000001。

# 但是如果文本中既有英文又有中文,那么全部用Unicode就会有浪费
# 所以，本着节约的精神，又出现了把Unicode编码转化为“可变长编码”的UTF-8编码
# UTF-8编码把一个Unicode字符根据不同的数字大小编码成1-6个字节

# 计算机系统通用的字符编码工作方式：
# 在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码。

# python中的字符串是以Unicode编码的,所以Python输出字符串支持多种语言！！
# 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：
# >>> ord('A')
# 65
# >>> ord('中')
# 20013
# >>> chr(66)
# 'B'
# >>> chr(25991)
# '文'

# 如果知道字符的整数编码，还可以用十六进制这么写str：
# >>> '\u4e2d\u6587'
# '中文'

#这个是bytes类型的数据,每个字符都只占用一个字节 。因为如果Python中的字符串
#在网络中传输啥的,需要将str变为以字节为单位的bytes
x=b"ABC"

# 以Unicode表示的str通过encode()方法可以编码为指定的bytes，例如：
# >>> 'ABC'.encode('ascii')
# b'ABC'
# >>> '中文'.encode('utf-8')
# b'\xe4\xb8\xad\xe6\x96\x87'
# >>> '中文'.encode('ascii')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)
# 纯英文的str可以用ASCII编码为bytes，内容是一样的，含有中文的str可以用UTF-8编码为bytes。含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错。
# 在bytes中，无法显示为ASCII字符的字节，用\x##显示。

# 反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法：
# >>> b'ABC'.decode('ascii')
# 'ABC'
# >>> b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
# '中文'
# 如果bytes中包含无法解码的字节，decode()方法会报错：
# >>> b'\xe4\xb8\xad\xff'.decode('utf-8')
# Traceback (most recent call last):
#   ...
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 3: invalid start byte
# 如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节：
# >>> b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')
# '中'

# len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数：
# >>> len(b'ABC')
# 3
# >>> len(b'\xe4\xb8\xad\xe6\x96\x87')
# 6
# >>> len('中文'.encode('utf-8'))
# 6

# 在操作字符串时，我们经常遇到str和bytes的互相转换。
# 为了避免乱码问题，应当始终坚持使用UTF-8编码对str和bytes进行转换。

print("中文")
# 比较操作符 逻辑操作符 成员操作符同样适用
str="I Love fishc.com"
# 第六个字符串之前的所有字符
print(str[:6])

print(str[6])

# 输出I Love插入了字符串 fishc.com
str=str[:6]+"插入了字符串"+str[6:]

# 字符串常用的一些小方法,但是字符串本身并未改变
str2="xiaoxie"
# 首字母转换成大写输出
print(str2.capitalize())
# 全部转换成小写,大写输出
str3="DAxIe"
print(str3.lower())
print(str3.upper())
# 打印出现次数
str4="adaddfjl"
print(str4.count("ad"))
# 以什么结束
print(str4.endswith("l"))
# 给空格,默认8个空格
str5="I\tlove\tfishC.com!"
print(str5)


# 查找方法
a="卓越人生,从现在开始"
print(a.find("人",0,5))

# 修改方法
# 新子串代替旧子串
print(a.replace("卓越人生","精彩人生",1))
# 分隔符
a="高中 and 初中 and 大学 and 校企合作"
# 返回列表，默认以空格为分隔符进行分隔,分隔成num+1个字符串
list1=a.split("and")
list2=a.split("and",2)
print(list1)
print(list2)
# 是否符合标题化 （所有单词都是以大写开始，其余字母均小写）
str6="Title"
print(str6.istitle())
str6="TitlE"
print(str6.istitle())
# 12345字符串以TitlE字符串隔开
print(str6.join("12345"))

# 一些留余方法
# 字符串居中，占40空格
print(str3.center(40))
# 左对齐
print(str3.ljust(10,"."))
# 右对齐
print(str3.rjust(10,"."))







# 字符串格式化方法,和c语言一样用%进行
# print('%2d-%02d' % (3, 1)),右对齐
# print('%.2f' % 3.1415926)
# 有些时候，字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%：
# >>> 'growth rate: %d %%' % 7
# 'growth rate: 7 %'

str7="{0} love {1}.{2}".format("I","Fishc","com")
print(str7)

#str8="{a} love {b}.{c}".format("I","Fishc","com")是错误的
str8="{a} love {b}.{c}".format(a="I",b="Fishc",c="com")
print(str8)

str9="{{0}}".format("不打印")
print(str9)

str10="{0:.1f}{1}".format(27.654,"G8")
print(str10)

# Python中的字符串格式化 %s %d %f %e等,知道就好,和c语言差不多
# 跟c差不多 %一定要一一对应的关系
# %o八进制 %x十六进制
print("%c" % 97)
print("%cxxxx" % 97)

print("%c %c %c"%(97,98,99))
print("%s"%"I love fishc")
print("%d %d = %d"%(97,98,97+98))

print("%f"%16.7)
print("%.2f"%16.7)

# 右对齐
print("%7.2f"%16.7)

# 左对齐
print("%-7.2f"%16.7)
# 在正数前面加+
print("%+d"%15)
print("%+d"%-15)

