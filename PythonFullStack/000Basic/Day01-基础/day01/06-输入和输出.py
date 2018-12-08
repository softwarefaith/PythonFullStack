#输出
print("helloworld")

mystr1 = "hello"
mystr2 = "world"
#输出多个变量的时候，中间会有分隔符（默认的分隔符是空格）
print(mystr1,mystr2)
#修改输出的分隔符
print(mystr1,mystr2,sep="&")
#print函数默认输出之后会换行
print("1",end="zhangsan")
print("2",end="\n\n")
print("3")
#输入：获取用户键盘输入的文字（python2 raw_input）
result = input()
print("打印输入的数字",result)