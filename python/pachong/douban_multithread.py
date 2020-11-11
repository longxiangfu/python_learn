"""
多线程爬取豆瓣电影
"""

import os
# from fake_useragent import UserAgent # 设置请求头
import requests
from bs4 import BeautifulSoup  # 解析网页
import time
# from urllib.request import urlretrieve #
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED

download_path = 'E:\\pycharmWork\\python\\pachong\\douban'
if not os.path.exists(download_path):
    os.makedirs(download_path)


def download_pic(url):
    # ua = UserAgent()
    # assert isinstance(ua, UserAgent)
    # headers = {'User-Agent': ua.chrome}

    # 设置请求头，并请求
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'}
    r = requests.get(url, headers=headers)
    # 创建BeautifulSoup,底层解析器适用lxml
    soup = BeautifulSoup(r.text, 'lxml')
    content = soup.find('div', class_='article')
    images = content.find_all('img')
    pic_link_list = [image['src'] for image in images]
    pic_name_list = [image['alt'] for image in images]
    for link, name in zip(pic_link_list, pic_name_list):
        # urlretrieve(url, f'{download_path}/{name}.jpg') # 下载，可能对python3支持不好，下载有问题
        html = requests.get(link)
        with open(f'{download_path}/{name}.jpg', 'wb') as f:
            f.write(html.content)
    print(f'{url}所有电影图片下载完成')


def main():
    """
    主函数
    """
    start_urls = ['https://movie.douban.com/top250']
    for i in range(1, 2):
        start_urls.append(f'https://movie.douban.com/top250?start={i * 25}&filter=')
    start_time = time.time()

    with ThreadPoolExecutor(max_workers=10) as excetor:
        futures = []
        for url in start_urls:
            future = excetor.submit(download_pic, url)
            futures.append(future)
    # 等待所有线程执行完，才进行下面的逻辑。java中用CountDownLantch
    wait(futures)  # 默认 return_when=ALL_COMPLETED
    end_time = time.time()
    print('=' * 50)
    print(f'运行时间：{start_time - end_time}')


if __name__ == '__main__':
    main()
