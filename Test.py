print("hello\nworld")

print(r'\\\t\\\\')


print('''line1
line2
line3''')

print(None)

print(len('abadad'))

strA = b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
print(strA)

strB = b'ABC'.decode('ascii')
print(strB)


s1 = 72
s2 = 85

dis = s2 - s1

print('%.1f%%' % ((dis/s1)*100))

classmates = ['A', 'B', 'C']
print('List长度%d' % len(classmates))

print(classmates[-1])

classmates.append('D')
print(classmates)

classmates.insert(4, 'E')
print(classmates)

# 要删除list末尾的元素，用pop()方法：
classmates.pop()
print(classmates)

# 要删除指定位置的元素，用pop(i)方法
classmates.pop(0)
print(classmates)

classmates[1] = 'Z'
print(classmates)

s = ['python', 'java', ['asp', 'php'], 'scheme']

# tuple
t1 = ('E', 'F', 'G')
print(t1)
# 只有一个元素的tuple
t2 = ('H',)
print(t2)


# 条件判断
age = 5
print('your age is', age)
if age > 18:
    print('adult')
elif age > 6:
    print('teenager')
else:
    print('kid')


# birth = input('birth: ')
# if int(birth) < 2000:
#     print('00前')
# else:
#     print('00后')



height = 1.75
weight = 80.5

bmi = weight / (height * height)
print('BMI is',bmi)



# 循环
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0
for x in nums:
    sum = sum + x

print(sum)

total = 0
for y in list(range(100)):
    total += y

print(total)

# 字典
dic = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(dic['Michael'])

dic['Adam'] = 67
print(dic)

# 要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：
print('Thomas' in  dic)
# 二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：
print(dic.get('Thomas'))
print(dic.get('Thomas', -1))

# 删除一个key
dic.pop('Bob')
print(dic)

# 和list比较，dict有以下几个特点：
#
# 查找和插入的速度极快，不会随着key的增加而变慢；
# 需要占用大量的内存，内存浪费多。
# 而list相反：
#
# 查找和插入的时间随着元素的增加而增加；
# 占用空间小，浪费内存很少。
# 所以，dict是用空间来换取时间的一种方法。
#
# dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。
#
# 这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。
#
# 要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key


# set
st1 = set([1, 2, 3])
print(st1)
st1.add(4)
st1.add(4)
print(st1)
st1.remove(4)
print(st1)

st2 = set([2, 3,4])

print(st1 & st2)
print(st1 | st2)


# 函数
n1 = 121212
print(hex(n1))

# 空函数
def nop():
    pass

def sr_abs(x):
    if not isinstance(x, (int, float)):
        raise  TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

print(sr_abs(-100))

import  math

# 多个参数多个返回值
def sr_move(x, y, step, angle=0):
    nx = x + y * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx,ny

x, y = sr_move(100, 100, 60, math.pi / 6)
print(x, y)
# Python的函数返回多值其实就是返回一个tuple

def quadratic(a, b, c):
    x1 = (-b + math.sqrt(b*b-4*a*c)) / (2*a)
    x2 = (-b - math.sqrt(b*b-4*a*c)) / (2*a)
    return x1, x2

print(quadratic(2, 3, 1))

# 求x的n次方
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(3,2))

# 默认参数
# def power1(x, n=2):

# 可变参数
def calc(*nums):
    sum1 = 0
    for n in  nums:
        sum1 = sum1 + n * n
    return sum1

print(calc(1, 2, 3))

# Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：

# 关键字参数
def person(name, age, **kw):
    print('name', name, 'age', age, 'other', kw)

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('JackMa', 50, **extra)

# 命名关键字参数
def anotherPerson(name, age, *, city, job):
    print(name, age, city, job)

anotherPerson('Sara', 15, city='NewYork', job='Dancer')

# 参数组合
# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。



def product(*nums):
    if len(nums) == 0:
        raise TypeError('At least ONE parameter')

    total1 = 1
    for n in nums:
        total1 *= n
    return total1

# print(product())



# 在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。



# 切片
l = list(range(100))

print(l[:10])
# 倒数切片
print(l[-10:])

# 前10个数，每两个取一个：
print(l[:10:2])
# 所有数，每5个取一个：
print(l[::5])

# 原样复制一个
print(l[:])

# 字符串切片
str1 = 'ABCDEFG'
print(str1[1:-1:2])


# 迭代
# Python的for循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象上。
for ch in str1:
    print(ch)



# 默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()，如果要同时迭代key和value，可以用for k, v in d.items()。
d = {'a': 1, 'b': 2, 'c': 3}

# 判断一个对象是可迭代对象
from collections.abc import Iterable
print(isinstance(str1, Iterable))

for k in d.keys():
    print(k)

for v in d.values():
    print(v)

for k,v in d.items():
    print(k, v)

def findMinAndMax(l):
    if len(l) == 0:
        return (None, None)
    else:
        min = max = l[0]
        for i in l:
            if i < min:
                min = i
            if i > max:
                max = i
        return min, max


print(findMinAndMax([1, 3, 5]))



# 列表生成式
l1 = [n1 * n1 for n1 in range(1,11)]
print(l1)

l2 = [m + n for m in 'ABC' for n in 'XYZ']
print(l2)

l3 = [n2 * n2 for n2 in range(1,11) if n2 % 2 == 0]
print(l3)

import os
l4 = [d for d in os.listdir('.')]
print(l4)

d = {'x': 'A', 'y': 'B', 'z': 'C' }
l5 = [k + '=' + v for k, v in d.items()]
print(l5)

# 把一个list中所有的字符串变成小写：(大写upper)
L = ['Hello', 'World', 'IBM', 'Apple']
print([str2.lower() for str2 in L])



# 生成器(是可迭代对象)
g = (x * x for x in range(10))

for n in g:
    print(n)

# 斐波那契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n += 1
    print('done')

fib(10)

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

o = odd()
next(o)
next(o)
next(o)

def triangles():
    a = [1]
    while True:
        yield a
        if a == [1]: a = [1,1]
        else:
           a = [a[i]+a[i-1] for i in range(len(a)) if i!=0 ]
           a.insert(0, 1)
           a.append(1)


print(triangles())


# 迭代器
# 凡是可作用于for循环的对象都是Iterable类型；
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。