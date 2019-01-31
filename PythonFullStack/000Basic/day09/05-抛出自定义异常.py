#自定义异常类
#自定义异常类必须继承Exception
class CustomExcepition(Exception):
    def __init__(self,content):

        self.content = content
    #表示抛出异常的描述信息
    def __str__(self):
        return "我是自定义异常,因为数据不是a,所以有异常,异常数据为:%s" %self.content

content = input("请输入数据")
if content !="a":
    #抛出自定义异常
    raise CustomExcepition(content)
    #raise只能抛出异常类型
    # raise NameError("抛出系统的异常")
