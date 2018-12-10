#关键字不定长参数,位置不定长参数,必选参数
# def show(name,age,*args,**kwargs):
#     print(name,age,args,kwargs)
#
# #不能使用此种方式去调用函数,因为前面使用关键字方式调用函数了
# # show(name="李四",age=18,1,2,3,aa=1,bb=2)
# show("李四",18,12,13,aa=12,bb=13)
#不可以的,**kwargs必须放在参数的最后面
# def show(**kwargs,name,age,*args,):
#     print(name,age,args,kwargs)
#一般不情况下不要这么写
# def show(*args,name,age,**kwargs):
# #     print(name,age,args,kwargs)
# #
# # show(1,2,name=3,age=4,aa=5,bb=6)
#最常见的方式
def show(name,age,*args,**kwargs):
    print(name,age,args,kwargs)