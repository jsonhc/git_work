# Author: wadeson
# date: 2017/12/25


class Foo:
    def __init__(self):
        self.name = "hello"

    def show(self):
        print("hello")

# obj = Foo()     # obj是对象，也是Foo类的实例，创建obj这个对象的过程，也是Foo类的实例化，obj是Foo类的对象，也是Foo类的一个实例
# # 单例用于使用同一份实例，或者同一个对象，对象和实例只创建一次

v = None
while True:
    if v:
        v.show()
    else:
        v = Foo()
        v.show()
