# 接收任务py进程文件:
import time,sys,queue
from multiprocessing.managers import BaseManager

# 创建类似的QueueManager
class QueueManager(BaseManager):
    pass

# 由于这个QueueManager只从网上获取Queue,所以注册时只提供名字:
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 连接到服务器 也就是运行task_master.py的机器
server_addr='127.0.0.1'
print('Connect to server %s...'%server_addr)
# 端口和验证码注意保持与task_master.py设置的完全一致:
m=QueueManager(address=(server_addr,5000),authkey=b'abc')
# 从网络上连接:
m.connect()
# 获得Queue的对象:
task=m.get_task_queue()
result=m.get_result_queue()
# 从task队列取任务,并把结果写入result队列:
for i in range(10):
    try:
        n=task.get(timeout=1)
        print('run task %d * %d'%(n,n))
        r='%d * %d = %d'%(n,n,n*n)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print('task queue is empty.')

# 处理结束
print('worker exit.')

# 任务进程通过网络连接到服务进程 所以要指定服务进程的IP。




# 与上面的master py文件一起 这是一个简单但真正的分布式计算
# 把代码稍加改造 启动多个worker就可以把任务分布到几台甚至几十台计算机上
# 比如把计算n*n的代码换成发送邮件 就实现了邮件队列的异步发送