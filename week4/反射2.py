# Author: wadeson
# date: 2017/12/24


class Foo:
    stat = 123

    def __init__(self, name, age):
        self.name = name
        self.age = age

ret = getattr(Foo, "stat")
print(ret)