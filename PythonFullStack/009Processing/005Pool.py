"""
在利用Python进行系统管理的时候，特别是同时操作多个文件目录，或者远程控制多台主机，
并行操作可以节约大量的时间。
当被操作对象数目不大时，可以直接利用multiprocessing中的Process动态成生多个进程，
十几个还好，但如果是上百个，上千个目标，手动的去限制进程数量却又太过繁琐，
此时可以发挥进程池的功效。
Pool可以提供指定数量的进程，供用户调用，
当有新的请求提交到pool中时，
如果池还没有满，那么就会创建一个新的进程用来执行该请求；
但如果池中的进程数已经达到规定最大值，那么该请求就会等待，直到池中有进程结束，
才会创建新的进程来它。



"""

import multiprocessing
import time


def myfunc(msg):
    print("begin msg:", msg)
    time.sleep(3)
    print('end msg:', msg)


if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=3)
    for i in range(7):
        msg = 'Hello %s'%(i)
       # pool.apply_async(func=myfunc, args=(msg,))
        pool.apply(func=myfunc,args=(msg,))

    pool.close()
    pool.join()


