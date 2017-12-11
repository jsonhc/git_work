# Author: wadeson
# date: 2017/12/7


class F:
    def a(self):
        print("F.a")


class F1(F):
    def a1(self):
        print("F1.a")


class F2(F):
    def a(self):
        print("F2.a")


class S(F2, F1):
    def a1(self):
        print("S.a")


obj = S()
obj.a()
