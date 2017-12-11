# Author: wadeson
# date: 2017/12/4


def g():
    print("-----------------start--------------------")
    m = yield 12
    print(m)
    d = yield
    print(d)
    print("----------------stop-----------------------")


c = g()
d = c.__next__()
print(d)
c.send('wadeson')

