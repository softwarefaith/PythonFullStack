#定义一个装饰器函数
def decorator(func):
    def inner(num1,num2):
        print("计算结果如下")
        # func函数(函数返回一下)
        #return3
        return func(num1,num2)

    return inner
#故意搞得复杂一点


#定义一个带有参数的函数(修饰它)
@decorator # -> sum = decorator(sum)
def sum(num1,num2):
    #3
    result = num1 + num2
    return result
#result 承接了3
result = sum(1,2)
print(result)