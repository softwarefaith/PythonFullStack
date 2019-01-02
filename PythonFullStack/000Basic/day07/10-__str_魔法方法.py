#__str_:当使用print打印对象的时候回自动调用

class Person(object):
    def __init__(self,name,age):

        self.name = name
        self.age = age
    def __str__(self):

        #返回一个字符串信息
        return "我叫:%s 年龄:%d" %(self.name,self.age)

#创建对象
person = Person("张三",18)
#打印对象的属性值
print(person.name,person.age)
print(person)