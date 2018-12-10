# #内置函数:可以直接使用的函数:print(),len,max,min sorted,open
# #内置函数式python自己定义的函数,可以直接使用,不需要自己定义
# #就是讲api(接口)
# #len可以统计容器类型的长度(个数)(字符串,列表,元组,字典,集合)
# #统计字符串的个数
# str = "abc"
# result = len(str)
# print(result)
# #列表
# result = len(["a","b"])
# print(result)
#
# result = len({"a":"b"})
# print(result)
#
# result = len({"李四"})
# print(result)
# #max函数 统计容器类行数据中的最大值
# result = max("13100")
# print(result)
#
# result = max([5,10,100])
# print(result)
#
# #min 统计容器类数据中的最小值
# result = min([10,20,30])
# print(result)

#列表排序(会返回一个新的列表)
new_list = sorted([8,6,7],reverse=True)
# print(new_list)
#del函数 可以删除变量
# del(new_list)
#没有变量了
# print(new_list)
del new_list
print(new_list)
#代表定义一个整型的变量
# int a = 10
# #python中(会自动帮助我们推到数据类型)定义一个整型的变量
# a = 10
