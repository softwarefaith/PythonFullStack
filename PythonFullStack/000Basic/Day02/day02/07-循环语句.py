#循环(for while):根据条件循环执行某种惭怍

#死循环(最长见的BUG之一,造成cpu负载量过大,1001)
#非0即真
#0=False 其他代表True
#执行5次循环
# num = 0
# while num <=5:
#     num +=1
#     print("hello world")

#for循环 结合range range指一个范围
#range
# for value in range(5):
#     print(value)

#(1,6,2)起始数据,和结束数据(结束数据默认不打印,)步长(跳跃间距)
#如果没有设置起始数据,默认从0开始
#步长,默认是1
# for value in range(1,6,2):
#     print(value)
#for循环和whlie循环可以结合else使用
num = 5
while num >= 1:
    print(num)
    num -=1
else:
    print("循环数据结束")

for value in range(3):

    if value == 2:
        print("ok")
    print(value)
else:
    print("循环结束")



