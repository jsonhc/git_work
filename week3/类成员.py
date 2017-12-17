# Author: wadeson
# date: 2017/12/13


class Foo:
    country = "china"     # 静态字段,保存在类中，也可以被对象调用

    def __init__(self, name):
        self.name = name       # 普通字段，保存在对象中，类不可以直接调用，如果被类调用需要先创建对象


# obj = Foo("hubei")
# print(obj.country)            # china
# print(Foo.country)            # china


class Bar:
    def __init__(self):
        pass

    def min(self):
        print("bar")

    @staticmethod                  # 定义静态的方法的标志，加上该装饰器，那么定义的方法就是静态方法，静态方法也可以带有参数，但不会有self参数
    def sta():
        print("static")

    @staticmethod                  # 静态方法可以被类调用，也可以被对象调用，静态方法类似于一个函数，静态方法保存在类中
    def stat(x, y):
        return x+y

# Bar.sta()               # 直接类调用，static
# obj = Bar()
# obj.sta()               # 对象调用，static
# print(Bar.stat(2, 3))               # 5


class Sugar:
    def bar(self):
        print("bar")

    @classmethod                # 类方法就是添加了此装饰器，并且定义的方法默认有cls这个参数，这个参数就是类名，类方法保存在类中
    def per(cls):
        print("123")

# Sugar.per()          # 直接类进行调用，123
# obj = Sugar()
# obj.per()          # 对象调用，123


class Pro:
    @property          # 加上该装饰器就可以将普通方法的调用变为普通字段的调用
    def per(self):
        return 666

    @per.setter
    def per(self, val):
        print(val)

    @per.deleter
    def per(self):
        return 555

    @per.getter
    def per(self):
        return 777


obj = Pro()
obj.per = 123
print(obj.per)
del obj.per
print(obj.per)
