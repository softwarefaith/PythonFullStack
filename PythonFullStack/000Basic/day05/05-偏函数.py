import functools

def show(num1,num2,num3=1):
    result = num1 + num2 + num3
    return result

#片函数:通俗理解就是指明函数的参数偏爱某个值,这种函数就叫做偏函数

result = show(1,2)


print(result)
#定义一个偏函数(偏爱3)
def show2(num1,num2,num3 = 3):
    #在函数内部调用函数
    result = show(num1,num2,num3)

    return result

result = show2(1,2)
print(result)

#偏函数有简写的方式
newfuc=functools.partial(show2,num2=2)
result = newfuc(1)
print(result)

#可以对内部函数使用偏函数
result = int("123")
#利用偏函数对系统内部函数设置偏爱值,数据类型转换按照2进制方式转换
new_fuc=functools.partial(int,base=2)
result = new_fuc("11")
print(result)
