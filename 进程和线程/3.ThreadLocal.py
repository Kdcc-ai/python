# # 在多线程环境下 每个线程都有自己的数据
# # 一个线程使用自己的局部变量比使用全局变量更好！
# # 而全部变量的修改必须加锁！

# # 但是局部变量也有问题 在函数调用的时候传递起来就很麻烦！
# # def process_student(name):
# #     std = Student(name)
# #     # std是局部变量，但是每个函数都要用它，因此必须传进去：
# #     do_task_1(std)
# #     do_task_2(std)

# # def do_task_1(std):
# #     do_subtask_1(std)
# #     do_subtask_2(std)

# # def do_task_2(std):
# #     do_subtask_2(std)
# #     do_subtask_2(std)


# # 那么如果用一个全部dict来存放所有的Student对象 然后以thread自身作为key来获得线程对应的Student对象如何？
# import threading
# global_dict={}

# def std_thread(name):
#     std=Student(name)
#     # 这时候把std放到全局变量global_dict中去！
#     global_dict[threading.current_thread()]=std
#     da_task_1()
#     do_task_2()
# def do_task_1():
#     # 不传入std 而是根据当前线程查找
#     std=global_dict[threading.current_thread()]
#     #...
# def do_task_2():
#     # 任何函数都可以查找这个std变量
#     # ...  不错啊
#     pass
# # 但代码有点丑



import threading
# 不用查找dict , ThreadLocal帮你自动做这件事
# 貌似使用和那个方法锁差不多

# 创建全局的ThreadLocal对象 这是ThreadLocal对象
local_school=threading.local()

def process_thread():
    # 这个方法用于获取当前线程关联的student
    std=local_school.student
    print('Hello, %s (in %s)' % (std,threading.current_thread().name))

def process_student(name):
    # 绑定ThreadLocal的student

    # 先绑定 再获取 可以的 
    local_school.student=name
    process_thread()

t1=threading.Thread(target=process_student,args=('Alice',),name='Thread A')
t2=threading.Thread(target=process_student,args=('Bob',),name='Thread B')
t1.start()
t2.start()
t1.join()
t2.join()