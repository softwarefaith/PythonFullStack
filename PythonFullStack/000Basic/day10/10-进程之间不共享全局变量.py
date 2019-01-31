import multiprocessing
import time

my_list = []

def add_data():
    for i in  range(3):
        # print(i)
        my_list.append(i)
        # time.sleep(0.3)
    print("add_data",my_list)
def read_data():
    # time.sleep(2)
    print("read_data:",my_list)

#手写单例
if __name__ == '__main__':
    #创建两个子进程
    add_proccess = multiprocessing.Process(target=add_data)
    read_proccess = multiprocessing.Process(target=read_data)
    #启动进程执行任务

    add_proccess.start()
    # 进程等待,主进程等待子线程承执行完再让后面的代码执行
    add_proccess.join()
    read_proccess.start()

