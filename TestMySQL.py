import mysql.connector

conn = mysql.connector.connect(user='root', password='1', database='test')
cursor = conn.cursor()

# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# cursor.execute('insert into user (id, name) values (%s, %s)', ['3', 'Michael3'])

# 数据库变化
# print(cursor.rowcount)

# conn.commit()
# conn.close()

cursor.execute('select * from user where id = %s', ('3',))
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()

