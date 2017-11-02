# random

import random

# 生成随机浮点数:[0, 1]

random.random()

# 指定范围随机浮点数

random.uniform(100, 200)

# 指定范围内的整数

random.randint(100, 300)

# 指定范围内，按指定基数递增的集合中获取一个随机数，基数缺省值为1

random.randrange(100, 200, 10)   # 10 为步长

# 从序列中获取一个随机元素，参数sequence表示一个有序类型，
# 并不是一种特定类型，泛指list，tuple，字符串等

random.choice('abcdefh')

# 用于将一个列表中的元素打乱

list = ['a', 'b', 'c']

random.shuffle(list)

# 从指定序列中随机获取k个元素作为一个片段返回，
# sample函数不会修改原有序列

random.sample('1234567890', 3)


