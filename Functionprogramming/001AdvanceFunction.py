# 把函数作为参数传入，这样的函数称为高阶函数
# 函数式编程就是指这种高度抽象的编程范式。


# map 函数

"""
map()函数接收两个参数，一个是函数，一个是Iterable，
map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。

"""


def f(x):
    return x * x

r = map(f, [1, 2, 3, 4])

print('map:', list(r))


# reduce

"""
把一个函数作用在一个序列[x1, x2, x3, ...]上，
这个函数必须接收两个参数，
reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

"""


from functools import reduce


def add(x, y):
    return x + y

result = reduce(add, [1, 2, 3, 4])

print('reduce:', result)


# filter

"""
filter()也接收一个函数和一个序列。
和map()不同的是，filter()把传入的函数依次作用于每个元素，
然后根据返回值是True还是False决定保留还是丢弃该元素

关键在于正确实现一个“筛选”函数

注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。


"""


# sorted()

"""

"""
