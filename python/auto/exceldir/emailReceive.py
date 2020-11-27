"""
自动接收邮件
"""

import poplib
from email.parser import Parser
from email.header import decode_header



def connect_email():
    """
    连接POP服务器
    :return:
    """
    user = 'longxiangfuct@sina.com'
    password = 'b2f6b9beca93e3b8'
    host = 'pop.sina.com'

    # 开始连接到服务器
    server = poplib.POP3(host)
    # 打开调试信息
    server.set_debuglevel(1)
    # 打印POP3服务器的欢迎文字
    print(server.getwelcome().decode('utf-8'))
    # 进行身份验证
    server.user(user)
    server.pass_(password)
    return server


def get_email_content(server):
    """
    获取email的内容
    :param server:
    :return:
    """
    # 返回邮件的总数目和占用服务器的空间大小
    email_num, email_size = server.stat()
    # 获取电子邮件信息,poplib.POP3不能获取未读邮件，要想获取，可以使用其他第三方库
    rsp, msglines, msgsiz = server.retr(email_num)  # 返回最新的邮件，参数为邮件索引
    # 拼接邮件内容并对内容进行GBK解码
    msg_content = b'\r\n'.join(msglines).decode('gbk')
    # 把邮件内容解析为Message内容
    msg = Parser().parsestr(msg_content)
    server.close()
    return msg


def guss_charset(msg):
    """
    获取内容编码
    :param msg:
    :return:
    """
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset



def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value


def parser_content(msg, indent=0):
    """
    解析内容
    :param msg:
    :param indent:
    :return:
    """
    if (msg.is_multipart()):  # 是否是多部分
        parts = msg.get_payload()  #获取内容体
        for n, part in enumerate(parts):
            parser_content(part, indent + 1)
    else:
        content_type = msg.get_content_type()
        if content_type == 'text/plain' or content_type == 'text/html':
            content = msg.get_payload(decode=True)
            charset = guss_charset(msg)  # 猜测编码格式
            if charset:
                content = content.decode(charset)
            else:
                charset = 'GBK'
                content = content.decode(charset)
            print(content)
        else:
            print(content_type)


def parser_subject(msg):
    subject = msg['Subject']
    value, charset = decode_header(subject)[0]
    if charset:
        value = value.decode(charset)
    return value

if __name__ == '__main__':
    server = connect_email()
    msg = get_email_content(server)
    print("------------总内容----------------")
    print(msg)
    subject = parser_subject(msg)
    print("------------主题----------------")
    print(subject)
    print("--------------内容--------------")
    parser_content(msg)
