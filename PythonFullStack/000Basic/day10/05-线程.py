#线程:执行代码的分支,默认只有一个线程
#导入线程的模块
#python本质上没有线程(假象)
import time
import threading
def AA(count):
    for i in range(count):
        print("aa")
        time.sleep(0.2)


def BB(count):
    for i in range(count):
        print("bb")
        time.sleep(0.2)


if __name__ == '__main__':
    #创建了一个子线程执行对应的代码
    #target:表示目标函数
    #args:表示以元组的方式给函数传参
    #kwargs:表示已字典方式给函数传参
    #创建了一个子线程
    sub_thred =threading.Thread(target=AA,args=(10,))
    threed_thred = threading.Thread(target=BB,kwargs={"count":3})
    #执行子线程(启动线程),只有启动才会让线程执行对应函数的代码
    sub_thred.start()
    threed_thred.start()
#在主线程中
# BB(10)
#线程是无序的,有cpu调度决定