#!/usr/bin/env python3


# 整型
pyInt = 0
# 长整型
pyLong = 1.999
# 浮点型
pyFloat = 3.4

# 复数

# ==========字符串(不可修改)
pyString = 'Hello word'

# ---常用的功能:移除空白  分割 长度 索引 切片

# ===========列表

# ---创建
py_list0 = ["001", '002', '003','004', '005']

py_list1 = list(['004', '005', '006', '007'])

# ---基本操作
# ---索引 切片 追加 删除 长度 循环 包含

print("list", py_list0[0])  # 通过下标访问,从0开始 -- length - 1
print("list", py_list0[-1])  # 下标倒取:-1代表访问最后一个元素

print("切片[1: 2]", py_list0[1: 2])  # [头:尾] == [头, 尾) 半开区间
print("切片[1:]",  py_list0[1:])    # 包括最后一个元素
print("切片[:2]", py_list0[: 2])   # 从头开始
print("切片[1: -1]", py_list0[1: -1])

print("切片[0:: 2]", py_list0[0:: 2])  # 每隔多少元素取一个

py_list0.append("006")
print("追加006",py_list0)


py_list0.insert(-100, '007')   # 插入时,index>length 依然最后插入; -index < 0,在首插入
print("插入008", py_list0)

py_list0[0] = '我把0修改了'
print("修改", py_list0)

del py_list1[0]   # 删除的索引不存在报错 IndexError: list assignment index out of range
print("删除004", py_list1)

py_list1.remove("005")
print("删除005", py_list1)

py_list1.pop(0)  # 删除最后一个
print("pop第一个元素", py_list1)

py_list1.pop()  # 删除最后一个
print("删除最后一个", py_list1)


e = ["100", '101', """102""", '100', '101']  # 结尾扩展
py_list1.extend(e)
print("扩展元素", py_list1)

print('统计100个数', py_list1.count('100'))

listCopy = py_list1.copy()  # 拷贝
print('list copy', listCopy)
listCopy.append("list copy 添加元素后")
print('对比', listCopy, 'pylist', py_list1)

listCopy.sort()
print('list copy 排序', listCopy)

listCopy.reverse()
print('list copy 反转', listCopy)

index = listCopy.index('100', 2, 5)  # 结束位置不包括, 找不到报错
print('list copy 100位置', index)


# 其他列表操作符
list_Length = len(listCopy)  #长度

['Hi'] * 4  # 重复

['H'] + ['My Name is Allan']   # 组合列表

'100' in listCopy

# ============元组(不可变列表)

# ---创建
py_tuple0 = (11, 22, 33)


py_tuple1 = tuple((44, 55, 66))

py_tuple3 = (88, )   # 一个元素需要后面加逗号

py_tuple4 = py_tuple0 + py_tuple3

# 只有两个方法 count  index  读取与list一样

py_tuple0.count(11)
py_tuple0.index(55)






