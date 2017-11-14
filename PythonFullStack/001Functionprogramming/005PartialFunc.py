# 偏函数

"""
1.通过设定参数的默认值，可以降低函数调用的难度。
而偏函数也可以做到这一点

2.functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），
返回一个新的函数，调用这个新函数会更简单。

3.符合函数设置默认参数的规则

偏函数是将所要承载的函数作为partial()函数的第一个参数，
原函数的各个参数依次作为partial()函数后续的参数，除非使用关键字参数。

"""

import functools


def add(x, y):
    return x + y

#  固定参数映射设置值
add2 = functools.partial(add, y=10)

print("add2 = ", add2(5))

