# Author: wadeson
# date: 2017/12/9


class Person:
    def __init__(self, name, age, gender, fight):
        self.name = name
        self.age = age
        self.gender = gender
        self.fight = fight

    def grassland(self):
        self.fight = self.fight - 200                # 草丛战斗，战斗力减少200

    def practice(self):
        self.fight = self.fight + 100                # 自我修改，战斗力增加100

    def incest(self):
        self.fight = self.fight - 500                # 多人战斗，战斗力消耗500

    def detail(self):
        temp = "姓名: %s, 年龄: %s, 性别: %s, 战斗力: %s" % (self.name, self.age, self.gender, self.fight)
        print(temp)

sun = Person("wadeson", 25, "男", "1000")     # 创建sun这个角色
sun.detail()
