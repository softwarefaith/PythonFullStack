# 缺省参数： 在函数定义的时候参数就有值，那么像这样的参数叫做缺省参数
# 提示： 如果给缺省参数传值就是传入的值，
# 如果不给缺省参数传值那么就使用默认值(缺省值)


def sum_num(num1, num2=1):
    result = num1 + num2
    return result

# 没有给函数的第二个参数传值，那么使用默认值（缺省值）
value = sum_num(1, 5)

print(value)
# # 如果有必选参数和缺省参数，那么缺省参数要放到必选参数后面
def sum_num(a=1, b=1):
    pass
