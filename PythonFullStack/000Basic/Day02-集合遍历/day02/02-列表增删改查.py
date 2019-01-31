# #定义一个列表
# my_list = [1,1.2,"abc",True]
#
# result = my_list[-1]
#
# #列表的增删改查
# my_list = []
# print(my_list)
#
# #给列表增加指定数据
# my_list.append(1)
# print(my_list)
# my_list.append("大家好")
# print(my_list)
# #插入新指定数据
# my_list.insert(1,"abc")
# print(my_list)
# #列表里面插入列表
my_list1 = ["西瓜","芒果","草莓"]
# my_list.append(my_list1)
# print(my_list)
# result = my_list[-1]
# print(result)
#将列表元素取出来,然后在拼接到原有的列表里面
#extend函数.没有返回值
my_list=[1,2,3]
my_list.extend(my_list1)
print(my_list)
#####################################################
#修改数据
my_list= [1,"abc","大家好","西瓜","芒果","草莓"]

my_list[0] = "葡萄"
print(my_list)
#删除数据
#remove 删除指定数据
my_list.remove("abc")
print(my_list)
#根据下标删除
del my_list[0]
print(my_list)
#根据下标删除数据,下标要合法
my_list= [1,"abc","大家好","西瓜","芒果","草莓"]
# del my_list[5]
# print(my_list)
#想把删除的数据,返回给我
# result =del my_list[0]
# print(result)
# result = my_list.pop(0)
# print(result)
#使用pop删除方式如果不传下标,默认删除的是最后一个元素
result = my_list.pop()
print(result)

#判断指定数据是否在列表当中
my_list= [1,"abc","大家好","西瓜","芒果","草莓"]

result = "西瓜" in my_list
print(result)

result="西瓜" not in my_list
print(result)

#根据数据在列表中插曲对应下标
#如果没有找到数据会崩溃
result = my_list.index("草莓")
print(result)

#根据指定数据获取数据在列表中的个数
my_list=["西瓜","草莓",1,1,1]
result = my_list.count(1)
print(result)
