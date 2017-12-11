# Author: wadeson
# date: 2017/12/8


class Baserequest:
    def __init__(self):
        print("Baserequest")


class Requesthandler(Baserequest):
    def __init__(self):
        print("Request")
        # super(Requesthandler, self).__init__()
        # Baserequest.__init__(self)
        super().__init__()

    def server_for(self):
        print("Request")
        self.Min()

    def Min(self):
        print("Request.Min")


class Minx:
    def Min(self):
        print("Min")


class Sun(Minx, Requesthandler):
    pass

obj = Sun()
obj.server_for()
