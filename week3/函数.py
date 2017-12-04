# Author: wadeson
# date: 2017/12/4

def outer():
    x = 10

    def inner():
        print(x)

    return inner()


outer()
