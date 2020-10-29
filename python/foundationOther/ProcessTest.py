"""
演示进程
"""

from multiprocessing import Process
import time


def longtime():
    print("我是一个任务")
    time.sleep(5)


if __name__ == "__main__":
    # 开启一个进程来使用longtime()
    p = Process(target=longtime())
    p.start()
