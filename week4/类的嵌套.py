# Author: wadeson
# date: 2017/12/25


class F1:
    def __init__(self):
        self.name = "hello"


class F2:
    def __init__(self, a):
        self.ff = a


class F3:
    def __init__(self, b):
        self.dd = b

f1 = F1()     # f1.name
f2 = F2(f1)    # f2.ff = f1, f2.ff.nam
f3 = F3(f2)    # f3.dd = f2, f2.ff = f1, f3.dd.ff.name
print(f3.dd.ff.name)
