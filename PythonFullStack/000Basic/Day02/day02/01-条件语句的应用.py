#1接受用户输入的数据
score = int(input("请输入您的分数:"))

#2.判断学生的分数,根据分数输出不同的数据
if score >=90 and score <=100:
    print("优秀")
elif score >=80 and score <90:
    print("良好")
elif score >= 70 and score < 80:
    print("良好")
elif score >= 60 and score <70:
    print("及格")
else:
    print("不及格")
