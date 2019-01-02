#为了兼容不同python版本
#建议大家使用新式类的方式去创建
class Teacher(object):
    #类属性
    country = "中国"

    #方法
    def show(self):
        print("ahahahh")


print(Teacher.__bases__)

t1 = Teacher()
t1.show()
#类可以创建不同的对象
#创建第二个对象
t2 = Teacher()
t2.show()