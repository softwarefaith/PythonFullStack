#---------------import导入包里面的模块-------------

# import fist_package.first #推荐方式1
# import fist_package.second
#
# #使用包模块里面的代码
# fist_package.first.show()
# fist_package.second.show_msg()

#---------------import导入包里面的模块设置别名-------------

# import fist_package.first as one
# import fist_package.second as two
# one.show()
# two.show_msg

#-------form导入包名 import模块名 推荐方式2
# from fist_package import first as one
# from fist_package import second
#
# one.show()
# second.show_msg()

#-----from包名.模块名 import 功能代码
# from fist_package.first import show
#需要保证当前模块没有导入模块的功能代码(不推荐)
# def show():
#     print("哈哈")
# show()

#from 包名 imort*,导入包里所有的模块
#导入,去指定导入的模块(在__init__)
#__all__去指定导入的模块
# from fist_package import *
# first.show()
# second.show_msg()


#直接导入包,不会导入对应的模块
#需要在init文件中自己导入
import fist_package

fist_package.first.show()