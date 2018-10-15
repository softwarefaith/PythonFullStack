# 函数就是实现某个功能的代码块，提高代码的复用性
# 无参数无返回值的函数
def show():
    print("大家好，今天的天气不好！！！")

# 函数的调用，函数名(参数)
show()


# 有参数无返回值的函数
def show(name, age):
    print("我叫:%s 年龄:%d" % (name, age))

show("张三丰", 108)


# 无参数有返回值的函数
def return_value():
    msg = "好好学习，天天向上."
    return msg

# 调用有返回值函数并使用变量进行保存
result = return_value()
print(result)


# 有参数有返回的函数
def show_msg(name, age):
    msg = "我叫:%s 年龄:%d" % (name, age)
    return msg

result = show_msg("李四", 40)

print(result)
