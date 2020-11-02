"""
界面操作去除图片水印
"""

import os
from tkinter import Tk, Label, Button
from tkinter.filedialog import askopenfilenames
from tkinter.messagebox import showinfo
from removebg import RemoveBg

IMAPATH = ''


def remove_bg(path):
    bg = RemoveBg("L878rmVDpmbeiSeBzbgdFXSq", "error.log")
    bg.remove_background_from_img_file(path)


class GUI:
    def __init__(self, window):
        self.window = window
        self.window.title('去除图片背景')
        self.window.geometry('300x200')

        # 标签显示
        self.label = Label(window, text='提示内容')
        self.label.pack(padx=5, pady=10)  # 固定窗口位置

        # 选择图片按钮
        btn1 = Button(window, text='选择图片', width=15, height=2, command=self.get_img)
        btn1.pack()  # 固定窗口位置

        # 生成图片按钮
        self.send_btn = Button(window, text='去除背景', width=15, height=2, command=self.gen_img)
        self.send_btn.pack()  # 固定窗口位置

    def get_img(self):
        global IMAPATH
        # 选择文件，返回为元祖
        filenames = askopenfilenames(filetypes=(
            ("jpeg img", "*.jepg"),
            ("jpg img", "*.jpg"),
            ("png img", "*.png")
        ))
        if len(filenames) > 0:
            fnlist = [fn for fn in filenames]
            fnstr = '\n'.join(fnlist)
            self.label.config(text=fnstr)
            IMAPATH = fnlist
        else:
            self.label.config(text='目前没有选择任何图片文件')

    def gen_img(self):
        global IMAPATH
        respathlist = []
        for imgpath in IMAPATH:
            filepath, tempfilename = os.path.split(imgpath)  # 分别为文件路径（不包含文件名和类型）和文件名+扩展名
            filename, extenion = os.path.splitext(tempfilename)  # 分别为文件名和扩展名
            remove_bg(imgpath)
            respathlist.append(imgpath)
        respath = ' '.join(respathlist)
        showinfo('完成任务', f"图片处理完成，路径为：{respath}")  # 弹出窗口


if __name__ == '__main__':
    # 创建窗口
    window = Tk()
    # 在窗口中进行操作
    GUI(window)
    # 显示窗口，必须再所有控件后
    window.mainloop()
