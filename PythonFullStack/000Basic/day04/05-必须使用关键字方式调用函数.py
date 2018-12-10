#必须使用关键字方式调用
def show(address,sex,*,name,age):
    print(name,age)

# show(name=12,age =14)

show("上海","男",name="张三",age=18)
show(address="上海",sex="女",name="李四",age=99)
#不定长位置参数
abs()