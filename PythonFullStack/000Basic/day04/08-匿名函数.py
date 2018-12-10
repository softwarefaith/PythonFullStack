#匿名函数:没有名字的函数就是匿名函数
#lambda:这个关键字修饰的就是匿名函数
result=(lambda x,y:x+y)(1,2)
print(result)
#匿名函数使用场景:简化代码,
#匿名函数的定义(一般匿名函数就这么使用)
func = lambda x,y:x*y
result = func(1,2)
print(result)

#判断是否是偶数
def is_os(num):
    if num % 2 == 0:
        return True
    else:
        return False
result = is_os(1)
print(result)

#使用匿名函数,判断是否是偶数
new_func = lambda num:True if num % 2 == 0 else False
result = new_func(1)
print(result)
#对字典列表排序可以使用匿名函数
my_list = [2,1,7]
#排序的函数,(从小到大排序,没有返回值,)
my_list.sort()
print(my_list)
my_list = [{"name":"zs","age":19},{"name":"ls","age":12}]
# my_list.sort()
# # print(my_list)
#匿名函数排序字典列表的方式
# my_list.sort(key=lambda item:item["age"])
# print(my_list)

def get_value(item):
    return item["age"]
#正常方式排序列表字典(从小到大)
my_list.sort(key=get_value,reverse=True)
print(my_list)