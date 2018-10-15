import sys

# 递归函数： 在函数里面在调用函数本身就是递归函数
# 递归函数的特点: 1. 传递  2. 回归

# 5! = 5 * 4!
# 4! = 4 * 3!
# 3! = 3 * 2!
# 2! = 2 * 1!
# 1! = 1

def calc_num(num):
    # 当计算1的阶乘的时候不需要往下传递需要返回结果
    if num == 1: # 必须要设置结束递归的条件及返回值
        return 1
    else:
        return num * calc_num(num-1)

# 获取默认的递归次数
result = sys.getrecursionlimit()
print(result)

# 设置递归次数
sys.setrecursionlimit(1100)

result = sys.getrecursionlimit()
print(result)



result = calc_num(1000)
print(result)

# 注意点：1. 不能无限递归调用，默认是递归调用的次数1000，一般都是1000次所有
