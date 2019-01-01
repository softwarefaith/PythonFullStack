#read readline readlines,读取文件的操作
# file = open("1.txt","r",encoding="utf-8")
# #读取全部的数据
# #r模式读取是指定数据的长度
# result=file.read(1)
# print(result)
# file.close()

#以二进制方式读取
# file = open("1.txt","rb")
# #以二进制方式读取文件,是按照字节数读取的
# result = file.read(3)
# file_data=result.decode("utf-8")
# print(file_data)
#根据指定的文件指针读取数据
# file = open("1.txt","rb")
# #查看文件指针的位置
# result = file.tell()
# print(result)
# # #设置文件的指针(偏移指针)
# file.seek(3)
# #查看当前指针
# result = file.tell()
# print(result)
# #
# file_data = file.read()
#
# content = file_data.decode("utf-8")
# print(content)
#readline--------------
# file = open("2.txt","rb")
# # #只读取一行数据,当读取数据遇到"\n"的时候结束读取
# # file_data = file.readline()
# # #解码
# # print(file_data.decode("utf-8"))
# # file.close()
#readlines
file = open("2.txt","rb")
#文件中的数据按照每行去读取,把每行的数据放到一个列表里面
file_data = file.readlines()
# print(file_data)
for data in  file_data:
    #print函数默认换行
    print(data.decode("utf-8"),end="")
file.close()