#1.打开源文件读取数据
#rb:比较通用的方式,可以兼容不同的文件
src_file = open("3.txt","rb")
#读取文件中全部的数据(大文件不行)
dst_file = open("/Users/zhangzhihao/desktop/5.txt","wb")
while True:
    file_data = src_file.read(1024)
    #判断数据是否读取完毕
    #判断file_data数据是否为None
    if file_data:
        dst_file.write(file_data)
    else:
        print("数据读取完成",file_data)
        break

#打开目标文件准备写入数据
#扩展一下:默认写到pychram里面,
# Users/用户名/desktop 我桌面的路径

#把源文件的内容写入到目标文件

#关闭文件
dst_file.close()
src_file.close()
