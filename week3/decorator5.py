def auth(auth_type):
    print("auth_type is %s" % auth_type)

    def outer(func):
        def inner(*args, **kwargs):
            func(*args, **kwargs)
        return inner
    return outer


@auth("file")     # auth("file")(langding)()或者auth("file")(langding)(*args, **kwargs)
def langing():
    print("welcome to land")

langing()
'''
auth_type is file
welcome to land
'''