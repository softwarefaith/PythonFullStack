#装饰器:本质上就是一个函数,可以给原函数的功能进行扩展
#不改变原函数的定义和调用的操作

def show():
    print("AAA")

#在AAA前面给我加上----(装饰器是通过闭包完成的)
#装饰器函数(通过闭包完成的)

def decorator(new_func):
    #定义
    def inner():
        print("---",end=" ")
        #需要调用show,new_func就是show
        new_func()
    return inner
#相当于重新给show赋值()show就是inner
show = decorator(show)
# #相当于调用inner
show()
