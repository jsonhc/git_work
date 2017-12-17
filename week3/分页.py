# Author: wadeson
# date: 2017/12/17


L = []
for i in range(1000):
    L.append(i)
#
#
# while True:
#     page = input("please input your page: ")
#     page = int(page)
#     # 1 0,10； 2 1，20
#     page_start = (page-1) * 10
#     page_end = page * 10
#     print(L[page_start:page_end])


class Page:
    def __init__(self, p):
        self.page = p

    @property
    def start(self):
        return (self.page-1) * 10

    @property
    def end(self):
        return self.page * 10

while True:
    page = input("please input your page: ")
    try:
        page = int(page)
    except Exception as e:
        print("invalid options")
        page = 1
    obj = Page(page)
    print(L[obj.start:obj.end])
