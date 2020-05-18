# 有时候会用到
# 其实就是用{}替换原来的%来实现格式化输出
print("{} {}".format("hello", "world"))  # 不设置指定位置，按默认顺序
print("{0} {1}".format("hello", "world")) # 设置指定位置
print("{1} {0} {1}".format("hello", "world")) # 设置指定位置

# 还可设置参数
print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))
# 通过列表索引设置参数
my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的

# 还可以传入对象
class AssignValue(object):
    def __init__(self, value):
        self.value = value
my_value = AssignValue(6)
print('value 为: {0.value}'.format(my_value))  # "0" 是可选的



# 数字格式化 一些格式化方法 用到的时候使用即可
print("{:.2f}".format(3.1415926))

print ("{} 对应的位置是 {{0}}".format("runoob"))