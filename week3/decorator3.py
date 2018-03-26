# Author: wadeson
# date: 2017/12/4


def dec_student(func):
    def dec(*args, **kwargs):
        print("the name in student is %s" % args[0])
        func(*args, **kwargs)
    return dec


@dec_student   # 将函数student进行装饰，将函数student的函数名作为dec_student函数的参数传入进去
def student(name, age):
    print(name, age)

student('wadeson', 25)  # 执行该行代码的步骤：1、dec_student(student)('wadeson', 25)    2、return dec---->dec('wadeson', 25)   
#  3、print("the name in student is %s" % args[0]) and 执行student('wadeson' ,25)
