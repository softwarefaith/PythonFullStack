# 内置函数就是直接可以使用的函数，比如： len, max, min, sorted，open
# 内置函数是python自己定义的函数，可以直接使用
# len函数可以统计容器类型(字符串，列表，元组， 字典，集合)的个数
# 统计字符串的个数
result = len("abc")
print(result)
result = len(['a', 'b'])
print(result)
result = len((1, 2))
print(result)

result = len({"name": "李四"})
print(result)

result = len({"李四"})
print(result)

# max函数统计容器类型数据中的最大值
result = max("135")
print(result)

result = max([5, 10, 11])
print(result)

result = min([1, 0])
print(result)

new_list = sorted([8, 6, 7])
print(new_list)

# 函数一个变量 del 函数可以删除变量
# del(new_list)

# print(new_list)

# del 关键字 也可以删除变量
del new_list
print(new_list)
