

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

# 属性检查
"""
Python内置的@property装饰器
负责把一个方法变成属性调用的：

@property广泛应用在类的定义中，可以让调用者写出简短的代码，
同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。
"""


class Person2(object):

    def __init__(self, birth):
        self.__birth = birth

# birth 可读可写
    @property
    def birth(self):
        return self.__birth

    @birth.setter
    def birth(self, value):
        self.__birth = value

    @property
    def age(self):     # age 只读属性
        return 50;


