"""
操作sqlite数据库
"""

import sqlite3

# 创建连接
conn = sqlite3.connect("./sm_app.sqlite")
# 创建游标
cur = conn.cursor()
# create_users_table = """create table if not exists users(
#     id integer primary key autoincrement,
#     name text not null,
#     age integer,
#     gender text
# );
# """
# 执行sql
# cur.execute(create_users_table)

# insert_users_table = """
#     insert into users(name, age, gender)
#     values
#     ("zhangsan", 25, "male"),
#     ("lisi", 28, "female"),
#     ("wangwu", 29, "male")
# """
# cur.execute(insert_users_table)
# conn.commit()

select_users = """select * from users"""
cur.execute(select_users)
result = cur.fetchall()
print(result)
# 关闭游标和连接
cur.close()
conn.close()
