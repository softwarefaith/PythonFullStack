#单例:设计模式,常用的设计模式

#在应用中,不管创建多少次对象,都是一个对象


class Person(object):

    #私有属性
    __instance = None
    #创建对象
    def __new__(cls, *args, **kwargs):
        #第一次创建对象
        if cls.__instance == None:
            #创建对象
            print("创建对象")
            #把创建的对象给类属性
            #object.__new__(cls)(调用类父类的方法)
            #相当于创建对象成功(instance是否为None)
            #创建出来的当前对象
            cls.__instance = object.__new__(cls)
        #如果__instance有值,直接返回__instance(第一次创建的对象)
        return cls.__instance
    def __init__(self,name,age):
        print("初始化")

#p1和p2是同一个对象
p1 = Person("zhangsan",10)

p2 = Person("lisi",20)
print(p1,p2)
