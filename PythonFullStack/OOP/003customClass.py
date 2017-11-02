# 定制类
""""""

"""
利用特殊用途的函数，可以帮助我们定制类

"""


# __str__
# __repr__

"""
__str__()返回用户看到的字符串，
而__repr__()返回程序开发者看到的字符串，
也就是说，__repr__()是为调试服务的。

通常__str__()和__repr__()代码都是一样的，所以，有个偷懒的写法

__repr__ = __str__
"""

# __iter__
"""
如果一个类想被用于for ... in循环，类似list或tuple那样，
就必须实现一个__iter__()方法，该方法返回一个迭代对象，
然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，
直到遇到StopIteration错误时退出循环。
"""


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值

# __getitem__

"""
把它当成list来使用还是不行

与之对应的是__setitem__()方法，
把对象视作list或dict来对集合赋值。
最后，还有一个__delitem__()方法，用于删除某个元素。
"""


class Fib2(object):
    def __getitem__(self, n):
        if isinstance(n, int):  # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):  # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

f = Fib()

f[0]
f[1:5]

# __getattr__

"""
正常情况下，当我们调用类的方法或属性时，
如果不存在，就会报错

写一个__getattr__()方法，动态返回一个属性

当调用不存在的属性时，
比如score，Python解释器会试图调用__getattr__(self, 'score')
来尝试获得属性，这样，我们就有机会返回score的值

返回函数也是完全可以的：

"""

# __call__

"""
一个对象实例可以有自己的属性和方法，
当我们调用实例方法时，我们用instance.method()来调用。
能不能直接在实例本身上调用呢？

任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。

_call__()还可以定义参数

使实例能够像函数一样被调用，同时不影响实例本身的生命周期
同时不影响实例本身的生命周期（__call()__不影响一个实例的构造和析构）。
但是__call()__可以用来改变实例的内部成员的值
"""

"""
对实例进行直接调用就好比对一个函数进行调用一样，
所以你完全可以把对象看成函数，把函数看成对象，
因为这两者之间本来就没啥根本的区别。

如果你把对象看成函数，那么函数本身其实也可以在运行期动态创建出来，
因为类的实例都是运行期创建出来的，这么一来，我们就模糊了对象和函数的界限。

么判断一个变量是对象还是函数呢？
其实，更多的时候，我们需要判断一个对象是否能被调用，
能被调用的对象就是一个Callable对象

通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。
"""
