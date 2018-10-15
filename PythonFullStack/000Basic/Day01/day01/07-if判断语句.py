
#默认你输入的文字，返回值是str类型
age = int(input("请输入你的年龄："))
print(type(age))
#判断语句，满足条件才执行
if age >= 15 and age<=17:
    print("青少年")
elif age > 17 and age <=40:
    print("中年")
else:
    print("老年")
#比较运算符 > < == >= <=
#比较运算符使用完毕之后会返回给一个bool值给你
result = 10 != 10
print(result)
#条件为TRUE的时候才可以执行
if result:
    print("条件成立")