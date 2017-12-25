# Author: wadeson
# date: 2017/12/20


class Foo:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __call__(self, *args, **kwargs):
        print("call")

    def __str__(self):
        return "%s %s" % (self.name, self.age)

# obj = Foo()      # 这就表明加载并执行__init__(self)这个构造方法
# obj()         # 这就表明加载并执行了__call__(self, *args, **kwargs)该方法
obj = Foo('hello', 18)
print(obj)              # 这其实操作了两步：1、print(str(obj))    2、str(obj)使得对象obj调用了__str__该方法
print(obj.__str__())

