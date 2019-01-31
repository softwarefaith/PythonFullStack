#类的三大特性之一:继承
#封装继承多肽
#继承好处:子类可以复用父类的属性和方法
#object->Person->Student
class Person(object):

    def __init__(self):
        #谁定对象的默认属性值
        self.name = "张三"
        self.age = 18
    #方法:
    def show(self):
        print(self.name,self.age)

#定义一个学生类
#Student就是Person类的子类
class Student(Person):
    pass
xiao_lan = Student()
#子类可以使用父类的方法,还可以使用父类的属性
xiao_lan.show()
print(xiao_lan.name,xiao_lan.age)