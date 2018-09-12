import sqlite3
import os

# 连接到SQLite数据库
# 数据库文件是test.db
# 如果文件不存在，会自动在当前目录创建:
# conn = sqlite3.connect('test.db')
# cursor = conn.cursor()
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
# print(cursor.rowcount)
# cursor.close()
# conn.commit()
# conn.close()

# 查询
# conn = sqlite3.connect('test.db')
# cursor = conn.cursor()
# cursor.execute('select * from user where id=?', ('1',))
# values = cursor.fetchall()
# print(values)
# cursor.close()
# conn.close()


db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()


def get_score_in(low, high):
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        cursor.execute(
            'select * from user where score >= ? and score <= ?', (low, high)
        )
        values = cursor.fetchall()
        values = sorted(values, key=lambda x: x[2])
        name = list(map(lambda x: x[1], values))
        print(values)
    except Exception as  e:
        print(e)
    finally:
        cursor.close()
        conn.close()
    return name


assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)