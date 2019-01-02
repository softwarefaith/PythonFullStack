#魔法方法:当前需要完成某个功能操作的时候会自动调用的的某个方法
#比如:__init___
#魔法方法表现形式:__开头,然后__结束的方法就是魔法方法
#init,当前对象初始化的时候会调用此方法
class Teacher(object):

    #init方法里面添加参数
    def __init__(self,name,age):
        #self:表示当前对象
        self.name = name
        self.age = age
    def show(self):
        #slef:当前对象,哪个对象调用此方法,self就是谁(对象)
       print(self.name,self.age)

t1 = Teacher(name="李四",age=15)
t1.show()

# t2 = Teacher("张三",18)
# t2.show()
