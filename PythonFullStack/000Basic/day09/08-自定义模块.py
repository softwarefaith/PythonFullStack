#自定义模块:程序员自己创建的模块
#自定义模块命名规则:和变量名命名规则像
#1.不能以数字开头,可以_字母数字
#导入模块
import fist_moudle
import second_moudle

#可以使用模块里面的代码
# print(fist_moudle.g_num)
# fist_moudle.show()
# stu = fist_moudle.Student("李四",18)
# stu.show()
#打印当前模块的主模块
print(__name__)
result = second_moudle.sum_num(3,2)
print(result)
