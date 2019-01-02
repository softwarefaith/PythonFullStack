#导入模块
#比较重要的模块
import os
# file = open("4.txt","w",encoding="utf-8")
# file.write("abc")
# file.close()
# #重命名一下
# os.rename("4.txt","444.txt")
# #创建文件夹(不能创建,同样名字的文件夹)
# #默认在当前路径帮助我们创建(pycharm的路径)
# os.mkdir("AAA")
#给文件夹改名字(如果没有目标文件会报错)
# os.rename("AAA","BBB")

#创建文件夹下方的文件
#1.指定路径创建
# file = open("BBB/1.txt","w",encoding="utf-8")
# file.close()
# #切换到指定BBB目录创建,默认是py文件操作的目录
# #查看操作目录的路径
# current_path = os.getcwd()
# print(current_path)
# #切换到指定的目录(切换到)
# os.chdir("BBB")
# current_path = os.getcwd()
# print(current_path)
# #切换指定路径后可以直接写文件的名字,在当前指定的路径下创建文件
# file = open("2.txt","w",encoding="utf-8")
# file.close()
#修改文件夹下方文件的名字
#同样也分为两种:1.修改路径下的,2.切换路径直接修改
#当前目录py文件的目录(切换目录之后不可以指定路径去修改,会报错)
# os.rename("BBB/1.txt","BBB/3.txt")


#删除文件
# os.remove("BBB/2.txt")
# os.remove("BBB/3.txt")
#删除文件夹(如果没有文件夹不可以删除)
os.rmdir("BBB")