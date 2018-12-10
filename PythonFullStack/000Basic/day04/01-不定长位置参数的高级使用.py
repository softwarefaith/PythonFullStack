
def show_msg(*args):
    print(args)

#定义一个不定长位置参数
def show(*args):
    #
    show_msg(*args)
    # show_msg(args)

show(10,20)