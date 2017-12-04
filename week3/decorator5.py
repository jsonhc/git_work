def auth(auth_type):
    print("auth_type is %s" % auth_type)

    def outer(func):
        def inner(*args, **kwargs):
            func(*args, **kwargs)
        return inner
    return outer


@auth("file")
def langing():
    print("welcome to land")

langing()
