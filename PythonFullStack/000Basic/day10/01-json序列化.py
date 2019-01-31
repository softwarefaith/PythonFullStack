import json
#微信:即时通信(xml)
#只支持部分数据类型:(语言障碍,CC++java)
#1.列表,字典,int ,自定义类型不可以,需要额外指定

my_list = [{"name":"张三","age":"20"}]

file = open("mylist.txt","w",encoding="utf-8")
#序列化
json.dump(my_list,file)
file.close()

file = open("mylist.txt","r",encoding="utf-8")
#反序列化
my_list = json.load(file)
print(my_list)

#自定义类型
class Student(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

file = open("stu.txt","w",encoding="utf-8")
#序列化对象
stu = Student("zhangsan",19)
#序列化对象,本质上就是把对象的属性保存
#序列化对象的属性
json.dump(stu.__dict__,file)



