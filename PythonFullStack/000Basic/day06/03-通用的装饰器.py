#通用的装饰器
#装饰器可以修饰任何函数(自定义)
def decorator(func):
    def inner(*args,**kwargs):
        print("计算结果如下")
        # func函数(函数返回一下)
        # return3
        return func(*args, *kwargs)

    return inner


# 故意搞得复杂一点


# 定义一个带有参数的函数(修饰它)
@decorator  # -> sum = decorator(sum)
def sum(num1, num2):
    # 3
    result = num1 + num2
    return result
@decorator
def sum1(num1,num2,num3):
    result = num1 + num2 + num3
    return result

# result 承接了3
# result = sum(1, 2)
# print(result)
result = sum1(1,2,3)
print(result)