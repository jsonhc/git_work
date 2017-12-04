# Author: wadeson
# date: 2017/12/4


def dec_student(func):
    def dec(*args, **kwargs):
        print("the name in student is %s" % args[0])
        func(*args, **kwargs)
    return dec


@dec_student
def student(name, age):
    print(name, age)

student('wadeson', 25)
