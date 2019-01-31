class Person(object):
    #私有类属性
    __type = "黄种人"
    def __init__(self):
        #实例属性:
        self.name = "小红"
    #定义一个对象方法:
    def show(self):
        print("我是对象方法")
    #定义类方法(用关键字@classmethod就是类方法)
    #cls(当前类)
    @classmethod
    def show_info(cls):
        print(cls)
        print("我是类方法")
    #定义一个静态方法,提示:静态方法和当前对象和当前类没有任何关系
    #用关键字@staticmethod修饰的就是静态方法
    @staticmethod
    def show_msg():
        print("我是静态方法")
    #类方法应用场景(可以修改类属性)
    @classmethod
    def set_type(cls,type):
        #修改类属性了
        cls.__type = type
        #打印类属性
        print(cls.__type)
    #获取类属性
    @classmethod
    def get_type(cls):
        return  cls.__type

#创建对象,利用对象,调用类方法
p = Person()
p.show_info()
#调用类方法
Person.show_info()
#使用类名调用,实例方法(需要传入对象)
Person.show(p)
#(使用类名)调用静态方法
Person.show_msg()
#使用对象调用静态方法
p.show_msg()


#------扩展--------
#使用对象调用类方法修改类属性值
p.set_type("小蓝")

result = p.get_type()
print(result)