# Author: wadeson
# date: 2017/12/5


class F:
    def f1(self):
        print("F.f1")

    def f2(self):
        print("F.f2")


class S(F):
    def s1(self):
        print("S.s1")

    def f2(self):              # 如果自己的方法和父类重名，那么使用的是自己的方法，而丢弃继承下来的父类的方法
        print("S.f2")
        super().f2()
        super(S, self).f2()
        F.f2(self)


obj = S()
obj.s1()
obj.f2()
