# Author: wadeson
# date: 2017/12/3

a = 30
def outer():
    a = 10
    def inner():
        nonlocal a
        print(a)
        a = 20
        print(a)
    inner()
    print(a)

outer()
print(a)