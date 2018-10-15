

# 定义必须参数使用关键字传参的函数, 注意点： *后面的参数必须使用关键字方式传参
def show(address, sex,*, name, age):
    print(address, sex)
    print("我叫:%s 年龄:%d" % (name, age))

# 使用位置参数传参
# show("刘八女", 38)
# 使用关键字参数传参
# show(name="曹操", age=66)


show("上海", '男', name="刘墉", age=92)
show(address="北京", sex="男", name="和珅", age=49)