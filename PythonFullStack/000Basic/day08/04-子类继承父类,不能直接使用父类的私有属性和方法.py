class Person(object):

    def __init__(self):
        self.__age = 10

    def __show(self):
        print("我是一个私有方法")
    def text(self):
        print("我是一个公有方法")

class Student(Person):
    def show(self):
        #访问父类的私有属性和私有方法
        # print(self.__age)
        # self.__show()
        self.text()


student = Student()
student.show()


#总结:子类继承父类,不能直接使用私有属性和私有方法