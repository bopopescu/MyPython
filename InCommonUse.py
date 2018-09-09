# 获取当前日期和时间
from datetime import datetime, timedelta, timezone
now = datetime.now()
print(now)
print(type(now))

# 获取指定日期和时间
dt = datetime(2015, 4, 19, 12, 20)
print(dt)

# datetime转换为timestamp
print(dt.timestamp())
# timestamp是一个浮点数，它没有时区的概念，而datetime是有时区的

# timestamp也可以直接被转换到UTC标准时区的时间
t = 1429417200.0
# 本地时间
print(datetime.fromtimestamp(t))
# UTC时间
print(datetime.utcfromtimestamp(t))


# str转换为datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

# datetime转换为str
print(now.strftime('%a, %b %d %H:%M'))
print(now.strftime('%Y-%m-%d %H:%M:%S'))


# datetime加减
print(now)
print(now + timedelta(days=1))
print(now + timedelta(hours=10))


# 本地时间转换为UTC时间
# 创建时区UTC+8:00
tz_uzc_8 = timezone(timedelta(hours=8))
# 强制设置为UTC+8:00
dt = now.replace(tzinfo=tz_uzc_8)
print(dt)


# 时区转换
# 拿到UTC时间，并强制设置时区为UTC+0:00:
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)

bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)

tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)

tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)




# collections
# collections是Python内建的一个集合模块，提供了许多有用的集合类。

# namedtuple
from collections import namedtuple
# Point对象是tuple的一种子类
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)

# 用坐标和半径表示一个圆
Cicle = namedtuple('Circle', ['x', 'y', 'r'])


# deque
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)


# defaultdict
# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：
from collections import defaultdict
dd = defaultdict(lambda : 'N/A')
dd['key1'] = 'abc'

print(dd['key1'])
print(dd['key2'])


# OrderedDict
from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
# dict的Key是无序的
print(d)

od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# OrderedDict的Key是有序的
print(od)

# OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：
new_od = OrderedDict()
new_od['z'] = 1
new_od['y'] = 2
new_od['x'] = 3
print(new_od)

# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key：
class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)




# Counter
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] += 1


print(c)