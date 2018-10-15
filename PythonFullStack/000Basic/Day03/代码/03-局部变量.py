# 局部变量： 在函数内定义的变量叫做局部变量，局部变量只能在函数内使用，
# 不能在函数外使用


def show():
    # 局部变量
    score = 100
    print("分数:", score)

# show()
# print(score)

def show_msg():
    print(score)

show_msg()
