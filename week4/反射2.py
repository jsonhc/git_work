# Author: wadeson
# date: 2017/12/24


# class Foo:
#     stat = 123
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# ret = getattr(Foo, "stat")
# print(ret)

import fanshe

# r1 = fanshe.NAME
# print(r1)
# r2 = fanshe.test()
# print(r2)
# r3 = getattr(fanshe, "NAME")
# print(r3)
# r4 = getattr(fanshe, "test")
# print(r4)
# print(r4())
# cls = getattr(fanshe, "Foo")
# obj = cls('hello')
# print(obj.name)
inp = input("请输入要查看的URL：")
if hasattr(fanshe, inp):
    ret = getattr(fanshe, inp)
    print(ret())
else:
    print(404)
