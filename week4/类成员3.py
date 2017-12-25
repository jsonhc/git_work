# Author: wadeson
# date: 2017/12/22


class Foo:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.n = 123

    def __getitem__(self, item):
        if type(item) == slice:
            print(type(item))
        else:
            print("OK")

    def __setitem__(self, key, value):
        print(key, value)

    def __delitem__(self, key):
        print(key)

l = Foo('hello', 13)
l[3]              # 调用着希望内部作索引处理
l[1:4:2]          # 调用着希望内部作切片处理
