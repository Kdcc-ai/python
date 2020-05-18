# # 进程间通信:
# # 操作系统提供了很多机制来实现进程间的通信

# # Python的multiprocessing模块包装了底层的机制，
# # 提供了Queue、Pipes等多种方式来交换数据。
# from multiprocessing import Process,Queue
# # 我们以Queue为例 在父进程中创建两个子进程
# # 一个往Queue里写数据 一个从Queue里读数据
# import os,time,random
# def write(q):
#     print('Process to write:%s'%os.getpid())
#     for value in ['A','B','C']:
#         print('Put %s to queue...'%value)
#         q.put(value)
#         time.sleep(random.random())
#         # 生成0-1随机数
# def read(q):
#     print('Process to read: %s' % os.getpid())
#     while True:
#         value=q.get(True)
#         print('Get %s from queue' % value)
# if __name__=='__main__':
#     # q队列是子进程共有的！
#     q=Queue()
#     pw=Process(target=write,args=(q,))
#     pr=Process(target=read,args=(q,))
#     # 启动子进程pw 写入：
#     pw.start()
#     # 启动子进程pr 读取：
#     pr.start()
#     # 等待pw结束：
#     pw.join()
#     # terminate函数 结束工作进程 不再处理
#     # pr进程里面是死循环 无法等待结束 只能强行终止
#     pr.terminate()

# 例子2:
import multiprocessing

def foo(aa):
    ss = aa.get()  # 管子的另一端放在子进程这里，子进程接收到了数据
    print('子进程已收到数据...')
    print(ss)  # 子进程打印出了数据内容...

if __name__ == '__main__':  # 要加这行...

    tx = multiprocessing.Queue()  # 创建进程通信的Queue，你可以理解为我拿了个管子来...
    jc = multiprocessing.Process(target=foo, args=(tx,))  # 创建子进程

    print('主进程准备发送数据...')
    tx.put('有内鬼，终止交易！')  # 将管子的一端放在主进程这里，主进程往管子里丢入数据↑
    jc.start()  # 启子子进程 处于就绪状态


#由于Windows没有fork调用，因此，multiprocessing需要“模拟”出fork的效果
# 父进程所有Python对象都必须通过pickle序列化再传到子进程去，
# 所以，如果multiprocessing在Windows下调用失败了，要先考虑是不是pickle失败了。 



# 知识点:start()方法只是启动它：
# 进程启动三种状态：就绪 堵塞 运行 调用该方法后线程进入就绪状态,等待操作系统给他分配时间片
# start()方法就是调用run()方法 但是start()只是让进程处于就绪状态,run()则是运行状态