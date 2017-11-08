# 笔记
"""
"""


# 模块
"""
为了编写可维护的代码，我们把很多函数分组，
分别放到不同的文件里，这样，每个文件包含的代码就相对较少，
很多编程语言都采用这种组织代码的方式。
在Python中，一个.py文件就称之为一个模块（Module）。

"""

# 模块好处

"""
使用模块有什么好处？

1. 最大的好处是大大提高了代码的可维护性。

2. 复用性.
当一个模块编写完毕，就可以被其他地方引用。

我们在编写程序的时候，也经常引用其他模块，
包括Python内置的模块和来自第三方的模块。

3.可以避免函数名和变量名冲突.
尽量不要与内置函数名字冲突

"""

# Python 表现形式

"""
为了避免模块名冲突
Python又引入了按目录来组织模块的方法，称为包（Package）.
引入了包以后，只要顶层的包名不与别人冲突，那所有模块都不会与别人冲突


Python 模块化 存在两种方式:
1.  .py 文件
2.  目录形式
"""

# Python 包的规范

"""
1.包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，
否则，Python就把这个目录当成普通目录，而不是一个包。

2. __init__.py可以是空文件，也可以有Python代码，
因为__init__.py本身就是一个模块，而它的模块名就是 目录名

3.创建模块时要注意命名，不能和Python自带的模块名称冲突

4.可以有多级目录，组成多级层次的包结构

abc.py ,Web文件夹 在MyProduct 目录下
-- MyProduct
    -abc.py
    --Web
        -cde.py



则模块的名字变为了 MyProduct.abc
MyProduct.Web.cde



"""


"""
导入模块其实就是告诉Python解释器去解释那个py文件

导入一个py文件，解释器解释该py文件
导入一个包，解释器解释该包下的 __init__.py 文件

#路径问题
导入模块时是根据那个路径作为基准来进行的呢？即：sys.path
如果sys.path路径列表没有你想要的路径，
可以通过 sys.path.append('路径') 添加。

"""