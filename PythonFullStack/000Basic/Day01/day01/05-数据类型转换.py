num = 10
mystr = "10"
# result= num + mystr
# print(result)
#将字符串转换成整型
num2 = int(mystr)
num_type = type(num2)
result = num2 + num

#同一数据类型才可以进行计算
pi = 3.99

result = num + pi
#int类型和float类型尽心计算的时候，会将计算结果返回为float类型
result_type= type(result)

print(result_type)
#将浮点型转换成整型(会抹去后缀的所有小数点)
int_pi =int(pi)
print(int_pi)
#整型转换成浮点型
result = float(num)
print(result)

result = float(mystr)
print(result)
#将浮点型转换成字符串类型
mystr = str(result)
print(type(mystr))
#数据类型转换的方法 整型（int（））浮点型（flota（））字符串类型（str（））
#不是数字不要转换
mystr = "haha"
result = int(mystr)
print(result)