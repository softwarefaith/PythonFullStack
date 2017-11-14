# 文件读写
""""""
"""

StringIO和BytesIO是在内存中操作str和bytes的方法，使
得和读写文件具有一致的接口。


"""


try:

    f = open('../a.text', 'w')
    f.write('Hello Word')

finally:

# 文件使用完毕后必须关闭，
# 因为文件对象会占用操作系统的资源，
# 并且操作系统同一时间能打开的文件数量也是有限的：
    f.close()

"""
如果文件很小，read()一次性读取最方便；
如果不能确定文件大小，反复调用read(size)比较保险；
如果是配置文件，调用readlines()最方便：

也可调用 readline() 每次读取一行内容；
而调用readlines()可以一次读取所有内容并按行返回list
"""

# file-like Object
"""
像open()函数返回的这种有个read()方法的对象，
在Python中统称为file-like Object。
除了file外，还可以是内存的字节流，网络流，自定义流等等。
file-like Object不要求从特定类继承，只要写个read()方法就行。

StringIO就是在内存中创建的file-like Object，常用作临时缓冲。

在Python中，文件读写是通过open()函数打开的文件对象完成的。使用with语句操作文件IO是个好习惯。

"""

with open('../a.text', 'r') as f:
    text = f.read()
    print(text)

#

from  io import StringIO

f = StringIO()
f.write('Hello')
f.write('')
num = f.write('Word!')  # 返回写入字符串的长度

print(num)

print(f.getvalue())

f1=StringIO('My name is Allen.')

while True:
    s = f1.readline()
    print(s)


# BytesIO

from io import BytesIO  #操作与 StringIO一样


