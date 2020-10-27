"""
操作mysql
"""

import mysql.connector
from mysql.connector import Error


# 连接mysql
def create_connection(host_name, user_name, user_password):
    mysqlconnection = None
    try:
        mysqlconnection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print('Connection to MYSQL successful')
    except Error as e:
        print(f"The error '{e}' occurred.")
    return mysqlconnection


# 创建数据库
def create_database(mysqlconnection, query):
    cursor = mysqlconnection.cursor()
    try:
        cursor.execute(query)
        print("Database create succesfully")
    except Error as e:
        print("The error {0} occurred.".format(e))


# 连接到具体的数据库
def create_database_connection(host_name, user_name, user_password, db_name):
    mysqlconnection = None
    try:
        mysqlconnection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print('Connection to MYSQL DB successful')
    except Error as e:
        print(f"The error '{e}' occurred.")
    return mysqlconnection


# 执行写操作
def execute_write(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Write operation executed successfully")
    except Error as e:
        print(f"The error '{e}' occcurred.")


# 执行读操作
def execute_read(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        print("Read operation executed successfully")
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred.")


if __name__ == "__main__":
    # 创建连接
    # connection = create_connection("localhost", "root", "123456")
    # # 创建数据库
    # create_database_query = "create database reader"
    # create_database(connection, create_database_query)
    # 连接数据库
    connection = create_database_connection("localhost", "root", "123456", "reader")
    # 创建表
    create_users_table = """create table if not exists users(
        id int auto_increment,
        name text not null,
        age int,
        gender text,
        primary key(id)
    );
    """
    # execute_write(connection, create_users_table)
    # 插入数据
    insert_users_table = """
        insert into users(name, age, gender)
        values
        ("zhangsan", 25, "male"),
        ("lisi", 28, "female"),
        ("wangwu", 29, "male")
    """
    # execute_write(connection, insert_users_table)
    # 查询
    select_users = "select * from users"
    users = execute_read(connection, select_users)
    for user in users:
        print(user)
