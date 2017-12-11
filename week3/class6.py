# Author: wadeson
# date: 2017/12/11


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title(), "is now sitting")

    def roll_over(self):
        print(self.name.title(), "rolled over")


dog = Dog("taidi", "4")
dog.sit()


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.name)

    def open_restaurant(self):
        print("this restaurant %s is open" % self.name)

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, num):
        self.number_served = self.number_served + num


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        pass


class User:
    def __init__(self, first_name, last_name):
        self.name = "%s %s" % (first_name, last_name)
        self.login_attemps = 0

    def describe_user(self):
        print(self.name)

    def greet_user(self):
        print("hello %s" % self.name)

    def read_login_attemps(self):
        print(self.login_attemps)

    def increment_login_attemps(self):
        self.login_attemps = self.login_attemps + 1

    def reset_login_attemps(self):
        self.login_attemps = 0

u = User("wadeson", "huang")
u.describe_user()


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def descriptive_name(self):
        long_name = "%s %s %s" % (self.year, self.make, self.model)
        return long_name

    def read_odometer(self):
        print(self.odometer)

    def update_odometer(self, mileage):
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print("invalid operation")

    def increment_odometer(self, miles):
        self.odometer = self.odometer + miles


class Battery:
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print(self.battery_size)

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        print(range)


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()                   # 将电池的信息封装成一个类进行调用该类中的方法


my_car = Car('audi', "a4", 2016)
print(my_car.descriptive_name())
my_car.read_odometer()
my_car.update_odometer(100)
my_car.read_odometer()

my_tesla = ElectricCar("tesla", "model s", 2017)
print(my_tesla.descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()













