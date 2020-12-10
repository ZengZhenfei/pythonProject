
import sqlite3
conn = sqlite3.connect("test.db") #打开或创建数据库文件
print("成功打开数据库")
c = conn.cursor() #获取游标


# sql = '''
#     update table company
#         (id int not null primary key autoincrement,
#         name text not null,
#         age int not null,
#         address char(50),
#         salary real)
# '''
# c.execute(sql) #执行sql
# conn.commit() #提交数据库操作
# conn.close() #关闭数据库操作
# print("建表成功")

# sql1 = '''
#     insert into company (id,name,age,address,salary)
#     values(001,'张三',25,'广州市',10000)
# '''
# sql2 = '''
#     insert into company (id,name,age,address,salary)
#     values(002,'李四',22,'广州市天河区',10000)
# '''
# c.execute(sql1) #执行sql
# c.execute(sql2) #执行sql
# conn.commit() #提交数据库操作
# conn.close() #关闭数据库操作
# print("插入数据成功")

sql = '''
    select * from company
'''
cursor = c.execute(sql) #执行sql
for row in cursor:
    print('id=',row[0])
    print('name=' , row[1])
    print('age=' , row[2])
    print('salary=' , row[4])
conn.commit() #提交数据库操作
conn.close() #关闭数据库操作
print("查询数据成功")