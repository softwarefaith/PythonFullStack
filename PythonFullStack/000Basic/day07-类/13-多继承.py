#多继承:相当于继承多个父亲
class A(object):
    def show(self):
        print("我是A类")


class B(object):
    def show(self):
        print("我是B类")

class C(A,B):
    pass
c = C()
#调用父类A的方法
c.show()
#调用父类B的方法
# c.show_info()

#python里面方法调用hi尊村mro
#累的继承顺序,决定方法调用的时候查找的顺序
print(C.mro())