# Author: wadeson
# date: 2017/12/4


def extend_hello(func):
    def dec():
        print("decorate for hello")
        func()
    return dec


@extend_hello
def hello():
    print("hello")

hello()
