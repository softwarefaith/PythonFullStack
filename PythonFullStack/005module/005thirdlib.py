# os 模块 用于提供系统级别的操作
""""""

"""
Python的标准库中的os模块包含普遍的操作系统功能。
这个模块的作用主要是提供与平台无关的功能。
也就是说os模块能够处理平台间的差异问题，
使得编写好的程序无需做任何改动就能在另外的平台上运行。
当然，这个模块只是提供了一个轻便的方法使用要依赖操作系统的功能。
有些特定的功能还得使用特定的模块
"""


# sys 用于提供对解释器相关的操作

# hashlib
# 用于加密相关的操作，代替了md5模块和sha模块，主
# 要提供 SHA1, SHA224, SHA256, SHA384, SHA512 ，MD5 算法

import hashlib


h = hashlib.md5()
h.update(bytes('admin', encoding='utf-8'))  #对admin字符进行加密


print(h.hexdigest())

#  hmac 模块
# 它内部对我们创建 key 和 内容 再进行处理然后再加密

import  hmac

myhmac = hmac.new(b'key')
myhmac.update(b'message')

print(myhmac.hexdigest())

# json 和 pickle

"""
json，用于字符串 和 python数据类型间进行转换
ppickle，用于python特有的类型 和 python的数据类型间进行转换

dumps():把任意对象序列化成一个str
ddump() 直接把对象序列化后写入一个file-like Object：

反序列化:
loads()
load()


"""
"""
Python提供两个模块来实现序列化：cPickle和pickle。这两个模块功能是一样的，区别在于cPickle是C语言写的，速度快，pickle是纯Python写的，速度慢，
跟cStringIO和StringIO一个道理。
用的时候，先尝试导入cPickle，如果失败，再导入pickle：

try:
    import cPickle as pickle
except ImportError:
    import pickle

"""


"""
Python语言特定的序列化模块是pickle，
但如果要把序列化搞得更通用、更符合Web标准，
就可以使用json模块。


json模块的dumps()和loads()函数是定义得非常好的接口的典范。当我们使用时，只需要传入一个必须的参数。
但是，当默认的序列化或反序列机制不满足我们的要求时，
我们又可以传入更多的参数来定制序列化或反序列化的规则，
既做到了接口简单易用，又做到了充分的扩展性和灵活性。

"""

import json

class Student(object):
    def __init__(self):
        self.name = "Allan"
        self.age = 22

s = Student()

def student2dict(std):
    return {
        'name': std.name,
        'age': std.age

     }

print(json.dumps(s, default=student2dict))

"""
执行shell命令的相关的模块和函数的功能
均在 subprocess 模块中实现，并提供了更丰富的功能
"""