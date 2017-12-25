# Author: wadeson
# date: 2017/12/17


class Foo:
    __v = "static"

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.__gender = gender

    def show(self):
        return self.__v

    @staticmethod
    def sta():
        return Foo.__v

obj = Foo("jsonhc", 25, "F")
print(obj.name)
print(obj.show())
print(Foo.sta())



