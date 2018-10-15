# 切片: 根据下标的范围获取一部分数据，比如: 列表，字符串可以使用切片

my_str = "hello"

# result = my_str[1]
# print(result)

# 切片的使用格式
# 数据[起始下标:结束下标:步长]
# 提示： 起始下标默认0， 结束下标是不包含， 步长默认是1

# 使用切片的方式获取一部分数据
result = my_str[1:4:1]
print(result)

result = my_str[0:3]
print(result)

result = my_str[:3]
print(result)

my_str = "hello"

result = my_str[2:5]

print(result)

# 使用负数下标切片方式获取数据
# 可以获取倒数后面三个数据，冒号后面不知道表示可以取到最后一个数据
result = my_str[-3:]
print(result)


result = my_str[0:5]

print(result)
# 快速获取整个字符串
result = my_str[:]

print(result)

my_str = "hello"

# 步长是负数表示从后往前取值
result = my_str[-2:-5:-1]
print(result)

# 使用正数下标切片方式获取数据
result = my_str[3:0:-1]
print(result)

# 倒着获取字符串中的每个数据
result = my_str[::-1]
print(result)

result = my_str[::2]
print(result)