#格式化符号：%s %d %f %x
#%s:输出字符串
#%d：输出int类型
#%f 输出float类型
#%x输出16位进制数据
name = "张三丰"
print("我叫%s" % name)
score = 100
print("python的考试分数：%d" % score)
#格式化之后，小数保留6位，四舍五入
pi = 3.1415926
print("圆周率：%f" %pi)
#2进制，8进制，10进制 16进制
num = 16
print("%x"%num)


s = 'abcdef'
s.replace('abc','eeeeee')
print(s)