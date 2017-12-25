# Author: wadeson
# date: 2017/12/22


class Foo:
    def __init__(self, name):
        self.name = name

    def __iter__(self):
        return iter([11, 22, 33, 44])


li = Foo('hello')

# 如果类中有__iter__这个方法，那么所创建的对象就是可迭代对象
# 1、执行li对象的类Foo类中的__iter__方法，并获取其返回值
# 2、循环上一步中的返回值
for item in li:
    print(item)
