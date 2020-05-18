# turtle本身是一个绘图库 配合Python代码

from turtle import *
def drawStar(x,y):
    # 抬起画笔 海龟在飞行(不会画出图案)
    pu()
    # 从当前点去x,y
    goto(x,y)
    # 落下画笔 海龟在爬行(会画出图案)
    pd()
    # 逆时针旋转
    setheading(0)
    for i in range(5):
        # 前进40
        fd(40)
        # 向右转144度 他是直接往前面走的
        rt(144)

# range函数 range(1,11) 从1-10
# range(0,30,5) 0-30  步长为5 0,5,10,15,20,25
for x in range(0,250,50):
    # 每次传入x,0
    drawStar(x,0)
done()
