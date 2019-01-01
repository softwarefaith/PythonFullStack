#
# #返回函数:
# #函数嵌套,在函数里面返回一个函数
# def show():
#
#     def show1():
#         print("haha")
#     #返回了一个函数
#     return show1
# #new_func就是show1
# new_func = show()
# #指定返回的函数
# new_func()

#返回函数是高阶函数的一种
def calc(operation):

    if operation == "+":
        def sum_num(num1,num2):

            result =num1 + num2
            return result
        #返回函数不需要加()
        return sum_num
    if operation == "-":
        def jq_num(num1,num2):

            result = num1 - num2

            return result
        return jq_num

#根据传入的不同参数,返回不同函数(返回函数重要的意义所在)
new_func = calc("+")

result = new_func(1,2)

print(result)
