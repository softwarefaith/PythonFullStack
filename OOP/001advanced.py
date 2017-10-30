

# 限制属性
""""""
"""
1.当我们定义了一个class，
创建了一个class的实例后，
我们可以给该实例绑定任何属性和方法，
这就是动态语言的灵活性

2.尝试给实例绑定一个方法
给一个实例绑定的方法，对另一个实例是不起作用的

3.为了给所有实例都绑定方法
可以给class绑定方法

4.我们想要限制实例的属性怎么办？
比如，只允许对Person实例添加name和age属性
__slots__ = ('name', 'age')
试图绑定address将得到AttributeError的错误
"""


class Person(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称


def set_age(self, age):
    self.age = age

from  types import MethodType

p = Person()
p.set_age = MethodType(set_age, p)
p.set_age(30)

print("age = ", p.age)