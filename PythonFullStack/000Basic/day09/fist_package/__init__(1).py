#如果外界使用 form 包名 import *不会导入包里所有的模块
__all__ = ["first","second"]

# #从当前包导入对应的模块
# from . import first
# from . import second

from fist_package import first
from fist_package import second