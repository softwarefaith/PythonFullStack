#重写:子类继承父类,父类的方法满足不了子类的需求,可以对父类的方法进行重写

class Person(object):
    def run(self):
        print("跑起来了")


class Student(Person):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    #子类重写父类的方法,因为父类满足不了子类的方法的时候
    #才去重写
    def run(self):
        print("%s跑起来了" % self.name)


stu = Student("张三",18)
#调用方法的时候,先去本类找,如果本类没有去父类找,
#遵循mro的特点,最终去爷爷类(object)去找
#如果都没有找到,会崩溃
stu.run()