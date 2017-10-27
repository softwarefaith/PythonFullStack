# 装饰器

"""
1.由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。

2.函数对象有一个__name__属性，可以拿到函数的名字


"""

import functools


def log(func):
    @functools.wraps(func)  # 不加这一句:__name__ 返回wrapper
    def wrapper(*args, **kw):
        print("我把你装饰了")
        return func(*args, **kw)
    return wrapper;


@log
def now():
    print('now')

print('获取函数名字:', now.__name__)

print('调用now:', now())

"""
==以上代码解读:
log()是一个decorator，返回一个函数，
所以，原来的now()函数仍然存在，
只是现在同名的now变量指向了新的函数，
于是调用now()将执行新函数，
即在log()函数中返回的wrapper()函数

wrapper()函数的参数定义是(*args, **kw)，
因此，wrapper()函数可以接受任意参数的调用

函数也是对象，它有__name__等属性，
但你去看经过decorator装饰之后的函数，
'now'变成了'wrapper'：

不需要编写wrapper.__name__ = func.__name__这样的代码，
Python内置的functools.wraps就是干这个事的
"""

"""
在面向对象（OOP）的设计模式中，decorator被称为装饰模式。
OOP的装饰模式需要通过继承和组合来实现，而Python除了能支持OOP的decorator外，直接从语法层次支持decorator。Python的decorator可以用函数实现，也可以用类实现。

decorator可以增强函数的功能，定义起来虽然有点复杂，
但使用起来非常灵活和方便。


"""
