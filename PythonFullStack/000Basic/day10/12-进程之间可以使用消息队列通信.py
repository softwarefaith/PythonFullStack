import multiprocessing
import time

def add_data(queue):
    for i in range(3):
        print(i)
        queue.put(i)
        time.sleep(0.3)

def read_data(queue):


    while True:
        # 判断队列是否为空
        if queue.empty():
            break
        value =queue.get()
        print(value)

if __name__ == '__main__':
    #默认队列可以放入多个任意数据
    queue = multiprocessing.Queue(3)

    add_proccess = multiprocessing.Process(target=add_data,args=(queue,))
    read_proccess = multiprocessing.Process(target=read_data, args=(queue,))

    #启进程执行任务
    add_proccess.start()
    #进程等待一下,,加载完毕数据之后读取
    read_proccess.start()

#总结:多任务使用线程和进程
#从资源的角度来说,线程更加节省资源
#进程饿销毁的资源比较多

#从代码稳定性来说:多进程要比多线程稳定性要强
#因为一个进程挂掉,不会影响其他应用程序