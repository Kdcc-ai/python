# 就是lambda函数 关键字lambda表示匿名函数，冒号前面的x表示函数参数。
# 但他就只能有一个参数 返回一个值 甭写return
# 另外 匿名函数也是一个对象 可以把它赋给别人;同样它也可以作为返回值

# 作业
L2 = list(filter(lambda n: n % 2 == 1, range(1, 20)))
print(L2)