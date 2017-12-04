# Author: wadeson
# date: 2017/12/4

import time


def foo():
    print("in the foor")
    bar()


def bar():
    print("in the bar")


foo()


def hello():
    start_time = time.time()
    print("hello world")
    time.sleep(4)
    stop_time = time.time()
    print("%s" % (stop_time - start_time))


def hello1(func):
    print(func)
    func()


hello1(hello)
