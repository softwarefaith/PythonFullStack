#可变类型:可以在原有数据基础上对数据进行修改(增删改查)
#不可变类型:不能再原有基础上对数据进行修改
#可以直接重新赋值:那么内存地址会发生改变

#可变类型:列表,集合,字典,对数据进行修改之后,内存地址不会改变
#不可变类型:字符串,数字,元组,不能再原有的数据基础上对数据进行修改
my_list = [1,5,6]
print(my_list,id(my_list))
#改变,增加,删除
my_list[0]=2
my_list.append(10)
del my_list[1]
print(my_list,id(my_list))
#字典
my_dict = {"name":"李四","age":19}
print(my_dict,id(my_dict))
my_dict["name"] = "王五"
print(my_dict,id(my_dict))
#集合(列表,[数组])
my_set = {5,10}
print(my_set,id(my_set))
my_set.add("666")
print(my_set,id(my_set))
#不可变类型一些操作------------------------------

my_str = "hello"
print(id(my_str))
#修改元素
# my_str[0] = "10"
# print(my_str)
#重新赋值改变内存地址
my_str = "hhh"
print(id(my_str))
#数字
my_num = 5
print(id(my_num))

my_num = 10
print(id(my_num))

#元组
my_tuple = (4,6)
print(id(my_tuple))
# my_tuple[0]错误的
my_tuple = (1,5)
print(id(my_tuple))

#重新赋值(重新开辟空间)
my_list = [10,20]
print(id(my_list))
my_list = [20,30]
print(id(my_list))

#可变类型:元勋在基础数据修改
#不可变类型:修改数据内存地址会发生变化
#其实本质上修改的是变量存储的内存地址

#重新运行程序:需要重新开辟内存空间(内存地址才会改变)