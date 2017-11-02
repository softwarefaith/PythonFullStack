# 记录错误
""""""
"""
如果不捕获错误，自然可以让Python解释器来打印出错误堆栈，
但程序也被结束了。既然我们能捕获错误，就可以把错误堆栈打印出来，
然后分析错误原因，同时，让程序继续执行下去。

Python内置的logging模块可以非常容易地记录错误信息：
"""


import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('END')

"""
同样是出错，但程序打印完错误信息后会继续执行，并正常退出：
通过配置，logging还可以把错误记录到日志文件里，方便事后排查。


"""