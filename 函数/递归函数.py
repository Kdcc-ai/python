# 尾递归函数 是把每一步的乘积传入到函数当中去
# 例如
def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
# 理解好 Python解释器也没有做优化，所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出
# 汉诺塔
def move(n,a,b,c):
    if n==1:
        print("move",a,"->",c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)


move(4,"A","B","C")