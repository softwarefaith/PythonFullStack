#提示一下:创建py文件的时候,命名规则尽量和变量和函数的命名规则一样
class AA(object):
    def __init__(self,name):
        print("A")
        self.name = name


class B(AA):
    #提示一下:如果子类提供了调用的方法,那么,不会主动调用父类的方法
    def __init__(self,subject):

        #调用父类的init方法(错误)
        # self.__init__("zhangsan")
        #使用类名调用父类的init方法(注意点,用类名调用方法,需要传入对象)
        # AA.__init__(self,"zhangsan")
        # self.subject = subject
        #.类继承链的方式(super方式)
        # super(B,self).__init__("王五")
        #简写方式->B,self
        super().__init__("王五")




b = B("python")
