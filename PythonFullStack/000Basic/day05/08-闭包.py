# #闭包本质上也是一个函数(高阶函数)
# #在函数嵌套的前提下,内部函数使用了外部函数的参数或者变量
# #并把这个内部函数返回,那么返回的函数就叫做闭包(对应的就是函数)
#
# def show(msg):
#     #外部的变量
#     num = 10
#     def inner():
#         #打印外部的变量,msg外部的参数
#         print(num,msg)
#     #inner它就是闭包
#     return inner
#
# new_func = show("哈哈")
# print(new_func)
# new_func()

#闭包的应用场景:可以根据参数生成不同的返回函数
#通过闭包可以生成不同的函数

def hello(msg,count):

    result = msg *count

    return result

result = hello("A",2)
print(result)
result = hello("A",2)
result = hello("A",2)
result = hello("A",2)
print(result)

def hello(msg,count):

    def return_msg():

        # result = msg *count
        print(msg*count)
        return result

    return return_msg

new_func1 = hello("A",2)
# new_func1()
#new_func1和new_func2不是同一个函数
new_func2 = hello("B",2)
#闭包可以解耦合,根据传入不同的参数,返回不同的函数,
print(new_func1,new_func2)

result1 = new_func1()
#AA
# print(result1)

result2 = new_func2()
#BB
# print(result2)


