def auth(auth_type):
    print("auth_type is %s" % auth_type)

    def outer(func):
        def inner(*args, **kwargs):
            func(*args, **kwargs)
        return inner
    return outer


@auth("file")     # auth("file")(langing)()或者auth("file")(langing)(*args, **kwargs)
def langing():
    print("welcome to land")

langing()  # 执行该代码的步骤：1、auth('file')(langing)()    2、return outer---->outer(langing)(),由于outer函数传入的参数就是参数名
# 3、outer(langing)--->return inner---->inner()  4、最后再执行langing函数
'''
auth_type is file
welcome to land
'''
