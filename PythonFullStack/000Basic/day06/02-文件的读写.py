#文件的访问模式:
#1.r:只读,文件不存在会崩溃
#2.w:只写
#3.a:追加写入
#4.rb:以二进制方式读取文件数据:常用
#5.wb:以二进制方式写入文件数据:常用
#6:ab:以二进制方式增加文件数据:常用
#爬视频,图片数据,文本数据,音频数据
# r+ w+ a+ 支持读写
#rb+ wb+ ab+ 支持二进制方式读写操作





#打开文件使用open函数
#------------r模式(只读)-----------
# 如果没有此文件会崩溃
# file = open("1.txt","r",encoding="utf-8")
# #读取文件中所有的数据
# content = file.read()
# print(content)
# #必须关闭
# file.close()
#--------w模式----------------------
#提示:如果文件不存在,会创建一个文件并打开,
#encoding="utf-8"设置编码方式(mac.linux)
#GBK cp936
#提示:w模式:如果文件存在,那么会文件中,原有数据清空,在写入数据
# file = open("1.txt","w",encoding="utf-8")
#1.txt写入数据
#打开文件后多次写入数据,不会覆盖数据
# file.write("A")
# file.write("哈哈")
# file.write("说大事大所大所多")
# #查看当前的编码格式(cp936)
# result = file.encoding
# print(result)
# # 记住所有对于文件的操作,最后一步都是close
# file.close()

#a------------追加数据
#
# file = open("1.txt","a",encoding="utf-8")
# file.write("BBB")
# file.close()
#在python2里面是不支持中文:
#python3默认支持中文
#_*_ coding:utf-8
# print("啊哈哈")
#rb-----------以二进制方式读取数据
file = open("1.txt","rb")
#binary mode doesn't take an encoding argument
#如果是二进制方式不需要指定编码格式
#读取数据
#中文打印会出现\xe5 一个中文三个字节
# file_data = file.read()
# #解码的操作
# content = file_data.decode("utf-8")
# #打印的就是解码后的数据
# print(content)
# #不支持写入数据
# file.write("aaaa")
#
# file.close()
#wb--------------以二进制方式写入数据
#前面是w就会覆盖原来的数据
# file = open("1.txt","wb")
# content = "hello 哈哈"
# #content包装成二进制人间,对content进行二进制编码
# file_data =content.encode("utf-8")
# file.write(file_data)
# file.close()
#ab-------二进制方式追加数据
# #如果两种模式同时存在,下方代码不会执行
# file = open("1.txt","ab")
# content = "hello"
# #追加也必须是二进制人间
# file_data =content.encode("utf-8")
# file.write(file_data)
# #不可读数据
# file.close()
#r+-------------------读写
#为了兼容不同操作系统,只要没有看到b模式就可以使用encoding方式指定编码
#基本操作,很多的坑
#正则表达式
file = open("1.txt","r+",encoding="utf-8")
file.write("abc")
result = file.read()
print(result)
file.close()
