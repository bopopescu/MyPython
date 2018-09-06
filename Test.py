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
