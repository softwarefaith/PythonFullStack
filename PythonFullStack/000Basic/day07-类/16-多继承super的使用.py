class A(object):
    def show_a(self):

        print("我是A类")


class B(object):
    def show_b(self):
        print("我是B类")


class C(A,B):
    #查看类的继承顺讯
    def show(self):
        print(self.__class__.mro())

        #如果没有找到,会继续下一个父类来找
        #self代表当前链条,C要查询的是当前链条的下一个类
        super(B,self).show_b()

c = C()
c.show()
