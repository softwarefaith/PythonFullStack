#元组:以小括号形式的数据集合,比如(1,2,"abc")
#可以存储任意数据类型
#注意,元组可以根据下标获取数据,但是不能对元组进行数据修改

my_tuple = (1,4,"abc",True,1.2)
print(my_tuple)

#根据下标取值
value = my_tuple[-1]
print(value)

# #元组不能根据下标删除数据
# del my_tuple[2]
# print(my_tuple)
#修改也是不可以
# my_tuple[0] = 3
# # print(my_tuple)
# #直接根据下标修改数据是不可以的,不论元组里面装的是什么数据类型
# my_tuple = (1,[3,5])
# my_tuple[1] = [2,4]
# print(my_tuple)
#my_list list类型
my_list = my_tuple[1]
my_list = [2,4]
print(my_list)

#创建空的元组
my_tuple = ()
print(my_tuple)
#元组只装一个元素
#注意是个坑:元组如果只有一个元素,那么元组的类型是元素的类型
#如果想元组里面只装一个元素,元组要求是元组类型,那么在元素后面加上逗号
my_tuple = (1,)
print(type(my_tuple))

#判断数据是否存在在元组里面
my_tuple = (5,10,10,10)

result = 5 in my_tuple
print(result)

result = 5 not in my_tuple
print(result)
#元组中元素的下标
index = my_tuple.index(5)
print(index)
#元组中元素的个数
result = my_tuple.count(10)
print(result)

