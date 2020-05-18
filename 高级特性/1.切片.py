# 切片 列表或者元组常见操作

# L[1:3] 1,2两个元素
# L[-2]倒数第二个元素 L[-1]D倒数第一个元素...
L=list(range(100))
print(L)
print(L[:10])
# 前十个数
print(L[-10:])
# 后十个数
# ....后十个数 前十个数每两个取一个： L[:10:2]

# 甚至什么都不写 只写[:]就可以原样复制一个list
def trim(L):
    if len(L)==0:
      return L
    else:
      while L[:1]==" ":
        L=L[1:]
      while L[-1:]==" ":
        L=L[:-1]
    return L

if trim('hello  ') != 'hello':
     print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
