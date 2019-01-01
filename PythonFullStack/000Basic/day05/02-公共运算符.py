my_str1 = "hello"
my_str2 = "world"

result =my_str1+my_str2

print(result)
#+运算符可以完成列表,元组,字符串的拼接

my_list1 = [1,3]
my_list2 = [2,4]
result = my_list1 + my_list2
print(result)

my_tuple1 = (1,5)
my_tuple2 = (2,4)
result = my_tuple1 + my_tuple2
print(result)

result = "-" *30
print(result)
result = "ab" *2
print(result)
#*运算符:可以完成,列表,元组字符串复制
my_list1 = [1,2]
result = my_list1 *2
print(result)

my_tuple1 = (4,6) *3
print(my_tuple1)
#集合不接受* 和 + 运算符
my_set = {1,2}
my_set_1 = {3,4}
result = my_set + my_set_1
print(result)