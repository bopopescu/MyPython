# 高阶函数
# map/reduce
def f(x):
    return x * x

l1 = [1, 2, 3, 4, 5, 6]

r = map(f, l1)
print(list(r))

print(list(map(str, l1)))

from functools import reduce
def add(x, y):
    return x + y

print(reduce(add, [1, 3, 5, 7, 9]))

print(sum([1, 3, 5, 7, 9]))



digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return digits[s]
    return reduce(fn, map(char2num, s))

print(str2int('12313'))


name1 = ['adam', 'LISA', 'barT']

def normalize(name):
    def fun(s):
        return s[0].upper() + s[1:].lower()
    return list(map(fun, name))

print(normalize(name1))


def prod(L):
    def multiply(x, y):
        return x * y
    return reduce(multiply, L)

print(prod([1,5,10]))



# filter
def isOdd(n):
    return n % 2 == 1

print(list(filter(isOdd, [1, 2, 3, 4, 5, 6, 7])))


def deleteEmpty(s):
    newS = ''
    for ch in s:
        if ch != ' ':
            newS += ch
    return newS

print(deleteEmpty('Hello World'))


def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


for n in  primes():
    if n < 100:
        print(n)
    else:
        break

def is_palindrome(n):
    k = str(n)
    return k == k[::-1]

output = list(filter(is_palindrome, range(1,1000)))
# print(output)



# sorted排序算法
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]

def by_score(t):
    return t[1]*-1

L1 = sorted(L, key=by_name)
# L2 = sorted(L1, key=by_score)

print(L1)
# print(L2)


# 返回函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1, 3, 5, 7)
print(f())

# 调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1==f2)



# 闭包(Closure)
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs

f1, f2, f3 = count()

# 返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9
print(f1(), f2(), f3())

# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

# 如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：
def another_count():
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs

f1, f2, f3 = another_count()
print(f1(), f2(), f3())

def createCounter():
    a = 0
    def counter():
        nonlocal a
        a += 1
        return a
    return counter

# 匿名函数
# 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
# 匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数
l = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(l)

# 把匿名函数作为返回值返回
def build(x, y):
    return lambda : x * x + y * y

print(build(3,4)())

f = lambda x : x % 2 == 1
L = list(filter(f, range(1, 20)))

print(L)



# 装饰器
def now():
    print('time')

f = now

print(f.__name__)
print(now.__name__)

import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('call %s():' % func.__name__)
        return func(*args, **kwargs)
    return wrapper


# 偏函数
int2 = functools.partial(int, base=2)
print(int2('01010001'))

# 会把10作为*args的一部分自动加到左边
max2 = functools.partial(max, 10)
print(max2(5, 6, 7))
# 相当于
# args = (10, 5, 6, 7)
# max(*args)


