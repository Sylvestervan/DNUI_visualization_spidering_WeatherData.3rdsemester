#求圆的面积
#TODO#用def
from math import pi as PI

def circle(r):
    return PI * (r ** 2)

r = int(input("You are requested to send an integer.\n"))
R = circle(r)

print(R)

#TODO#写一个lambda表达式，传递一个参数判断这个参数的2次方+1是否能被5整除，如果能被5整除返回True，反之False。

Is_divisible_by_5 = lambda x: (x**2 + 1) % 5 == 0
print(Is_divisible_by_5(3))

#TODO#定义一个学生Student类。有下面的实例方法：获取学生的姓名：get_name（）获取学生的年龄：get_age（）定义好类以后，实例化一个同学对象，并实例方法打印输出其姓名和年龄信息。
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


student = Student("Van Dijk", 120)

print("姓名:", student.get_name())
print("年龄:", student.get_age())

#TODO#
class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def __str__(self):
        return f'Student Age: {self.__age}'

student = Student('Alice', 20)
print(student)
print(student.get_name())
student.set_name('Bob')
print(student.get_name())