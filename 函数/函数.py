# http://docs.python.org/3/library/functions.html#abs 函数查看文档
a=[1,2,3]
print(a.reverse()) 
# 输出None 返回一个迭代器

# 类型转换函数 str() float() int()
# 函数名其实就是指向一个函数对象的引用,完全可以把函数名赋给一个变量
# >>> a = abs # 变量a指向abs函数
# >>> a(-1) # 所以也可以通过a调用abs函数
# 输出1

# 调用函数作业：
n1=255
n2=1000
i=(n1,n2)
for x in i:
    print(hex(x))

