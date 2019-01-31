#类属性是在方法和类内部定义的属性叫类属性
#实例属性:在init方法里面定义的属性叫做实例属性

class Person(object):
    #类属性
    type = "黄种人"
    def __init__(self):
        #实例属性(对象属性)
        self.name = "张三"
        self.age = 29

#------------类属性的操作-----------
#查看类属性的方法和属性(查看类)
# print(Person.__dict__)
# #使用类来访问类属性
# print(Person.type)
# #修改类属性
# Person.type = "白种人"
# print(Person.type)

#使用类访问对象属性(注意,不可以使用类名来访问对象属性)
# print(Person.name)

#----------对象属性的操作------------
#使用对象访问类属性(注意,可以使用对象来访问类属性)
person = Person()
print(person.type)
#使用对象修改类属性(不可以修改的)
#相当于增加了一个type的实例属性
person.type = "白种人"
#查看类属性的方法
print(person.type)
#查看类属性和类方法的函数
print(Person.__dict__)
#查看实例梳理的方法的函数
print(person.__dict__,"--------")

#总结:类属性由类来完成,对象(实例)属性,由对象来完成(可以访问类属性,但是不可以修改)
