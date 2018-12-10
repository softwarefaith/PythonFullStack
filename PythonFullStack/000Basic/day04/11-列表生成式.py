# #列表生成式:列表推导式:通俗理解就是使用for虚幻,快速创建一个列表
# #最终目的获取一个列表
# my_list = []
# for i in range(1,6):
#     print(i)
#     my_list.append(i)
# print(my_list)
# #列表生成式的方式创建列表
# my_list = [value for value in range(0,6)]
# print(my_list)
# #统计每个元素的个数
# result =[len(value) for value in ["abc","ab"]]
# print(result)
#
# #给遍历出来的字符串增加字符
# my_list = [value *2 for value in range(1,6)]
# print(my_list)
# my_list = [value + "hello" for value in ["abc","ab"]]
# print(my_list)
#双层循环(1,2,3)(1,2,3)(2):
my_list = [[x,y]for x in range(1,3) for y in range(1,3)]

print(my_list)

# for x in  range(1,3):
#     print(x)
#     for y in range(1,3):
#         print(y)
#结合if语句来使用
my_list = [value for value in range(1,11)if value % 2 ==0]
print(my_list)