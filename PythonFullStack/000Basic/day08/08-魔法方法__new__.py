#new:当前对象创建的时候就会调用:
#init方法:对象创建完毕之后会调用init方法,给对象添加属性及其初始化
#创建对象调用两个方法,先调用new,new调用完毕之后,表示对象创建完成
#然后调用init方法实例化
class Student(object):
    def __new__(cls,*args,**kwargs):

        print("创建了对象")
        print(args,kwargs)
        #返回父类的new方法(调用类父类的方法)
        #new方法必须返回(相当于创建对象)
        return object.__new__(cls)

        #对象没有创建(初始化呢)
    def __init__(self,name,age,sex):

        self.name = name
        self.age = age
        #默认给对象添加属性
        print("初始化")

#模块 (线程)(异常)

stu = Student("张三",10,"男")

