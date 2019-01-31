g_num = 10
#定义函数
def show_info():
    print("show_info")

def sum_num(num1,num2):
    result = num1+num2
    return result


#判断是否值主模块
#如果是当前模块就去执行下方代码
# if __name__ == "__main__":
    # 主模块:执行的这个模块就叫做主模块
print(__name__)
    # value = sum_num(1,2)
    # print(value)



