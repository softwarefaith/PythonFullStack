#continue :结束本次循环,然后可以继续下一个循环,整个循环不一定结束
#break:跳出当前循环,并且跳出所有的循环
# num = 1
# while num <= 5:
#     num += 1
#     if num == 2:
#         continue
#     print(num)
# else:
#     print("循环结束")
#break跳出循环,不执行else语句
num = 1
while num <= 5:
    num+=1
    if num == 2:
        break
    print(num)
else:
    print("循环结束")

for value in range(1,5):
    if value == 2:
        break
    print(value)
else:
    print("结束本次循环")
#创建一个列表["张三","李四"]
name = input("请输入你的名字:")
for value in ["张三","李四"]:
    if value == name:
        print("查找到这个人了")
        break
else:
    print("没有找到这个人")



