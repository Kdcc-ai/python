import time
from turtle import *

setup(width=0.9,height=0.9)
bgcolor('red')
fillcolor('yellow')
color('yellow')
speed(10)

# 主星
begin_fill()
up()
goto(-600,220)
down()
for i in range(5):
    forward(150)
    right(144)
end_fill()
time.sleep(1)

# 第一颗星
begin_fill()
up()
goto(-400,295)
setheading(305)
down()
for i in range(5):
    forward(50)
    left(144)
end_fill()
time.sleep(1)

# 第二颗星(从右画)
begin_fill()
up()
goto(-350,212)
setheading(30)
down()
for i in range(5):
    forward(50)
    right(144)
end_fill()
time.sleep(1)

# 第三颗星(从右画)
begin_fill()
up()
goto(-350,145)
setheading(5)
down()
for i in range(5):
    forward(50)
    right(144)
end_fill()
time.sleep(1)

# 第四颗星
begin_fill()
up()
goto(-400,90)
setheading(5)
down()
for i in range(5):
    forward(50)
    left(144)
end_fill()
time.sleep(1)

done()