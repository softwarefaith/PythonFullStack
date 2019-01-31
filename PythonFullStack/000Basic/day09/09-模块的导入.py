#__________________import 导入模块_______________
# import fist_moudle
# stu = fist_moudle.Student("张三",18)
#
# print(stu.name,stu.age)
# print(fist_moudle.g_num)

#__________________from模块名 import功能代码 导入模块_______________
# from fist_moudle import Student
# # from fist_moudle import show
# # stu = Student("张三",18)
# # def show():
# #     print("我是09-模块的导入")
# #
# # show()
#__________________from模块名 import* 导入模块_______________
#使用__all__限定导入的功能代码
# from fist_moudle import *
# # print(g_num)
# # show()
# # stu = Student("李四",19)

#给imort 模块名设置别名
import fist_moudle as first #as 设置模块的别名
print(first.g_num)

#from 模块名 imort功能代码 设置别名
from fist_moudle import show as show_msg
from fist_moudle import Student as Stu
s1 = Stu("lisi",18)
show_msg()


