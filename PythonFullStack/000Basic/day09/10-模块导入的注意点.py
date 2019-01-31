# from fist_moudle import show
# #这种导入需要保证当前模块不要定义导入的功能代码
# # def show():
# #     print("哈哈")
# show()
import random
import sys

# import fist_moudle#推荐导入方式1
# def show():
#     print("哈哈")
# show()
# fist_moudle.show()
#模块导入的注意点:
#1.自定义模块名不要和系统模块名重复
#2.导入功能代码不要在当前模块自定义否则使用不了导入的功能代码块
# result = random.randint(1,3)
# print(result)
#查看模块搜索的顺序
print(sys.path)