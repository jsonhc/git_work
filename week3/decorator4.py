# Author: wadeson
# date: 2017/12/4

_username = "wadeson"
_passwd = "redhat"


def auth(func):
    def intrapper(*args, **kwargs):
        username = input("please input your name: ")
        passwd = input("please input your passwd: ")
        if username == _username and passwd == _passwd:
            func(*args, **kwargs)
        else:
            print("username or password is wrong!")
    return intrapper


@auth
def langing():
    print("welcome to land")

langing()  # 将langing作为参数传入到auth中，auth(langing)()  ---->return intrapper，然后执行intrapper函数，由于该函数可以传入任意参数，这里没有
# 参数所以继续执行，函数intrapper函数中执行的func函数，实际执行的就是langing函数
