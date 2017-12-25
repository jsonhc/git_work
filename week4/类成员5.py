# Author: wadeson
# date: 2017/12/24


class Mytype(type):
    def __init__(self, *args, **kwargs):
        print(123)

    def __call__(self, *args, **kwargs):            # 这里的self也就是Mytype的对象，也就是Foo类
        obj = self.__new__(self, *args, **kwargs)
        self.__init__(obj)


class Foo(object, metaclass=Mytype):
    def __init__(self):
        print(345)

    def __new__(cls, *args, **kwargs):
        return object.__new__(cls, *args, **kwargs)

obj = Foo()
# 由于Foo类是Mytype的对象，所以当Foo类创建的时候就会执行Mytype这个类的构造方法，由于Foo类是Mytype的对象，所以加上()后就会调用Mytype类的__call__方法，在Mytype
# 这个类中的self就是Mytype类的对象，也就是Foo类，所以self是Foo这个类，由于obj是Foo类的对象，对象obj是由Foo类中的__new__方法创建的，创建完Foo类的对象后，于是执行Foo
# 的构造方法__init__
