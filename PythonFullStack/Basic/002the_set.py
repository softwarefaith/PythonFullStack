"""
集合
有如下作用:

去重，把一个列表变成集合，就自动去重了
关系测试，测试两组数据之前的交集、差集、并集等关系
"""

s = set([3, 3, 3, 5, 9, 10])

print('set = ', s)

t = set('Hello')

a = t | s  # 并集

b = t & s  # 交集

c = t - s  # 差集 项在t中 但不在s中

d = t ^ s  # 对称差集(项在t或s中，但不会同时出现在二者中)

"""
基本操作
"""

t.add("My name is Allan")
s.update([12,14,34])

s.remove(14)
print('set = ', s)


12 in s

18 not in s

s.issubset(t)   # 测试是否s中的每一个元素都在 t中

s.issuperset(t)   # 测试是否t中的每一个元素都在 s中

s.union(t)

s.intersection(t)

s.difference(t)

s.symmetric_difference(t)

s.copy()



