# Author: wadeson
# date: 2017/12/4


def extend_hello(func):
    def dec():
        print("decorate for hello")
        func()
    return dec


@extend_hello     # 为函数hello进行装饰，也就是将函数名hello将参数传入到extend_hello中
def hello():
    print("hello")

hello()   # 执行该行代码的步骤：1、extend_hello(hello)()    2、return dec------>dec()  3、print("decorate for hello")    hello()
