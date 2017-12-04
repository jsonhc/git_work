# Author: wadeson
# date: 2017/12/4


def hello(*args):
    print(args)

hello(1, 2, 3, 4)
hello(*(1, 2, 3))
