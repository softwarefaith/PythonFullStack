class Animal(object):
    #对象方法(想要调用他,必须有对象)
    def run(self):
        print("动物跑起来了")

class Dog(Animal):

    def run(self):
        #调用父类的方法
        #会死循环
        # self.run()
        #使用类名调用父类的方法
        # Animal.run(self)
        # print("小狗跑起来了")
        #可以使用super关键字来调用父类的方法
        # Dog表示根据指定类,找类继承链中的获取下一个类
        #self:指定类的继承链
        #mro(Animal)
        super(Dog,self).run()
        #打印类的继承链
        print(self.__class__.mro())


    def wang(self):
        print("汪")

dog = Dog()
#run 需要调用父类的方法
dog.run()
dog.wang()