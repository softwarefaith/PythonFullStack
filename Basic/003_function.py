def python_function(name, age, address='BJ'):
    print('name:', name, 'age:', age, 'address:', address)

python_function('cai', 27)

python_function(age=30, address='SH', name='Allan')

"""
如果未在函数中指定return,那这个函数的返回值为None 
非固定参数
*args 会把多传入的参数变成一个元组形式
"""


def more_function(name, age, *args):
    print('name:', name, 'age:', age, 'arg:', args)

more_function('Allan', 50, 'BJ', 'SH')


def more_key_function(name, age, **args):
    print('name:', name, 'age:', age, 'arg:', args)

more_key_function("Allan", 30, school='BJ', country='China')

"""
匿名函数****
"""

calc=lambda a, b: a * b

print(calc(2, 4))

