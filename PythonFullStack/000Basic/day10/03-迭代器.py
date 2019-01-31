#扩充:用的不是很多
#在类里面有一个__iter__和__next__方法创建的对象就是迭代器
#作用:根据数据的位置获取下一个位置的值
#根据需要每次生成一个值,不像列表把所有的数据都准备好
#这样的好处占用内存非常小
from collections import Iterable

class MyIterable(object):
    def __init__(self):
        self.mylist = [4,5,9]
        self.current_index = 0
    def __iter__(self):

        #返回迭代器的对象
        return self
    def __next__(self):

        if self.current_index<len(self.mylist):
            #获取迭代器中的下一个值
            result = self.mylist[self.current_index]
            self.current_index +=1
            return result
        else:
            #抛出异常,停止迭代
            raise StopIteration

#创建迭代器
my_iterable = MyIterable()

reslut = isinstance(my_iterable,Iterable)
print(reslut)
#使用迭代器函数获取迭代器中的下一个值
reslut = next(my_iterable)
print(reslut)

reslut = next(my_iterable)
print(reslut)

reslut = next(my_iterable)
print(reslut)

# reslut = next(my_iterable)
# print(reslut)


#for循环内部会自动处理,停止迭代异常
for value in my_iterable:
    print(value)


