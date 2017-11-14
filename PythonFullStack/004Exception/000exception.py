# 异常处理

""""""

"""
内置了一套try...except...finally...的错误处理机制
"""

try:
    print('try...')
    r = 10 / int('a')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')

"""
1.Python的错误其实也是class，所有的错误类型都继承自BaseException，
所以在使用except时需要注意的是，
它不但捕获该类型的错误，还把其子类也“一网打尽”

2.使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用
"""

# 抛出错误

"""
如果要抛出错误，首先根据需要，
可以定义一个错误的class，
选择好继承关系，
然后，用raise语句抛出一个错误的实例：

只有在必要的时候才定义我们自己的错误类型。
如果可以选择Python已有的内置的错误类型（比如ValueError，TypeError），
]尽量使用Python内置的错误类型。
"""


def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n


def bar():
    try:
        foo('0')
    except ValueError as e1:
        print('ValueError!')
        raise     # 最恰当的方式是继续往上抛，让顶层调用者去处理

bar()