# 如果要取最后一个元素，
# 除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素
# 以此类推，可以获取倒数第2个、倒数第3个

# Python中的列表，打了激素的数组，可以存放不同类型的数据
number=["小甲鱼",123,123.4]
print(number)
# append方法只能有一个参数
number.append("666")
print(number)

# 参数只能是列表
number.extend(["A",123])
print(number)

# 可以插入单个列表或者单个数据
number.insert(0,[123])
print(number)

# 可以从列表中获取元素 通过索引值

number.remove(number[0])
print(number)
# 使用remove()删除元素，知道这个元素的具体名字进行直接删除即可

del number[0]
print(number)
# 使用del删除元素，通过列表索引或者整个列表名字进行删除即可
# 删除整个列表之后就没法再输出了
# del number

# 使用pop()删除元素，通过列表索引进行删除
a=number.pop(4)
print(number)
print(a)

# 列表分片
# 经过以上代码，现number列表中剩下有4个元素
# 以下输出都是输出列表的拷贝，列表本身并未发生变化
print(number[1:3])
print(number[:3])
print(number[0:])
# 从右侧开始读取倒数第二个元素: count from the right
print(number[-2])

# 使用分片的方法进行拷贝
member=number[:]
print(member)

# 列表的比较,只是比较第一个元素
a=[123,456]
b=[789,10]
print(a>b)
# 列表的连接,只能两个列表进行连接，连接后形成新的列表
c=a+b
print(c)
# 列表*
print(a*3)

# in操作符,在for循环中用到过,在这儿用于判断元素是否在列表中
# 这里用c列表作用例

# 返回true
print(123 in c)

# 返回true
print("小甲鱼" not in c)

# 返回false
d=["小甲鱼",[123,456],"hhh"]
print(123 in d)

# 返回true
print(123 in d[1])

# 与访问二维数组类似
print(d[1][1])

# 输出列表中常见的一些方法,list字典
print(dir(list))

# 输出结果为1,小甲鱼字符串出现的次数
print(d.count("小甲鱼"))
# 输出结果为0,小甲鱼字符串第一次出现的位置
print(d.index("小甲鱼"))



e=[(2,2),(3,4),(4,1),(1,3)]
# 列表反转
e.reverse()
print(e)

# sort()函数L两个参数,一个key一个reverse
# 默认升序输出
e.sort()
print(e)
# 改变参数,降序输出
e.sort(reverse=True)
print(e)

# 指定列表中的元素排序来输出列表
def takeSecond(elem):
    return elem[1]
# 指定第二个元素排序,key代表键值,指定每个元素的第二个元素进行排序
e.sort(key=takeSecond)

# 列表可以进行比较,进行连接,与数进行相乘
list1=[123,456]
list2=[234,123]
print(list1>list2)
list1*=3
print(list1)
# 从第三个元素进行数,数到第六个,找到123的位置
print(list1.index(123,3,7))
print(123 in list1)
print(333 not in list1)



# clear()函数说明

# for line in lines:
    # print(line)
    # for x in jieba.lcut(line):
        # print(x)
        # if x not in stopwords:
            # text1.append(x)
# 上面语句不用管，看下面就好
text1=[123,123]
text1.clear()
text2=text1
corpora_documents=[]
corpora_documents.append(text2)
print(corpora_documents)
text1.clear()
    # 此程序输出结果为空
    # text2=text1#相当于将声明的两个对象的指针指向同一块内存空间即text1所在的内存空间
    # corpora_documents.append(text2)#Python采用的应该是延迟加载，也就是说这里corpora_documents只是将指针指向了text2的内存地址，并没有直接就将text2里面的内容加载进来。
    # print(corpora_documents)
    # text1.clear()#clear()就相当于擦除了text1中的内容，即text2指向了一个空的内容，由于Python延迟加载的特性也就造成了后面打印出来的corpora_documents的内容为空
    # print(corpora_documents),输出为空
    #如果将128句写成text1=[],127行输出就是想要的结果了,这是Python的内存管理机制与Java不同的方面