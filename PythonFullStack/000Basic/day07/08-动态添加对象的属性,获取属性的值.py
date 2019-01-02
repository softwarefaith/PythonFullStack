#类名一般情况大写(约定俗成)
#class + 类名
class Teacher(object):

    def show(self):
        print("今天天气不错")

#创建对象
teacher = Teacher()

#动态的添加属性
teacher.name = "李四"
teacher.age = 18

#获取数据对应的属性

print(teacher.name,teacher.age)

#修改属性
teacher.name = "王五"

print(teacher.name,teacher.age)
teacher.show()