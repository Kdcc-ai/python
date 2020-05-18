from turtle import *
# 使用递归 绘制出非常复杂的图形
# 设置色彩模式是RGB 使用RGB整数模式来修改颜色
# 设置色彩的一个方式
colormode(255)

# 左转90度
lt(90)

lv = 14
l  = 120
s = 45

# 初始化设置笔的宽度
width(lv)

# 初始化RGB颜色
r=0
g=0
b=0
pencolor(r,g,b)

penup()
bk(l)
pendown()
fd(l)

def draw_tree(l,level):
    global r,g,b
    # 获得宽度
    w=width()

    # 缩短宽度
    width(w*3.0/4.0)
    #改变颜色 
    r=r+1
    g=g+2
    b=b+3
    pencolor(r%200,g%200,b%200)

    l = 3.0/4.0*l

    lt(s)
    fd(l)

    if level < lv :
        draw_tree(l,level+1)
    bk(l)
    rt(2*s)
    fd(l)
    
    if level < lv:
        draw_tree(l,level+1)
    bk(l)
    lt(s)

    # restore the previous pen width
    width(w)


speed('fastest')
draw_tree(l,4)
done()