# def decorator3(func):
#     def inner():
#         print("BBB")
#         func()
#
#     return inner
# def decorator2(func):
#     def inner():
#         print("CCC")
#         func()
#
#     return inner
# def decorator1(func):
#     def inner():
#         print("AAA")
#         func()
#     return inner
#
# @decorator3()
# def shwo():
#     print("1111")
# shwo()
#111前面加上BBB

#定义一个增加参数的装饰器
def get_decorator(char):
    #装饰器函数
    def decorator3(func):
        def inner():
            print(char)
            func()
        return inner
    return decorator3

@get_decorator("ccc")
def show():
    print("111")

show()

