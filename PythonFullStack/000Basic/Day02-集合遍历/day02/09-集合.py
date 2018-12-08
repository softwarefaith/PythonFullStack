#set集合:以大括号表现形式的数据集合,集合里面不能有重复的数据
#集合可以根据下标获取数据,可以添加和删除
my_set = {1,4,"abc","hello"}
print(my_set,type(my_set))
#删除数据
my_set.remove("hello")
#不能删除没有的数据
# print(my_set)
# my_set.remove("22")

#添加数据(集合是无序的)
my_set.add(5)
print(my_set)
#discard也可以删除数据(此种方式不会报错)
my_set.discard(12221)
#测试可以不可以,根据下标修改数据
# my_set[0]=3
#遍历(获取集合中所有的元素)
for value in my_set:
    print(value)
#定义一个空的集合,只能使用函数的方式来调用
# my_set = {}
my_set = set()
my_set.add(1)
print(my_set)
#集合和列表转换类型(集合可以对容器类去重)
my_list = [1,2,3,4,5,5]
my_set = set(my_list)
print(my_set)
#列表,集合,元组,三者可以相互转换
# tuple()
# list()
# set()

