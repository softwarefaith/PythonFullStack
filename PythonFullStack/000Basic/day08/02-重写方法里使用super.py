class Person(object):
    def show(self):
        print("我是人类")

class Plane(object):
    def show(self):
        print("我是飞机")
    def fly(self):
        print("飞机可以飞")


class Student(Person,Plane):

    def show(self):
        #方法重写调用父类的方法
        #根据指定类,找类继承链中的下一个类
        super(Person,self).show()



s1 = Student()
s1.show()