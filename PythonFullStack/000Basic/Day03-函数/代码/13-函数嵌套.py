# 函数嵌套： 在函数里面在定义一个函数

def show():
    def test():
        print("哈哈，我是在另外一个函数内")
    # 函数内的函数必须函数内使用，不能在函数外使用
    test()

show()
# test()