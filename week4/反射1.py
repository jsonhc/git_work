# Author: wadeson
# date: 2017/12/24


class Foo:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        return "%s %s" % (self.name, self.age)

obj = Foo("hello", 23)
print(obj.name)
