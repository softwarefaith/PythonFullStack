
"""
===迭代

1.Python的for循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象上。
原则:只要是可迭代对象，无论有无下标，都可以迭代

默认情况下，dict迭代的是key。
如果要迭代value，可以用for value in d.values()，
如果要同时迭代key和value，可以用for k, v in d.items()。

由于字符串也是可迭代对象，因此，也可以作用于for循环：

如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：

Python内置的enumerate函数可以把一个list变成索引-元素对，
这样就可以在for循环中同时迭代索引和元素本身：

"""

from collections import Iterable
isinstance('abc', Iterable)

for i, v in enumerate(['a', 'b', 'c']):
    pass

