#指定__all__表示from模块名 imopt *只能使用指定功能代码,而不是所有功能代码
# __all__ = ["g_num","show"]
#定义一个全局变量
g_num = 10
#定义函数
def show():
    print("我是函数")

#定义类
class Student(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name,self.age)
#
