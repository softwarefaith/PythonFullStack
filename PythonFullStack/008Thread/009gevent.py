"""

自动切换

gevent是第三方库，通过greenlet实现协程

当一个greenlet遇到IO操作时，
比如访问网络，就自动切换到其他的greenlet，
等到IO操作完成，再在适当的时候切换回来继续执行。
由于IO操作非常耗时，经常使程序处于等待状态，
有了gevent为我们自动切换协程，就保证总有greenlet在运行，而不是等待IO。

由于切换是在IO操作时自动完成，
所以gevent需要修改Python自带的一些标准库，
这一过程在启动时通过monkey patch完成：

from gevent import monkey

"""

import gevent
import time


def foo():
    print("running in foo")
    gevent.sleep(2)
    print("switch to foo again")


def bar():
    print("switch to bar")
    gevent.sleep(5)
    print("switch to bar again")


start = time.time()

gevent.joinall(
    [gevent.spawn(foo),
     gevent.spawn(bar)]
)
