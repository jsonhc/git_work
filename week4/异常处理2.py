# Author: wadeson
# date: 2017/12/24


# class HelloError(Exception):
#     def __init__(self, msg):
#         self.msg = msg
#
#     def __str__(self):
#         return self.msg
#
# obj = HelloError('hello')
# print(obj)         # 打印obj对象，就会调用对象的__str__()方法，获取返回值
#
# try:
#     raise HelloError('出错了')        # 创建了一个HelloError类的对象
# except HelloError as e:
#     print(e)           # 打印对象e，就是调用了__str__()方法

print(23)
assert 1 == 1
print(234)
