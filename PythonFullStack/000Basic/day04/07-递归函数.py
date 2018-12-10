import sys
#不常用
#递归函数:在函数里面调用函数本身就是递归函数
#递归函数的特性:1.传递.2.回归
#死循环
# def show():
#     show()
#
# show()
#阶乘
# 5 = 5 *4!
# 4 = 4 *3!
# 3 = 3 *2!
# 2 = 2 *1!
# 1 = 1

def calc_num(num):
    #当计算到1的阶层的时候不需要传递需要的数据.直接返回
    if num == 1:
        return 1
    else:
        return num *calc_num(num-1)
result =calc_num(5)
# print(result)

#获取默认的递归次数
result=sys.getrecursionlimit()
print(result)
#递归1200
#设置递归次数
# sys.setswitchinterval(1200)
result=sys.setrecursionlimit(1200)
result=sys.getrecursionlimit()
print(result)
#默认递归调用次数是1000