# Author: wadeson
# date: 2017/12/4


def hello(**kwargs):
    print(kwargs)
    print(kwargs["name"])

hello(name="wadeson")
hello(**{"name": "wadeson"})


def func4(name, **kwargs):
    print(name)
    print(kwargs)

func4('huang')

L = ['1', '2', '3', '4', '5']
print(','.join(L))
