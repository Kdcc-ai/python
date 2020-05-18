# input默认返回str类型数据，转换成整形数据
import random
secret = random.randint(1,10)
temp=input("猜一下我想的是什么\n")
guess=int (temp)
if guess == 8:
     print("你是我心里的爬虫吗")
     print("哼,猜中了也没有奖励")
else:
    print("猜错了")
    while guess!=8:
       temp=input()
       guess=int (temp)
       if guess>8:
           print("猜大了\n")
       else:
           print("猜小了\n")
print("你终于猜对了")
print("游戏结束")
# python中的缩进原则很重要
x=5
y=6
# 三元操作符
small = x if x<y else y

# assert关键字断言，当这个关键字后边的条件为假的时候
# 程序自动崩溃，抛出异常，可以用这个关键字在程序中置入检查点，当确保程序中的某个条件一定为真才能让程序正常工作时，用这个

# for循环
favorite="fishc"
for i in favorite:
    #  print(i)
    #每次输出i加个换行
    
    #每次输出i加空格 
     print(i,end=" ")

number=["小甲鱼","666"]
for each in number:
     print(each,len(each))

# range函数 BIF内置函数
range(5)
for i in range(5):
# 输出0 1 2 3 4
    print(i)
    print("\n")

range(2,9)
# 输出2 3 4 5 6 7 8
for i in range(2,9):
    print(i)    
    print("\n")
# 输出1 3 5 7 9
range(1,10,2)
for i in range(1,10,2):
    print(i)
    print("\n")