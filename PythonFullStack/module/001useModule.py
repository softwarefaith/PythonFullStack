# 模块使用
"""
"""

# 内置模块
"""

"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '   # 文档注释

__author__ = 'Michael Liao'  # 开发者

import sys    # 模块导入

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

# 在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，
# 而如果在其他地方导入该hello模块时，if判断将失败，
# 因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，
# 最常见的就是运行测试。
if __name__=='__main__':
    test()

# 作用域设置

"""
如果函数和变量我们希望仅仅在模块内部使用。
在Python中，是通过 _ 前缀来实现的。

正常的函数和变量名是公开的（public），可以被直接引用

类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途
类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用

private函数和变量“不应该”被直接引用，而不是“不能”被直接引用，
因为Python并没有一种方法可以完全限制访问private函数或变量，
但是，从编程习惯上不应该引用private函数或变量。

非常有用的代码封装和抽象的方法
"""

# 第三方模块

"""
在Python中，安装第三方模块，是通过包管理工具pip完成的。

如果你正在使用Mac或Linux，安装pip本身这个步骤就可以跳过了。

注意：Mac或Linux上有可能并存Python 3.x和Python 2.x，因此对应的pip命令是pip3。

一般来说，第三方库都会在Python官方的pypi.python.org网站注册，
要安装一个第三方库，必须先知道该库的名称，可以在官网或者pypi上搜索

===Path
默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量中：

如果我们要添加自己的搜索目录，有两种方法：

一是直接修改sys.path，添加要搜索的目录：
>>> import sys
>>> sys.path.append('/Users/michael/my_py_scripts')

二.设置环境变量PYTHONPATH，该环境变量的内容会被自动添加到模块搜索路径中。
设置方式与设置Path环境变量类似。
注意只需要添加你自己的搜索路径，Python自己本身的搜索路径不受影响。

三.Python 安装第三方库的方式
settings之后再点击project下面的project Interprete  搜索库

"""