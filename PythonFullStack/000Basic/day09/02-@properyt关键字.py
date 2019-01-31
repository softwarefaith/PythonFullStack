class Student(object):

    def __init__(self):

        self.__score = 100
    #将方法改成对应属性值
    @property
    def get_score(self):

        return self.__score
    @get_score.setter
    def set_score(self,score):
        #相当于设置score的值
        self.__score = score


stu = Student()
# #
# # stu.set_score(99)
# #
# # score = stu.get_score()
# #
# # print(score)
#99
stu.set_score  = 99
#默认值100
score = stu.get_score

print(score)