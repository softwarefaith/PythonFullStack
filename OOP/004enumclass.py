# 枚举类
"""
当我们需要定义常量时，一个办法是用大写变量通过整数来定义
JAN = 1
好处是简单，缺点是类型是int，并且仍然是变量。

更好的方法是为这样的枚举类型定义一个class类型，然后，每个常量都是class的一个唯一实例
"""

from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# 访问枚举类型
print(Month.Jan)

# 遍历 value属性则是自动赋给成员的int常量，默认从1开始计数。

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

# 精确地控制枚举类型

"""
可以从Enum派生出自定义类

既可以用成员名称引用枚举常量，又可以直接根据value的值获得枚举常量

Enum可以把一组相关常量定义在一个class中，
且class不可变，而且成员可以直接比较。


"""

print('=============')


@unique  # @unique装饰器可以帮助我们检查保证没有重复值。
class Weekday(Enum):
    Sun = 0
    Mon = 1

day1 = Weekday.Mon
print(day1, day1.value)

print(Weekday['Sun'])

print(day1 == Weekday(5))