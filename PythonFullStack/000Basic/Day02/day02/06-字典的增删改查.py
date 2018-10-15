#定义一个空的字典
my_dict = {}
print(dict,type(my_dict))

#给字典添加键值对
my_dict["name"] = "张三"
#如果没有key,会增加一条键值对,如果有,更新key对应的value
my_dict["name"] = "李四"
#key是唯一的,
print(my_dict)
my_dict["age"] = 18
my_dict["sex"] = "男"
my_dict["address"] = "北京"
print(my_dict)
#修改键值对
my_dict["address"] = "上海"
print(my_dict)
#删除(key和value同时存在)
del my_dict["age"]
print(my_dict)
#字典是无序的,
#定义的数据的顺序和输出的顺序不一样

#随机删除键值对
my_dict = {"name":"张三","sex":"女","adddress":"杭州",1:4}
#将键值对都返回了(包装成元组)
# value = my_dict.popitem()
# print(my_dict)
# print(value)
#指定删除键值对
#返回删除的value
value = my_dict.pop("sex")
print(my_dict)
print(value)
#获取字典里面所有的key
result = my_dict.keys()
print(result)
#获取所有的value
result = my_dict.values()
print(result)
#判断key 是否存在字典当中
result = "age" in my_dict
print(result)
