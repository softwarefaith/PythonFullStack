 # def show(name, age, *args, **kwargs):
#     print(name, age, args, kwargs)
#
# # 不能使用下面的方式进行调用，因为前面使用的关键字后面不能使用位置参数
# # show(name="李四", age=18, 1, 4, c=1, b=2)
#
# show("李四", 20, 1, 2, 3, a="苹果", b="香蕉")


# def show(*args, name, age, **kwargs):
#     print(name, age, args, kwargs)
#
# show(1, 2, 3, 4, name='李四', age=20, aa=1, bb=3)

# 注意点： **kwargs必须放到所有参数的最后面
# def show(name, age, *args, **kwargs):
#     print(name, age, args, kwargs)
#
# show(1, 2, 3, 4, name='李四', age=20, aa=1, bb=3)


# 下面的定义可以使用缺省参数
def show(name, *args, age=18, **kwargs):
    print(name, age, args, kwargs)

show("张三", '哈哈', '嘻嘻', a=1)
show("张三", '哈哈', '嘻嘻', age=20, a=1)



