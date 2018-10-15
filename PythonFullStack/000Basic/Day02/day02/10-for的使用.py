#for循环最长使用获取容器类型中的所有元素
#获取容器类型中的每一个元素(遍历)(字符串,列表,元组,字典,集合)
#字符串
my_str = "abc"
for value in my_str:
    print(value)
#列表
my_list = ["苹果","草莓"]
for value in my_list:
    print(value)
#把元素遍历出来,还要下标
#可以是enumerate
my_list = enumerate(["苹果","草莓"])
print(type(my_list))
for value in my_list:
    print(value[0],value[1])
#拆包:index 获取到容器类型中的所有元素
my_list = enumerate(["苹果","草莓"])
#index代表下标,value代表元素值
for index,value in my_list:
    print(index,value)
#元组
#enumerate:遍历数据时,需要取下标enumerate
for value in enumerate((1,5)):
    print(value)
#遍历字典
my_dict = {"name":"张三","age":"18"}
#遍历字典,默认打印key
for key in my_dict:
    print(key)
#遍历value:
for value in {"name":"张三","age":"18"}.values():
    print(value)

#遍历出来字典所有的key,和value
for key,value in {"name":"张三","age":"18"}.items():
    print(key,value)


#集合
my_set = {1,3,5}
for value in my_set:
    print(value)


