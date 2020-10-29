"""
演示线程
"""

import time
import threading


def longtime():
    print("我是一个任务")
    time.sleep(2)


if __name__ == "__main__":
    # 开启一个线程来使用longtime()
    # t = threading.Thread(target=longtime, name='longtime_thread')
    # t.start()

    for i in range(10):
        t = threading.Thread(target=longtime(), name='longtime_thread_'+str(i))
        t.start()
        print(t.name)
