# 收获 python文件名不能随便起!!如果这个文件取名为datetime的话
# 一个文件就是一个模块 python解释器取datetime文件里面去找datetime类 自然没有 所以报错


# 处理日期和时间的标准库
from datetime import datetime

# 要知道模块与类的关系
# 从datetime模块里面导入datetime类


# 1.获取当前日期和时间
now = datetime.now()
print(now)
print(type(now))


# 2.获取指定日期和时间
dt = datetime(2020, 3, 29, 12, 20)
print(dt)
# datetime->timestamp
# 记住python的timestamp是一个浮点数 如果有小数位 小数位表示毫秒数
print(dt.timestamp())

# 其实 在计算机中 时间实际上是用数字表示的。
# 1970年1月1日00:00:00 UTC+00:00 时区 的 时刻 称为epoch time，记为0
# （1970年以前的时间timestamp为负数）
# 当前时间是相对于epoch time的秒数（这个秒数就是timestamp）
# 可以认为：
# timestamp = 0 = 1970-1-1 00:00:00 UTC+0:00
# 对应的北京时间是:
# timestamp = 0 = 1970-1-1 08:00:00 UTC+8:00
# 总结：我感觉是上面那个timestamp的时间与时区毫无关系
# timestamp一旦确定 其UTC时间就确定了 转换到任意时区的时间也是完全确定
# 计算机存储的当前时间是以timestamp表示的
# 因为全球各地的计算机timestamp在任意时间都是完全相同的 所以存储这个

# timestamp->datetime
# timestamp是一个浮点数 它没有时区的概念(全球计算机在某一时刻存的timestamp要相同)
# 下面这个转换是timestamp和本地时间做转换 而本地时间是当前操作系统设定的时区
t = 1429417200.0
print(datetime.fromtimestamp(t))
# 下面这个转化是timestamp和UTC标准时区的转换
t = 1429417200.0
print(datetime.utcfromtimestamp(t))


# 3.str转换为datetime
# 用户输入的日期是字符串 把str转换为datetime
cday=datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
# %Y 四位数年份表示 %m 月份 %d 月内的某一天 %H 24小时制小时数 %M 分钟数 %S 秒
# 后面这个规定了日期和时间部分的格式 https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
print(cday)


# 4.datetime转换为str
# datetime对象转换为str给用户
now=datetime.now()
print(now.strftime('%a,%b  %d %H:%M'))
# 这个格式化形式很重要


# 5.datetime加减 对日期和时间进行加减==把datetime往后或往前计算
# 方法
from datetime import timedelta
now = datetime.now()
print(now)
print(now+timedelta(hours=10))
print(now-timedelta(days=1))
print(now+timedelta(days=2,hours=12))


# 6.本地时间转换为UTC时间（系统本地是UTC+8:00）
# 本地时间是指系统设定时区的时间~~~ 相对那个UTC时间来说的
# 本地时间转换为UTC时间：给datetime类型时间设定时区属性
from datetime import timezone
tz_utc_8=timezone(timedelta(hours=8))
# 创建时区UTC+8:00
now=datetime.now()
print(now)
# 拿到本地时间
dt=now.replace(tzinfo=tz_utc_8)
# datetime的时区属性强制设置为UTC+8:00(北京时间恰好是相对UTC+8:00 代码正确)
print(dt)


# 7.时区转换（拿到当前UTC时间->任意时区时间 任意时区的时间->其他时区的时间）
# 另外时区的datetime才可以通过astimezone方法->转换到任意时区
# 其实就是拿到一个datetime->获取其正确的时区->强制设置其他时间为这个时区(这个时区其实就相当于基准时间)
# 拿到当前UTC时间
utc_dt=datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
# 转换为北京时间：给datetime类型时间设定时区属性
bj_dt=utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
# 转换为东京时间：给datetime类型时间设定时区属性
tokyo_dt=utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)
# bj_dt->tokyo_dt
tokyo_dt2=bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)




# 小结 datetime表示时间默认是本地系统的时间 时区信息是相对UTC 8个小时的时间
#      timestamp表示的时间与时区完全无关
#      datetime timestamp之间可以转换
#      datetime与str之间也可以相互转换
#      一个时区的时间可以通过设定时区(前提这个datetime本身必须是有时区属性的)转换成另外一个时区的时间



# ————————————————————————————————————————————————————
# 作业
import re
def to_timestamp(dt_str,tz_str):
    #'2015-6-1 08:10:30', 'UTC+7:00'
    tz = re.search(r'[+-][0-9]{1,2}:[0-9]{2}',tz_str)
    hours=tz.group().split(':')[0]
    cday = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    if(hours[1]=='0'):
      tz_utc=timezone(timedelta(hours=int(hours[0]+hours[2])))
    else:
      tz_utc=timezone(timedelta(hours=int(hours[0]+hours[1])))
    cdaytz = cday.replace(tzinfo=tz_utc)
    return cdaytz.timestamp()
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')