#在属性名和方法名前面加上__,那么定义的属性和方法就是私有属性和私有方法

class Person(object):
    #反爬虫(显示网页),age(抓取不完全的数据)
    #增加私有方法
    def __init__(self,name,age):

        #共有属性
        self.name = name

        #私有属性
        #注意点:外部访问不了的属性,就叫私有属性
        #私有属性指定在init方法里面添加
        self.__age = age
        #私有方法和属性,可以在类的内部使用(外部访问不了)
        print(self.__age)

        #公有方法
    def show(self):
        print("共有方法")
        #私有方法
    def __money(self):
        print("__100万")
    # __money()



person = Person("zhangsan",10)

# print(person.__age)
#查看对象中的属性信息(查看私有方法)
# print(person.__dict__)
# # #在这里不是修改私有属性的值,而是给对象添加了一个__age的属性
# # person.__age = 10
# #


person.show()
# person.__money()
#打印所有的属性(私有属性,共有属性)
print(person.__dict__)
#打印所有的方法(注意,是类名调用__dict__)
print(Person.__dict__,"---------")

#在python中,是没有真正的私有方法和私有函数的(伪装的)
#约定俗成(以__开头的就是私有的)
#非常规操作
#设置私有属性的值
person._Person__age = 20
#获取私有属性的值
print(person._Person__age)


#调用私有方法
person._Person__money()


