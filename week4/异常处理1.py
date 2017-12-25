# Author: wadeson
# date: 2017/12/24


def db():
    # return True
    return False


def index():
    try:
        result = db()
        if result is False:
            raise Exception("数据库处理操作错误")
    except Exception as e:
        print(e)

index()
