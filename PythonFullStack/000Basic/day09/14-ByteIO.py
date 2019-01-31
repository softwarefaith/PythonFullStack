from io import BytesIO

byte_io = BytesIO()

#向内存写入二进制数据
byte_io.write("哈哈".encode("utf-8"))
#读取数据,获取写入内存中的全部数据
data = byte_io.getvalue()
#需要设置光标
# data=byte_io.read()
print(data)
content = data.decode("utf-8")
print(content)
#固定内存地址
str = "100"
#找到内存地址拼接
#创建了一个内存地址
# 创建内存地址(复制上一个内存地址,)
