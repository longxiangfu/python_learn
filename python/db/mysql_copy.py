"""
操作mysql:将老数据库中数据导入新数据库中
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
    # 连接老数据库
    old_connection = create_database_connection("112.126.98.236", "root", "xinfadi_236_com", "xfdsx2018_test")
    # 查询数据
    old = """select * from xfd_supplier_info"""
    old_infos = execute_read(old_connection, old)
    # 连接新数据库
    new_connection = create_database_connection("192.168.1.240", "root", "xfdsx@2019/PW", "xfdsx_supplier")
    # 插入新数据库
    cursor = new_connection.cursor()
    for info in old_infos:
        id = info[0]
        if id == None:
            id = 'null'
        supplier_no = info[1]
        if supplier_no == None:
            supplier_no = 'null'
        supplier_name = info[2]
        if supplier_name == None:
            supplier_name = 'null'
        contacts_name = info[3]
        if contacts_name == None:
            contacts_name = 'null'
        mobile = info[4]
        if mobile == None:
            mobile = 'null'
        telephone = info[5]
        if telephone == None:
            telephone = 'null'
        address = info[6]
        if address == None:
            address = 'null'
        wechat = info[7]
        if wechat == None:
            wechat = 'null'
        introduction = info[8]
        if introduction == None:
            introduction = 'null'
        pay_mode = info[9]
        if pay_mode == None:
            pay_mode = 'null'
        pay_account = info[10]
        if pay_account == None:
            pay_account = 'null'
        account_period = info[11]
        if account_period == None:
            account_period = 'null'
        category_id = info[12]
        if category_id == None:
            category_id = 'null'
        op_id = info[13]
        if op_id == None:
            op_id = 'null'
        supplier_type = info[14]
        if supplier_type == None:
            supplier_type = 'null'
        is_del = info[15]
        if is_del == None:
            is_del = 'null'
        downloadstatus = info[16]
        if downloadstatus == None:
            downloadstatus = 'null'
        downloadtime = info[17]
        if downloadtime == None:
            downloadtime = 'null'
        lastmsg = info[18]
        if lastmsg == None:
            lastmsg = 'null'
        created_at = info[19]
        if created_at == None:
            created_at = 'null'
        else:
            print(type(created_at))
        updated_at = info[20]
        if updated_at == None:
            updated_at = 'null'
        else:
            print(type(updated_at))
        buyer_id = info[21]
        if buyer_id == None:
            buyer_id = 'null'
        print(info)
        # 处理创建时间和修改时间
        new_insert = ""
        if created_at == 'null' and updated_at == 'null':
            new_insert = "insert into xfd_supplier_info" \
                     " values(%s, %s, '%s', '%s', %s,     %s, %s, %s, %s, %s,     %s, %s, %s, %s, %s,    %s, %s, %s, '%s', %s,     %s, %s,    %s, %s, %s, %s, %s, '%s')" % \
                     (id, supplier_no, supplier_name, contacts_name, mobile, telephone, address, wechat, introduction, pay_mode, pay_account, account_period, category_id, op_id, supplier_type, is_del, downloadstatus, downloadtime, lastmsg, created_at, updated_at, buyer_id, 'null', 'null', 'null', mobile, 123456, 'A')
        if created_at != 'null' and updated_at == 'null':
            new_insert = "insert into xfd_supplier_info" \
                     " values(%s, %s, '%s', '%s', %s,     %s, %s, %s, %s, %s,     %s, %s, %s, %s, %s,    %s, %s, %s, '%s', '%s',     %s, %s,    %s, %s, %s, %s, %s, '%s')" % \
                     (id, supplier_no, supplier_name, contacts_name, mobile, telephone, address, wechat, introduction, pay_mode, pay_account, account_period, category_id, op_id, supplier_type, is_del, downloadstatus, downloadtime, lastmsg, created_at, updated_at, buyer_id, 'null', 'null', 'null', mobile, 123456, 'A')
        if created_at == 'null' and updated_at != 'null':
            new_insert = "insert into xfd_supplier_info" \
                     " values(%s, %s, '%s', '%s', %s,     %s, %s, %s, %s, %s,     %s, %s, %s, %s, %s,    %s, %s, %s, '%s', %s,     '%s', %s,    %s, %s, %s, %s, %s, '%s')" % \
                     (id, supplier_no, supplier_name, contacts_name, mobile, telephone, address, wechat, introduction, pay_mode, pay_account, account_period, category_id, op_id, supplier_type, is_del, downloadstatus, downloadtime, lastmsg, created_at, updated_at, buyer_id, 'null', 'null', 'null', mobile, 123456, 'A')
        if created_at != 'null' and updated_at != 'null':
            new_insert = "insert into xfd_supplier_info" \
                     " values(%s, %s, '%s', '%s', %s,     %s, %s, %s, %s, %s,     %s, %s, %s, %s, %s,    %s, %s, %s, '%s', '%s',     '%s', %s,    %s, %s, %s, %s, %s, '%s')" % \
                     (id, supplier_no, supplier_name, contacts_name, mobile, telephone, address, wechat, introduction, pay_mode, pay_account, account_period, category_id, op_id, supplier_type, is_del, downloadstatus, downloadtime, lastmsg, created_at, updated_at, buyer_id, 'null', 'null', 'null', mobile, 123456, 'A')

        print(new_insert)
        try:
            cursor.execute(new_insert)
            new_connection.commit()
            print("Write operation executed successfully")
        except Error as e:
            print(f"The error '{e}' occcurred.")

        break;