
"""
线程的一个关键特性是每个线程都是独立运行且状态不可预测。
如果程序中的其 他线程需要通过判断某个线程的状态来确定自己下一

步的操作,这时线程同步问题就 会变得非常棘手。
为了解决这些问题,我们需要使用threading库中的Event对象。 对象包含一个可由

线程设置的信号标志,它允许线程等待某些事件的发生。
在 初始情况下,Event对象中的信号标志被设置为假。如果有线程等待一个

Event对象, 而这个Event对象的标志为假,那么这个线程将会被一直阻塞直至该标志为真。
一个线程如果将一个Event对象的信号标志

设置为真,它将唤醒所有等待这个Event对象的线程。
如果一个线程等待一个已经被设置为真的Event对象,那么它将忽略这个事件, 继续执行。
event.isSet()：返回event的状态值，False或True；
 
event.wait()：如果 event.isSet()==False将阻塞线程，可以加参数，表示等待秒数；
 
event.set()： 设置event的状态值将为True，所有阻塞池的线程激活进入就绪状态， 等待操作系统调度；
 
event.clear()：恢复event的状态值为False。
"""

import  threading
import  time
import logging

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s',)


def worker(event):
    logging.debug("waiting")
    while not event.isSet():
        logging.debug("等待连接")
        event.wait(3)

    logging.debug("ready go")
    time.sleep(1)


def main():
    event = threading.Event()

    t1 = threading.Thread(target=worker,args=(event,))
    t1.start()
    t2 = threading.Thread(target=worker,args=(event,))
    t2.start()

    logging.debug("Checking")
    time.sleep(6)

    event.set()


if __name__ == '__main__':
    main()