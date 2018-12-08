# 函数的注意事项： 1. 函数名不能相同， 2.变量名不能和函数名相同
#
def show():
    print("好累呀")

# show()
def show(msg):
    print(msg)
# 提示：如果定义了第二个函数名和第一个函数名相同，那么第一个函数不能使用
# show("哈哈，逗大家玩")

# 定义变量名和函数名相同
show = 10

print(show)

show("哈哈，逗大家玩")
