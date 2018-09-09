# 文件读写
# 标示符'r'表示读，这样，我们就成功地打开了一个文件。
# 如果文件不存在，open()函数就会抛出一个IOError的错误，并且给出错误码和详细的信息告诉你文件不存在：

path =  '/Users/longrise/Desktop/培训报名接口.rtf'

# try:
#     f = open(path, 'r')
#     print(f.read())
# finally:
#     if f:
#         f.close()

# 简洁写法
# 引入with语句来自动调用close()
# 如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便
with open(path, 'r') as f:
    # print(f.read())
    for line in f.readlines():
        # 把末尾的'\n'删掉
        print(line.strip())



# file-like Object
# StringIO就是在内存中创建的file-like Object，常用作临时缓冲。

# 二进制文件
image_path = '/Users/longrise/Desktop/852CF1D02622B4D68AD1B8FFBE269667.png'
img1 = open(image_path , 'rb')
# print(img1.read())


# 字符编码
# 要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数
# f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')
# f.read()


# 写文件
# 写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件
# f = open(path, 'w')
# f.write('Hello')
# 追加写入
# f.write('asd', 'a')
# f.close()

# with open(path, 'w') as f:
#     f.write('World')



# StringIO
# 数据读写不一定是文件，也可以在内存中读写。
from io import StringIO
f = StringIO()
f.write('Hello')
f.write(' ')
f.write('World')

# getvalue()方法用于获得写入后的str
print(f.getvalue())

# 读取StringIO
f = StringIO('Hello!\nHi!\nWorld!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())



# BytesIO
# StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。
from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))

print(f.getvalue())

# 读取
# f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
# f.read()




# 操作文件和目录
import os
print('CZXT %s' % os.name)
# uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的
print(os.uname())

# 环境变量
print(os.environ)
print(os.environ.get('_system_arch'))
print(os.environ.get('x', 'default'))

# 操作目录
abs_path = os.path.abspath('.')
print(abs_path)

new_path =  os.path.join(abs_path, 'testdir')
# os.mkdir(new_path)
# os.rmdir(new_path)

allPath = '/Users/longrise/Desktop/Python/testdir/pxbmjk.rtf'
print(os.path.split(allPath))
print(os.path.splitext(allPath))

# 操作文件
# os.rename('/path/to/file.rtf', '/path/to/file.txt')
# os.remove('/path/to/file.txt')

# 过滤文件
print([x for x in os.listdir('.') if os.path.isdir(x)])
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])




# 变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，
# 在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思
# 序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
# 反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。
import pickle
d = dict(name='Bob', age=20, score=88)
# pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。a
a_bytes = pickle.dumps(d)

# 或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：
# f = open('dump.txt', 'wb')
# pickle.dump(d, f)
# f.close()

# 当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象
print(pickle.loads(a_bytes))

# 也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象
# f = open('dump.txt', 'wb')
# d = pickle.load(f)
# f.close()
# print(d)




# JSON
import json
json_str = json.dumps(d)
# dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object。
# 要把JSON反序列化为Python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化：
print('JSON:%s' % json.loads(json_str))


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def std2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        "score": std.score
    }

def dict2std(d):
    return Student(d['name'], d['age'], d['score'])

# 序列化为JSON
s = Student('Bob', 20, 88)
print(json.dumps(s, default=std2dict))

# 反序列化为实例对象
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2std))

# 把任意class的实例变为dict：
print(json.dumps(s, default=lambda obj: obj.__dict__))


