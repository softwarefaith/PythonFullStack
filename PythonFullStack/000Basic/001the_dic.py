# ==========字典
"""
Key唯一性
无顺序
去重
查询速度快，比列表快多了
比list占用内存多
"""
# ---创建

py_Dic0 = {"name": 'cai', "age": 28}

py_Dic1 = dict({"name": 'jie', 'age': 29})

# ---常用操作
# ----索引,新增,删除, 键|值|键值对, 循环 ,长度

py_Dic0['address'] = "bj"
py_Dic0['school'] = "ln"
py_Dic0['sex'] = "M"
print("增加元素", py_Dic0)

py_Dic0['address'] = 'ShanXi'
print("修改元素", py_Dic0)

# pop不到 会报错 但是设置默认值 找不到返回默认值
py_Dic0.pop('sex')
py_Dic0.pop('sex888', '000')

del py_Dic0['address']
print("删除元素", py_Dic0)

py_Dic0.popitem()  #删除最后一个
print("删除元素", py_Dic0)


# ====查找

#  get方法也可以设置默认值  get 不到返回默认值
print("索引", py_Dic0.get('name'),'获取',py_Dic0['name'])

# py_Dic0['name222']
  #get不到只返回None
print("索引不到", py_Dic0.get('name222'),'获取')

py_Dic0.keys()
py_Dic0.values()

print("item=", py_Dic1.items())


# ===更新
up = {'s': '001', 'b': '002'}
py_Dic1.update(up)
print("更新后的值", py_Dic1)


