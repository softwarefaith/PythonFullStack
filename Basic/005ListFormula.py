
"""
列表生成式
即List Comprehensions
Python内置的非常简单却强大的可以用来创建list的生成式。

L = []
 for x in range(1, 11):
    L.append(x * x)
    
转换为:

[x * x for x in range(1, 11)]

for循环后面还可以加上if判断

[x * x for x in range(1, 11) if x % 2 == 0]

运用列表生成式，可以快速生成list，
可以通过一个list推导出另一个list，而代码却十分简洁。



"""


from collections import Iterable

L = ['Hello', 20, 40, 'Apple', 'I Love U']


def test(t=None):
    if t is None:
        return None
    if not isinstance(t, Iterable):
        return None
    return [s.lower() for s in t if isinstance(s, str)]


print('结果=', test(L))