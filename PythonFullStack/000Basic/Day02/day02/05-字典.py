#字典:以大括号表现形式的键值对数据组合,{"name":"张三","age":18}
#提示key一般是字符串形式(99%)key必须是
#不可变类型:10 字符串 元组 可变类型:列表,变量
my_dict = {"name":"张三","age":18}

print(my_dict,type(my_dict))

#通过key来取值value
#字典是无序
value = my_dict["name"]
print(value)
#空的字典
#如果没有此键值对,利用keyquvalue会崩溃
# value = my_dict["sex"]
#设置默认值
#利用key取value可以设置默认值,如果没有此键值对,利用get这种方式
#会默认增加一个键值对,如果字典有此键值对,取出是原本字典的数据
#利用get这种方式,如果没有设置默认值,直接取,不会崩溃,返回值为NONE

result = my_dict.get("sex")
print(result)



