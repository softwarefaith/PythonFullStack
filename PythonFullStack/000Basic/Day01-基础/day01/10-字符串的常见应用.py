#定义字符串：使用引号：单引号，双引号，三引号‘’“””“” “”“
my_str = "hello"
#根据指定数据查找对应的下标（索引）
#下标是从0开始
# str = """hahah"""
print(str)
result = my_str.index("h")
print(result)
#根据指定数据查找对应的下标（索引）
#find和index有区别，find如果没有找到数据返回的是-1，index如果没有找到数据，直接会崩溃
result = my_str.find("z")
print(result)
#统计字符串的长度
result = len(my_str)
print(result)
#统计某个字符出现的次数
my_str = "hello"
result = my_str.count("l")
print(result)
#替换指定数据
result = my_str.replace("l","x")
print(result)
my_str = "苹果,橘子,鸭梨"
print(my_str)
#分割数据(将分割的数据装入列表里面，对应的分割出来的字符就是列表中的元素)
#所有的代码部分都需要用英文，包括标点符号
result = my_str.split(",")
print(result)
#判断是否以指定数据开头
my_url = "http://www.baidu.com"
#返回结果是bool值
result = my_url.startswith("http")
print(result)
#判断是否以指定数据结尾
result = my_url.endswith("xxx")
print(result)

#需求：把字符串以指定字符分割成三部分
my_str = "aaabbccc"
result = my_str.partition("bb")
print(result)
#join:根据指定字符串拼接数据(拼接不是分割)
flag_str = "-"
my_str = "abc"
result = flag_str.join(my_str)
print(result)
mylist = ["1","2","3"]
result = flag_str.join(mylist)
print(result)

#去除空格(只能去除左右两边的空格)
my_str = " hello "
print(my_str)
result = my_str.strip()
print(result)
#去除左边空格
# result = my_str.lstrip()
# print(result)
#去除右边的空格
result = my_str.rstrip()
print(result)
#去除指定的数据
my_str = "ahelloa"
#如果不传参数，默认是去除空格，
result = my_str.strip("a")
print(result)
my_str = "a b"
print(my_str)

result = my_str.strip()
print(result)


