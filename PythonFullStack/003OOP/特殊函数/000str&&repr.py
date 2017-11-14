class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return "{__class__.__name__}(name={name!r},age={age!s})".format(__class__=self.__class__, **self.__dict__)

    def __str__(self):
        return "{name!r}+{age!r}".format(**self.__dict__)

# '{}'的内容会被format()中的参数所替代，可以在'{}'里填上数字来指定format()中的位置，
# 但是如果'{}'里的是参数，其中的内容会以被format()中的字符替换

#  {__class__.__name__}  通常模板
#  {!r}  {!s}  格式

p = Person("Allan", 20)

print(repr(p))

print(str(p))