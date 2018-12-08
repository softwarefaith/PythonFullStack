#拆包通俗理解:把容器类型(字符串,列表,元组,字典,结合)
#每一个数据使用不同的变量保存一下
#字符串
my_str = "abc"
a,b,c = my_str
print(a,b,c)
#列表
my_list = [1,5]
num1,num2 = my_list
print(num1,num2)
#元组
my_tuple = (1,5)
num1,num2 = my_tuple
print(num1,num2)
#拆字典(默认拆取的是key)
my_dict = {"name":"胡亮","age":"20"}.values()
key1,key2 = my_dict
print(key1,key2)
#集合
my_set = {3,5}
num1,num2 = my_set
print(num1,num2)
