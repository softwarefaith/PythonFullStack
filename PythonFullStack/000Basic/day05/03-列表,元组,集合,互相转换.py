my_list = [1,4,5,4]

my_tuple = (5,7)

my_set = {4,9}

#把列表转换成集合(集合不允许有重复的数据,转换会去重)
result = set(my_list)
print(result)
#元组转换成集合
result = set(my_tuple)
print(result)
#把列表转成元组
result = tuple(my_list)
print(result)

result = tuple(my_set)
print(result)

#将集合和元组转成列表
result = list(my_set)

print(result,type(result))

result = list(my_tuple)
print(result,type(result))

#
# list() tuple() set()