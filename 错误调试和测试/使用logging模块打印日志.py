import logging
# 日志分为5个等级 由低到高：DEBUG INFO WARING ERROR CRITICAL

# DEBUG：详细的信息,通常只出现在诊断问题上
# INFO：确认一切按预期运行
# WARNING：一个迹象表明,一些意想不到的事情发生了,或表明一些问题在不久的将来(例如。磁盘空间低”)。这个软件还能按预期工作。
# ERROR：更严重的问题,软件没能执行一些功能
# CRITICAL：一个严重的错误,这表明程序本身可能无法继续运行
# 这5个等级，也分别对应5种打日志的方法： debug 、info 、warning 、error 、critical。默认的是WARNING，当在WARNING或之上时才被跟踪。


# 这5个等级，也分别对应5种打日志的方法： debug 、info 、warning 、error 、critical。
# 默认的是WARNING，当在WARNING或之上时才被跟踪。


# 1将日志输出到控制台
# 开始使用log功能
logging.info('这是 loggging info message')
logging.debug('这是 loggging debug message')
logging.warning('这是 loggging a warning message')
logging.error('这是 an loggging error message')
logging.critical('这是 loggging critical message')
# 因为日志打印等级默认是 WARNING 的级别，所以debug和info是不会打印出来的。

# 日志打印等级默认是WARNING及以上级别 但是有函数basicConfig进行设置logging的等级以及打印格式
# 下面意思是warning级别及以上的就会输出
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
# 打印格式第一个打印日志的时间 第二个打印当前执行程序名 第三个打印当前行号 第四个打印日志等级 第五个打印日志信息
# 知道有这回事就行
logging.debug('这是 loggging debug message')
logging.info('这是 loggging info message')
logging.warning('这是 loggging a warning message')
logging.error('这是 an loggging error message')
logging.critical('这是 loggging critical message')



# # 把日志输出到文件：
# import logging

# # 设置写入日志的文件是 log-20190116.log , 其中使用覆盖写入的 w 模式写日志文件
# logging.basicConfig(level=logging.DEBUG,
#                     filename='./log-20190116.log',
#                     filemode='w',
#                     format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

# # 开始使用log功能
# logging.debug('这是 loggging debug message')
# logging.info('这是 loggging info message')
# logging.warning('这是 loggging a warning message')
# logging.error('这是 an loggging error message')
# logging.critical('这是 loggging critical message')



# # 还可以既把日志输出到控制台又写入到日志文件 记好就行到时候如果用的话再看
# # 使用logger对象
# #!coding=utf-8
# import logging

# # 第一步，创建一个logger  
# logger = logging.getLogger()
# logger.setLevel(logging.INFO)  # Log等级总开关  

# # 第二步，创建一个handler，用于写入日志文件  
# logfile = './log-20190106.txt'
# fh = logging.FileHandler(logfile, mode='a')  # open的打开模式这里可以进行参考
# fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关  

# # 第三步，再创建一个handler，用于输出到控制台  
# ch = logging.StreamHandler()
# ch.setLevel(logging.WARNING)   # 输出到console的log等级的开关  

# # 第四步，定义handler的输出格式  
# formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
# fh.setFormatter(formatter)
# ch.setFormatter(formatter)

# # 第五步，将logger添加到handler里面  
# logger.addHandler(fh)
# logger.addHandler(ch)

# # 日志  
# logger.debug('这是 logger debug message')
# logger.info('这是 logger info message')
# logger.warning('这是 logger warning message')
# logger.error('这是 logger error message')
# logger.critical('这是 logger critical message')