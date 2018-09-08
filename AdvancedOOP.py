class Student(object):
    pass

# 动态给实例绑定一个属性
s1 = Student()
s1.name = 'Mic'
print(s1.name)

# 给实例绑定一个方法
def set_age(self, age):
    self.age = age

from types import MethodType
s1.set_age = MethodType(set_age, s1)
s1.set_age(25)
print(s1.age)


# 给一个实例绑定的方法，对另一个实例是不起作用的：
s2 = Student()
# s2.set_age(25)

# 为了给所有实例都绑定方法，可以给class绑定方法：
def set_score(self, score):
    self.score = score

Student.set_score = set_score

# 给class绑定方法后，所有实例均可调用：
s1.set_score(100)
print(s1.score)

s2.set_score(98)
print(s2.score)


# __slots__
# 用tuple定义允许绑定的属性名称
# __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
class LimitedStudent(object):
    __slots__ = ('name', 'age')


# @property，我们在对实例属性操作的时候，就知道该属性很可能不是直接暴露的，而是通过getter和setter方法来实现的。
class NewStudent(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise  ValueError('score must be an integer')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100')
        self._score = value

# 只定义getter方法，不定义setter方法就是一个只读属性
class SomeObj(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth


class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height



# 多重继承
class Animal(object):
    pass

# 大类:
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

# 各种动物:
class Dog(Mammal):
    pass

class Bat(Mammal):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass

# 加上Runnable和Flyable的功能
class Runnable(object):
    def run(self):
        print('Running...')

class Flyable(object):
    def fly(self):
        print('Flying...')

# 通过多重继承，一个子类就可以同时获得多个父类的所有功能。
class OneKindDog(Mammal, Runnable):
    pass



# MixIn
# MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系



# 定制类



# 枚举类
from enum import Enum,unique
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

print(Month.Jan)

# value属性则是自动赋给成员的int常量，默认从1开始计数。
for name, member in Month.__members__.items():
    print(name, '->', member, ',', member.value)

# 精确地控制枚举类型
# Sun的value被设定为0
# @unique装饰器可以帮助我们检查保证没有重复值。
@unique
class WeekDay(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

for name, day in WeekDay.__members__.items():
    print(name, '->', day, ',', day.value)


# 元类(metaclass)

