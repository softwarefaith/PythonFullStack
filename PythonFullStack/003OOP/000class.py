# 类与 实例
"""
"""

"""
面向对象最重要的概念就是类（Class）和实例（Instance）
必须牢记类是抽象的模板

类是创建实例的模板，而实例则是一个一个具体的对象，
各个实例拥有的数据都互相独立，互不影响；

方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；

和静态语言不同，Python允许对实例变量绑定任何数据

"""

"""
类的定义:
 class  定义类关键字
 person 类名,首字母大写
 (): 继承关系
 
类函数:

 和普通的函数相比，在类中定义的函数只有一点不同，
 第一个参数永远是实例变量self，并且，调用时，不用传递该参数
 
 除此之外，类的方法和普通函数没有什么区别，
 所以，你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数
 
 调用普通实例方法 通过 点语法
"""


class Person(object):

    def __init__(self, name, age):    # 实例化的时候self不需要传，Python解释器自己会把实例变量传进去：
        self.__name = name   # name  成为了私有属性
        self.age = age

    def log(self):
        print('name:', self.__name, 'age:', self.age)

# 实例1
test0 = Person('Allan', 29)   # test 是Person 类的一个实例
test0.name1 = 'name1'
print(test0.name1)

test1 = Person('Allan', 29)
# test0 实例动态绑定了name1属性
# 只属于这个实例,不属于新创建的实例对象test1
# print(test1.name1)

# 实例2

test3 = Person('Allan', 29)
test3.log()

# 因为Python解释器对外把__name变量改成了_Person__name(编译器决定)
print('name:', test3._Person__name, 'age:', test3.age)

# 此时  __name 和 person 类的 __name 不是一个属性
# 这里是实例动态绑定属性
# person 类的 __name  早已变味  _Person__name
test3.__name = "嗯哼"
print('name:', test3.__name , 'age:', test3.age)


# 类的访问

"""
在Class内部，可以有属性和方法，
而外部代码可以通过直接调用实例变量的方法来操作数据

==属性访问权限

如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，
在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），
只有内部可以访问，外部不能访问

确保了外部代码不能随意修改对象内部的状态，
这样通过访问限制的保护，代码更加健壮

如果外部想要访问或者修改私有属性:
可以添加  get set 方法
这也敢做的好处:在方法中，可以对参数做检查，避免传入无效的参数

Note:
在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，
是特殊变量，特殊变量是可以直接访问的，不是private变量

双下划线开头的实例变量是不是一定不能从外部访问呢？
其实也不是。
不能直接访问__name是因为Python解释器对外把__name变量改成了_Person__name
但是强烈建议你不要这么干，因为不同版本的Python解释器可能会把__name改成不同的变量名。

"""

# 继承与Person类
"""
1.子类获得了父类的全部功能
2.多态

3.isinstance()   验证是不是某一个类的实例
在继承关系中，如果一个实例的数据类型是某个子类，
那它的数据类型也可以被看做是父类。但是，反过来就不行

4. 鸭子 理论
Python的“file-like object“就是一种鸭子类型。
对真正的文件对象，它有一个read()方法，返回其内容。
但是，许多对象，只要有read()方法，都被视为“file-like object“。
许多函数接收的参数就是“file-like object“，
你不一定要传入真正的文件对象，完全可以传入任何实现了read()方法的对象。

"""


class Student(Person):
    def log(self):
        print('我是学生')
        super(Student, self).log()   # 调用父类方式

    def log_a(self):
        print('我是学生1')
        Person.log(self)

student = Student('Allan0', 50)
student.log()
student.log_a()

"""
当存在继承关系的时候，有时候需要在子类中调用父类的方法，
方法一:
此时最简单的方法是把对象调用转换成类调用，
需要注意的是这时self参数需要显式传递
比如 log_a  方法

缺点:
如果修改了父类名称，那么在子类中会涉及多处修改，
另外，Python是允许多继承的语言，
如上所示的方法在多继承时就需要重复写多次，显得累赘。
为了解决这些问题，Python引入了super()机制

方法二:
比如: log 函数中
super(Student, self).log() 
==> 
super(child_class, child_object).parent_attribute(arg)
父类方法的参数只有self时，参数args不用写



"""

# 多继承

"""

1. 在 init 初始化时,使用super()机制
    如果使用对象调用转换成类,父类可能会只执行多次
    
2.在super机制里可以保证公共父类仅被执行一次，
至于执行的顺序，是按照mro进行的（class.__mro__）-
方法解析顺序

3. Python中，类自身或者其父类继承了object那么这个类就是个新式类，
若没有继承object，则是经典类。
因为Python中存在多重继承，
在新式类中，要查找或调用一个方法或属性时，使用的是广度优先搜索算法；
而在经典类中则使用深度优先搜索算法。

"""

# 类型判断

"""
如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量
"""
print('类型判断', type(student)) # <class '__main__.Student'>

import types


def fn():
    pass

print('我的类型是函数吗?:', type(fn) ==types.FunctionType)

"""
对于class的继承关系来说，使用type()就很不方便。
我们要判断class的类型，可以使用isinstance()函数
"""

# 能用type()判断的基本类型也可以用isinstance()判断
type('abs') == str
isinstance('asd', str)

# 判断一个变量是否是某些类型中的一种
isinstance([1, 2, 3], (list, tuple))

# 获得一个对象的所有属性和方法
# 类似__xxx__的属性和方法在Python中都是有特殊用途的
print('对象的所有属性和方法:', dir('ABC'))

# 配合getattr()、setattr()以及hasattr()
# 我们可以直接操作一个对象的状态: 属性

print('============')

class Student2(Person):
    name = '类属性'


s = Student2('Allan00', 100)

# 打印name属性，因为实例并没有name属性，所以会打印类属性
print('类属性', s.name)

print(Student2.name) # 打印类的name属性

s.name = 'Allan 8888'
# # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
print(s.name)

print(Student2.name)  # 但是类属性并未消失，用Student.name仍然可以访问


del s.name
# 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
print(s.name)


"""
在编写程序的时候，千万不要把实例属性和类属性使用相同的名字，
因为相同名称的实例属性将屏蔽掉类属性，
但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性

"""

# MixIn

"""
在设计类的继承关系时，通常，主线都是单一继承下来的，
例如，Ostrich继承自Bird。
但是，如果需要“混入”额外的功能，通过多重继承就可以实现，
比如，让Ostrich除了继承自Bird外，再同时继承Runnable。
这种设计通常称之为MixIn。

MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，
我们优先考虑通过多重继承来组合多个MixIn的功能，
而不是设计多层次的复杂的继承关系。

不需要复杂而庞大的继承链，只要选择组合不同的类的功能，
就可以快速构造出所需的子类

[个人感觉像 多个协议  遵守 接口隔离原则, Python 中用类来模拟]

"""