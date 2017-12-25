# Author: wadeson
# date: 2017/12/20


class Foo:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __add__(self, other):
        return Foo(obj1.name, obj2.age)    # 当然这里也可以返回一个Foo的对象

    def __del__(self):       # 析构方法，对象被销毁时（什么时候销毁并不知道），python内部进行自动执行回收
        pass

obj1 = Foo("hello", 10)
obj2 = Foo("world", 11)
r = obj1 + obj2    # 两个对象相加的时候，自动执行第一个对象的__add__方法，并且将第二个对象当作参数传递到该方法中
print(r)
