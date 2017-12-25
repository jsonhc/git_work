# Author: wadeson
# date: 2017/12/25


class Teacher:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.salary = 1000       # 定义默认的初始的老师的工资


class Course:
    def __init__(self, name, cost, teacher):
        self.name = name
        self.teacher = teacher
        self.cost = cost

    def course_up(self):       # 上课，上课一次，老师的salary增加一次值
        self.teacher.salary = self.teacher.salary + self.cost

t1 = Teacher('t1', 21)
t2 = Teacher('t2', 22)
t3 = Teacher('t3', 23)

c1 = Course('math', 1, t1)
print(c1.teacher.name)
print(c1.teacher.salary)
c1.course_up()
print(c1.teacher.salary)
