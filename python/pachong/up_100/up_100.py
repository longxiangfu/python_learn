"""
bilibili的up100主视频解析
"""
import requests
import os
import json
import traceback
import time

from threading import Thread
from concurrent.futures import ThreadPoolExecutor
from queue import Queue

from requests.adapters import HTTPAdapter

dir_path = 'up_100'
executor = ThreadPoolExecutor(10)
queue = Queue()
# 为了防止反爬，可以设置ip池

def get_http_session(pool_connections=2, pool_maxsixe=10, max_retries=3):
    """
    创建http连接池
    :param pool_connections: 连接池大小
    :param pool_maxsixe: 连接池最大连接数
    :param max_retries: 最大重试次数
    :return: session
    """
    # 获取session
    session = requests.session()
    # 获取适配器
    adapter = HTTPAdapter(
        pool_connections=pool_connections,
        pool_maxsize=pool_maxsixe,
        max_retries=max_retries
    )
    # session安装适配器
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session


def save_file(filepath, content):
    """
    保存文件
    :param filepath:
    :param content:
    :return:
    """
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def make_dir(name):
    """
    创建目录
    :param name:
    :return:
    """
    up_dir = os.path.join(dir_path, name)
    if not os.path.exists(up_dir):
        os.makedirs(up_dir)
    return up_dir

def log(content, level, filepath):
    """
    日志记录
    :param content:
    :param level:
    :param filepath:
    :return:
    """
    with open(filepath, 'a', encoding='utf-8') as f:
        if level == 'error':
            f.write(content)
        if level == 'fail':
            f.write(content)

def read_json(filepath):
    """
    读取json文件
    :param filepath:
    :return:
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        res = f.read()
    return json.loads(res)  # 将json字符串转成字典列表


def get_up_base_info(name, uid):
    try:
        url = f'https://api.bilibili.com/x/space/arc/search?mid={uid}&pn=1&ps=25&order=click&jsonp=jsonp'
        r = get_http_session().get(url, timeout=100)
        if r.status_code == 200:
            up_dir = make_dir(name)
            filepath = os.path.join(up_dir, f'{uid}_base_info.json')
            content = json.dumps(r.json(), indent=4, ensure_ascii=False)  # json.dumps()：将结果格式化为json标准格式
            save_file(filepath, content)
            print(f'{name} up主信息保存成功')
            global queue
            queue.put((name, uid, filepath))
        else:
            fail_str = f'name: [{name}], uid: [{uid}], url: [{url}], reason: [{r.reason}]'
            log(fail_str, 'fail', 'base_fail.log')

    except Exception as e:
        log(traceback.format_exc(), 'error', 'base_error.log')  # traceback.format_exc()：打印出详细错误信息
        error_str = f'name: [{name}], uid: [{uid}]'
        log(error_str, 'error', 'base_error.log')


def get_video_barrage(d, name, aid):
    """
    获取某个视频的弹幕信息
    :param d:
    :param name:
    :param aid:
    :return:
    """
    cid = d['cid']  # 弹幕id
    barrage_url = f'https://api.bilibili.com/x/v1/dm/list.so?oid={cid}'
    r = get_http_session().get(barrage_url, timeout=10)

    # 弹幕->xml
    uid_dir_path = os.path.join(dir_path, name)
    if not os.path.exists(uid_dir_path):
        os.makedirs(uid_dir_path)
    barrage_path = os.path.join(uid_dir_path, f'barrage_{aid}.xml')
    r.encoding = 'utf-8'
    content = r.text
    save_file(barrage_path, content)
    print(f'video id:{aid} barrage save success')


def get_video_comment_info(aid, name):
    """
    获取视频评论信息
    :param aid:
    :param name:
    :return:
    """
    comment_url = f'https://api.bilibili.com/x/v2/reply?jsonp=jsonp&type=1&oid={aid}&sort=1'
    r = get_http_session().get(comment_url, timeout=10)
    if r.status_code == 200:
        uid_dir_path = os.path.join(dir_path, name)
        if not os.path.exists(uid_dir_path):
            os.makedirs(uid_dir_path)
        comment_path = os.path.join(uid_dir_path, f'comment_{aid}.json')
        rjson = r.json()  # 返回响应的json，这里是字典类型
        # dumps 将dict->json
        content = json.dumps(rjson, indent=4, ensure_ascii=False)
        save_file(comment_path, content)
        print(f'video id:{aid} comment save success')


def gt_up_video_info(name, uid, filepath):
    '''
    获取视频相关信息
    :param name:
    :param uid:
    :param filepath:
    :return:
    '''
    res = read_json(filepath)
    vlist = res['data']['list']['vlist']  # 视频列表
    for v in vlist:
        aid = v['aid']  # 视频id
        url = f'https://api.bilibili.com/x/player/pagelist?aid={aid}&jsonp=jsonp'
        player = get_http_session().get(url, timeout=10)
        player = player.json()
        data = player['data']  # 弹幕列表

        get_video_comment_info(aid, name)

        if not data:
            return
        for d in data:
            try:
                get_video_barrage(d, name, aid)

            except Exception as e:
                log(traceback.format_exc(), 'error', 'gt_up_video_info.log')  # traceback.format_exc()：打印出详细错误信息
                error_str = f'name: [{name}], uid: [{uid}]'
                log(error_str, 'error', 'gt_up_video_info.log')


def base_info_task(power_json_dict_lst):
    """
    循环字典列表，远程获取up主的作品信息
    Args:
        power_json_dict_lst: json字典列表

    Returns: None

    """
    for power_json_dict in power_json_dict_lst:
        uid = power_json_dict['uid']
        name = power_json_dict['name']
        # 通过线程池去执行
        executor.submit(get_up_base_info, name, uid)


def video_info_task():
    with ThreadPoolExecutor(max_workers=10) as executor:
        while True:
            global queue
            name, uid, filepath = queue.get()
            executor.submit(gt_up_video_info, name, uid, filepath)
            queue.task_done()
            time.sleep(2)


def main():
    power_json_dict_lst = read_json('power_up_100.json')
    # base_info_task(power_json_dict_lst)

    # 获取视频弹幕和评论信息
    # gt_up_video_info('潮汕好男人', '19071708', 'up_100\\潮汕好男人\\19071708_base_info.json')

    Thread(target=base_info_task, args=(power_json_dict_lst)).start()
    Thread(target=video_info_task).start()


if __name__ == '__main__':
    main()