# 元类
""""""

# =====type
"""
type()函数可以查看一个类型或变量的类型

type(object) => <class 'type'>

class的定义是运行时动态创建的，
而创建class的方法就是使用type()函数。

"""

# 1.先定义函数


def fn(self, name='word'):
    print('Hello,%s' % name)

# 2.创建Hello class


Hello = type('Hello', (object,), dict(hello=fn))

h = Hello()

print('----', h.hello())


"""
要创建一个class对象，type()函数依次传入3个参数：

1.class的名称；
2.继承的父类集合，注意Python支持多重继承，
如果只有一个父类，别忘了tuple的单元素写法；
3.class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上

要在静态语言运行期创建类，必须构造源代码字符串再调用编译器，
或者借助一些工具生成字节码实现，本质上都是动态编译，会非常复杂
"""

# metaclass

"""
当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。

先定义metaclass，就可以创建类，最后创建实例。

metaclass允许你创建类或者修改类。
换句话说，你可以把类看成是metaclass创建出来的“实例

metaclass是Python中非常具有魔术性的对象，它可以改变类创建时的行为

"""

# 1.  metaclass是类的模板，所以必须从`type`类型派生：


class ListMetaclass(type):

    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

# 2.创建类


class MyList(list, metaclass=ListMetaclass):
    pass

"""
当我们传入关键字参数metaclass时，魔术就生效了，
它指示Python解释器在创建MyList时，
要通过ListMetaclass.__new__()来创建，在此，我们可以修改类的定义

__new__()方法接收到的参数依次是：

当前准备创建的类的对象；

类的名字；

类继承的父类集合；

类的方法集合。
"""


# ORM 框架