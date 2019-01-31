#类的定义需要使用class关键字 人有特征和行为(动作)
#类有属性(特征)和方法(行为)

#定义一个老师类(继承父类)
#创建类的方式,是旧式类方式创建
#python3默认继承object
#python2中里面就没有父类

class Teacher():
    #国籍(属性)
    country = "中国"
    #方法
    def show(self):
        print("大家好,我是大家的授课老师")

#通过类来创建对象,类好比是一个图纸,根据图纸创建对象
teacher = Teacher()
#通过对象调用方法
teacher.show()
#通过对象查看方法
print(teacher.country)
#查看Teacher类继承的父类(object)
print(Teacher.__bases__)

