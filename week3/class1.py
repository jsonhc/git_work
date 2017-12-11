# Author: wadeson
# date: 2017/12/4


class Person:
    def __init__(self, name):     # 构造函数__init__函数，当类赋给一个对象或者一个实例时，该函数已经加载了
        self.name = name

    def show(self):
        print(self.name)


p = Person("wadeson")     # p就是一个对象或者一个实例，p也是类中的self,类名加括号会自动执行构造方法
print(p)      # <__main__.Person object at 0x000001B370E0B208>
p.age = 25        # 也是self.age = 25(self就是不同的对象的引用)
print(p.age)
p.show()

p1 = Person("jsonhc")
p1.age = 16
print(p1)          # <__main__.Person object at 0x0000025D9F91B9E8>
print(p1.age)
p1.show()
