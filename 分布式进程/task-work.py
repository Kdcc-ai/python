# 在Thread和Process中，应当优选Process，因为Process更稳定，
# 而且，Process可以分布到多台机器上，而Thread最多只能分布到同一台机器的多个CPU上。

# multiprocessing的子模块managers 把多进程分布到多台机器上->一个服务进程作为调度者将任务分布到多个进程中(依靠网络通信)
# 分布在不同电脑上

# 举个例子 如果我们已经有一个通过Queue通信的多进程程序在同一台机器上运行，现在，由于处理任务的进程任务繁重
# 希望把发送任务的进程和处理任务的进程分布到两台机器上。怎么用分布式进程实现？？
# 原来有的Queue可以继续使用 通过managers模块把Queue通过网络暴毙出去 就可以让其他机器的进程访问Queue了





# 具体实现 发送任务进程py文件

# 首先是服务进程 服务进程负责 启动Queue 把Queue注册到网络上 然后往Queue里面写任务
# task_master.py
import random,time,queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support
# 发送任务的队列: 同样我们可以指定任务数
task_queue=queue.Queue()
# 接收结果的队列:
result_queue=queue.Queue()

# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass

def getttask():
    global task_queue
    return task_queue
def gettesult():
    global result_queue
    return result_queue
def master_task():
# 把两个Queue都注册到网络上,callable参数关联了Queue对象：
  QueueManager.register('get_task_queue',callable=getttask)
  QueueManager.register('get_result_queue',callable=gettesult)
# 绑定端口5000 设置验证码'abc': Linux下address留空为本机 Windows下不能留空
  manager=QueueManager(address=('127.0.0.1',5000),authkey=b'abc')
# 字节类型的数据
# 启动Queue
  manager.start()

# 获得通过网络进行访问的Queue对象:
  task=manager.get_task_queue()
  result=manager.get_result_queue()
# 放几个任务进去:
  for i in range(10):
    # random函数用法 random.random()随机返回生成的一个实数,在[0，1)范围内
    # random.randint(0,99)随机返回0~99之间的整数
    n=random.randint(0,10000)
    print('Put tnask %d...' % n)
    task.put(n)
# 从result队列读取结果
  print('Try get results...')

  for i in range(10):
    r=result.get(timeout=10)
    print('Reault: %s' % r)

# 关闭:
  manager.shutdown()
  print('master exit.')
# 注意 当我们在一台机器上写多进程程序时候,创建的Queue可以直接拿来用 但是分布式进程环境下,添加任务到Queue不可以直接对原始的task_queue进行操作
#那样就绕过了QueueManager的封装,必须通过manager.get_task_queue()获得的Queue接口添加
if __name__=='__main__':
    freeze_support()
    master_task()