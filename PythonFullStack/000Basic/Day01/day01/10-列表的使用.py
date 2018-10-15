#以中括号形式的数据集合
#列表可以存储任意数据类型(列表在其他语言里面叫数组)，只能存取同种类型的元素
my_list = [1,1.22,"abc",True]
print(my_list,type(my_list))
#字符串本身也是一个容器，但是他是存取字符的容器
#列表可以存任意类型（可以根据下标取元素）
#下标（索引）是从0开始的
value = my_list[0]
print(value)
#下标：下标本质上是一个编号，可以根据下标找到对应的数据，在python里面有正数下标和负数下标
#正数下标：从0开始，0表示第一个元素：负数下标：从-1开始，-1表示倒数第一个元素
#列表越界（数组越界）会崩库
value = my_list[-1]
print(value)