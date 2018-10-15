#逻辑运算符 and or not
score = 90
#and代表同事满足左右两侧的条件
if score >= 90 and score <= 100:
    print("优秀")
#or 只要左右两侧满足一个条件就可以执行
num =1
if num == 1 or num == 2:
    print("这个数字是我需要的")
#not：对结果进行去反
#num == 2 会返回一个false not了一下相当于取反 True
if not num == 2:
    print("helloworld")