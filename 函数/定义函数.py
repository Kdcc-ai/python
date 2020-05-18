# 定义一个函数要用def语句,
# 依次写出函数名、括号、括号中的参数、冒号：
def my_abs(x):
    # return
    if x>=0:
        return x
    else:
        return -x
print(my_abs(-5))
# 如果加上ruturn则输出None

# 空函数：定义一个什么事也不做的空函数 可以用pass语句：
def nop():
    pass
# pass语句什么都不做，那有什么用？
# 实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
age=5
if age >= 18:
    pass
# 缺少了pass，代码运行就会有语法错误。

# 参数检查：通过参数个数 参数类型 函数内部语句
# 一个通过参数类型进行检查的函数
# def my(x):
    # if not isinstance(x,(int,float)):
    #   raise TypeError("bad operand type")
    # if x>=0：
    #   return x
    # else：
    #   return -x
# print(my("A"))

# 返回多个值：
import math
def move(x,y,step,angle=0):
    nx=x+step*math.cos(angle)
    ny=y-step*math.sin(angle)
    return nx,ny
x,y=move(100,100,60,math.pi/6)
print(x,y)
r=move(100,100,60,math.pi/6)
print(r)
# 其实这个的返回值是一个tuple

# 作业：
# 计算一元二次方程
def quadratic(a,b,c):
    if a == 0:
      x1 = -(c/b)
      x2 = x1
    else:
      x1=(math.sqrt(b**2-4*a*c)-b)/(2*a)
      x2=-(math.sqrt(b**2-4*a*c)+b)/(2*a)
    return x1,x2

print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))
if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')