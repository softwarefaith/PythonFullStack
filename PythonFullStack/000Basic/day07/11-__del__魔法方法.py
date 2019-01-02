#__del__:对象释放的时候回自动调用del方法
#1.程序退出,程序中所使用的对象全部销毁
#2.当前对象内存地址没有变量使用的时候,那么对象会销毁
import time
class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    #当对象引用计数为0的时候回调用此方法
    def __del__(self):
        print("对象被销毁了",self)

#创建对
#引用计数:1
xiao_ming = Person("小明",20)

#小兰持有了小明(xiao_lan用用xiao_ming的内存地址)
#引用计数变成2
xiao_lan = xiao_ming


#删除对象(减去一个引用计数)
#1
del xiao_ming
#0
del xiao_lan

#引用计数:内存地址呗变量使用的次数,当引用计数为0表示对象呗销毁
time.sleep(3)
print("程序退出了")


