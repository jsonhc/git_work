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

langing()
