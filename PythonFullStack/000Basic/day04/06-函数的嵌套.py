#函数的嵌套:在函数里面定义一个函数
def show():
    def test():
        print("哈哈在另外一个函数里面")
    #不可以在代码块外部调用,test就是局部函数
    test()

show()
