"""
方便手动切换

greenlet机制的主要思想是：生成器函数或者协程函数中的yield语句挂起函数的执行，
直到稍后使用next()或send()操作进行恢复为止。
可以使用一个调度器循环在一组生成器函数之间协作多个任务。
greenlet是python中实现我们所谓的"Coroutine(协程)"的一个基础库.

"""

from greenlet import greenlet


def test1():
    print(12)
    gr2.switch()
    print(34)
    gr2.switch()


def test2():
    print(56)
    gr1.switch()
    print(78)


gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()