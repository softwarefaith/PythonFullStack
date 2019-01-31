#进程:每次创建一个进程操作系统会给这个进程分配对应的资源
#一个进程里面默认有一个线程(主线程)
#真正干活的是线程,进程只提供资源
#但多进程也可以完成多任务

import multiprocessing
import time
def show():
    for i in range(10):
        time.sleep(1)
        print("show")


def info():
    for i in range(10):
        time.sleep(1)
        print("info")


if __name__ == '__main__':
    #创建子进程
    first = multiprocessing.Process(target=show)
    second = multiprocessing.Process(target=info)

    #启动子进程(无法控制调度,cpu干的事)
    second.start()
    first.start()
