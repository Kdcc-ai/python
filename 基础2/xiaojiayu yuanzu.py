# 元组，元组不能随意插入删除元素，不能随意改变，跟字符串一样，
# 不能原地排序等,讨论创建元素和列表的区别
# tuple类型
# 输出int型
temp=(123)
print(type(temp))
# 输出tuple型
temp2=(123,)
print(type(temp2))
# 输出tuple型
temp3=1,2,3
print(type(temp3))
# 输出tuple型
temp4=()
print(type(temp4))

# 记住以下区别
print(8*(8))
print(8*(8,))
# 同样可以更新,删除元组,插入元素
temp5=("jjj","ccc","ddd","ggg")
temp5=temp5[:2]+("怡景",)+temp5[2:]
print(temp5)