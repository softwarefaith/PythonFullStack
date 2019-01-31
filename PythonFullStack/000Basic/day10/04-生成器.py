#生成器:是一个特殊的迭代器,他同样可以通过next函数和for取值
#生成器,占用内存相当少

#值只能往后去不能向前面取值

# #1.使用生成器的表达式
# result = [x for x in range(4)]
# print(result,type(result))

# result = (x for x in range(4))
# print(result,type(result))
#
# #测试:使用next获取下一个值
# value = next(result)
# print(value)
#
# for value in result:
#     print(value)

#2.使用yield创建生成器

def show_num():
    for i in range(5):
        #代码遇到yield会暂停,然后把结果返回过去
        #下次启动生成器会在暂停位置
        #yield特点L:可以返回多次值,renturn只能返回一次
        yield i



g = show_num()
value =next(g)
print(value)

for value in g:
    print(value)