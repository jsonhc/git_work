# Author: wadeson
# date: 2017/12/17


class Per:
    @property
    def per(self):
        print(666)

    @per.getter
    def per(self):
        print("get")

    @per.setter
    def per(self, val):
        print(val)

    @per.deleter
    def per(self):
        print("del")


class Foo:
    def f1(self):
        print("f1")

    def f2(self, val):
        print(val)

    def f3(self):
        print("del")

    foo = property(fget=f1, fset=f2, fdel=f3)

obj = Foo()
obj.foo
obj.foo = 123
del obj.foo
print(obj.foo)
