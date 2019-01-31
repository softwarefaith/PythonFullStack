# num1 = input("请输入第一个数字:")
# num2 = input("请输入第二个数字:")
#
# result = int(num1) + int(num2)
# print(result)
# #try"里面如果代码遇见了异常,那么不会执行try语句里面的代码
# try:
#     num1 = input("请输入第一个数字:")
#     num2 = input("请输入第二个数字:")
#
#     result = int(num1) + int(num2)
#     print(result)
#
# except ValueError as e:#e表示异常对象
#     #会执行except语句
#     print(e)

#Exception:多数异常类都是继承Exception
# try:
#     num1 = input("请输入第一个数字:")
#     num2 = input("请输入第二个数字:")
#
#     result = int(num1) + int(num2)
#     print(result)
#
# except Exception as e:#e表示异常对象
#     #会执行except语句
#     print("请输入合法数字")
#     print(e,type(e))
#捕获多个异常:了解一下

# try:
#     name = "zs"
#     del name
#     print(name)
#
#     result = 1 / 0
#     print(result)
#
# except (NameError,ZeroDivisionError) as e:
#     print("有错误")
#     print(e,type(e))

# try:
#     # name = "zs"
#     # del name
#     # print(name)
#
#     result = 1 / 0
#     print(result)
#
# except Exception as e:
#     print("有错误")
#     print(e,type(e))
# try:
#     # name = "zs"
#     # del name
#     # print(name)
#
#     result = 1 / 0
#     print(result)
#
# except NameError as e:
#     print("有错误")
#     print(e,type(e))
# except ZeroDivisionError as e:
#     print("有错误")
#     print(e,type(e))



try:
    # name = "zs"
    # del name
    # print(name)

    result = 1 / 0
    print(result)

except Exception as e:
    print("有错误")
    print(e,type(e))
else:
    print("没有异常会执行else里面的语句")
finally:
    print("有没有异常都会执行这个语句")