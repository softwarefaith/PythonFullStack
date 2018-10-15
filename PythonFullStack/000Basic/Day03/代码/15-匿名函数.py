# 匿名函数： 顾名思义就是函数没有名字，使用lambda关键字定义的函数就是匿名函数
# 匿名函数只适合做一下简单的操作，返回值不需要加上return
# result = (lambda x, y: x + y)(1, 2)
# print(result)
#
# # 一般使用变量保持匿名函数
# func = lambda x, y: x * y
#
# result = func(1, 2)
# print(result)
#
# # 判断是否是偶数
# def is_os(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False
#
# result = is_os(1)
# print(result)

# 匿名函数的应用场景，简化代码, 还可以使用简单的if判断
new_func = lambda num: True if num % 2 == 0 else False

result = new_func(1)
print(result)

# 对字典列表排序的时候还可以使用匿名函数
my_list = [{"name": "zs", "age": 20}, {"name": "ls", "age": 19}]


# item: 表示列中的每一项字典数据
# item["age"]: 根据字典中age对应的value值排序
# 默认是从小到大进行排序
# my_list.sort(key=lambda item: item["age"], reverse=True)
# print(my_list)

# 匿名函数也是函数

def get_value(item):
    return item["age"]

my_list.sort(key=get_value, reverse=True)
print(my_list)