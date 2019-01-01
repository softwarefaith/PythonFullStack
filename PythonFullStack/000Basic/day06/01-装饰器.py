#装饰器就是一个函数,可以给原函数增加功能(在不改变原函数的基础上)




#装饰器函数
def decorator(new_func):

    def inner():
        print("----")
        #是show函数
        new_func()
    #所有的返回值返回的值函数的名字
    #如果加上()编程函数的调用
    return inner

# show = decorator(show)
#语法糖修饰(修饰show函数,给show函数增加新的功能)
@decorator#-->show = decorator(show)
def show():
    print("AAA")

#调用inner,不是调用最上方的show
show()




