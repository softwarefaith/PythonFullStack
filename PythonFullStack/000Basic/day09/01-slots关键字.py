#指明创建对象时候不能再添加其他属性,只能是指定属性

class Student(object):
    #这样操作可以让对象固定属性
    __slots__ = ("name","age")

    def __init__(self,name,age):
        self.name = name
        self.age = age


stu = Student("xx",18)

# stu.sex = "男"
#
# print(stu.sex)
stu.name = "张三"

print(stu.name,stu.age)
