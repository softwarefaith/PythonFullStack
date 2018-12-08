# 函数的不定长参数： 1. 不定长位置参数 2. 不定长关键字参数

# 不定长参数： 调用函数的时候不确定传入多少个参数，可能是0个或者多个参数

# 定义函数的时候：1. 不定长位置参数 2. 不定长关键字参数


# --------------不定长位置参数函数的定义及调用-------------

# 定义一个不定长位置参数(*args)
def sum_num(*args):
    # 提示： args： 会把调用函数传入的位置参数封装到一个元组里面，
    # 如果没有传入参数那么是一个空元组
    print(args, type(args))

    # 计算结果变量
    result = 0
    for value in args:
        result += value

    return result
#
#
#
# # 调用不定长位置参数的函数
# value = sum_num(1, 4, 5, 6)
# print(value)

# 注意点： *args:表示定义的函数是不定长的位置参数，
# 调用函数的时候只能使用位置参数传值，不能使用关键字
# result = sum_num(a=1, b=2, c=3)
# print(result)

# --------------不定长关键字参数函数的定义及调用-------------

# 定义不定长关键字参数函数， **kwargs: 表示的就是一个不定长关键字参数
def show_msg(**kwargs):
    # kwargs: 会把函数调用的关键字参数封装到字典里面
    print(kwargs, type(kwargs))

    for key, value in kwargs.items():
        print(key, value)

# 调用的不定长关键字参数的函数
show_msg(a=1, b=2)

# 不能使用位置参数给不定长关键字函数传参
# show_msg(1, 2)
















