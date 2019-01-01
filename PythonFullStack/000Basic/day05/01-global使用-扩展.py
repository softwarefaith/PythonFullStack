# #定义不可变类型的全局变量
# g_num = 10
# print("函数外",id(g_num))
#
#
# def modify():
#     #重新定义了一个局部变量
#     #生命要修改的全局变量,表示要修改全局变量的内存地址
#     global g_num
#     g_num = 1
#     print("函数内",id(g_num))
#
# modify()


# print(g_num)
#定义一盒可变类型的全局变量
g_list = [3,5]
print("函数外",id(g_list))
def modify():
    #在原有基础航添加了一条数据
    # global g_list
    #不可变类型,可以在函数代码块里面直接修改
    #无论增加还是不增加global不会改变内存地址
    # g_list.append(4)
    # print(g_list)
    # print("函数内",id(g_list))
    #局部变量
    #加上global表示内存地址要发生变化
    global g_list
    g_list = [1,2]
    print(g_list)
    print("函数内",id(g_list))


modify()

print(g_list)