#切片:根据下标的范围获取一部分数据:字符串,列表可以使用切片
#正数下标的切片
my_str = "hello"
result = my_str[0]
print(result)
#[起始下标,结束下标,步长](下标从0开始)
#切片结束下标不取
result = my_str[0:4:1]
print(result)
#前三个数据(默认步长为0)
result = my_str[0:3]
print(result)
#前两个可以省略
result = my_str[::3]
print(result)
#快速获取整个字符串
result = my_str[:]
print(result)
#使用负数下标切片的方式获取数据
my_str = "hello"
#获取最后三个元素,默认取到最后的数据
result = my_str[-3:]
print(result)
#步长是负数(步长不能为0)
result = my_str[-2:-5]
print(result,"--------")