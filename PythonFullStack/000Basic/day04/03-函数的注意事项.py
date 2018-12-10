#函数的注意事项:1.函数不能相同(注意,第二个函数会把第一个函数覆盖掉)
#2.变量名不能和函数名一样
def show():
    print("好累啊")

def show():
    print("一点都不累")
#
# show()

show = 10
print(show)
#拿着变量名去调用函数
show()
