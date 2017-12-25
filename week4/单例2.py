# Author: wadeson
# date: 2017/12/25


class Foo:
    __instance = None

    @classmethod
    def get_instance(cls):
        if Foo.__instance:
            return Foo.__instance
        else:
            Foo.__instance = Foo()
            return Foo.__instance

obj1 = Foo.get_instance()
print(obj1)

obj2 = Foo.get_instance()
print(obj2)
