# 类和实例
std1 = { 'name': 'Michael', 'score': 98 }
std2 = { 'name': 'Bob', 'score': 81 }

class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


bart = Student('Bart Simpson', 59)

lisa = Student('Lisa Simpson', 87)

bart.print_score()
lisa.print_score()

print(lisa.name, lisa.get_grade())



# 访问限制
# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__
# 这样就确保了外部代码不能随意修改对象内部的状态，这样通过访问限制的保护，代码更加健壮。
# 外部代码要获取name和score怎么办？可以给Student类增加get_name和get_score方法
class PrivateStudent(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('Bad score')

    def print_score(self):
        print('%s %s' % (self.__name, self.__score))




# 继承
class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')

animal1 = Animal()
animal1.run()

dog = Dog()
dog.run()

# 多态
def run_twice(animal):
    animal.run()
    animal.run()

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')

run_twice(Tortoise())


# 获取对象信息
print(type(123))

print(type('abc') == type('123'))

import types

def fn():
    pass

type(fn) == types.FunctionType

type(abs) == types.BuiltinFunctionType

type(lambda x: x) == types.LambdaType

type((x for x in range(10))) == types.GeneratorType

# 总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。
isinstance(dog, Dog)

print('ABC'.capitalize())


# 实例属性属于各个实例所有，互不干扰；
# 类属性属于类所有，所有实例共享一个属性；
# 不要对实例属性和类属性使用相同的名字，否则将产生难以发现的错误。
class NewStd():
    count = 0

    def __init__(self, name):
        self.name = name
        NewStd.count += 1


newStd1 = NewStd('A')
newStd2 = NewStd('B')

print(NewStd.count)
