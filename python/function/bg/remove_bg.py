"""
去除图片水印
"""

import os
from removebg import RemoveBg


# bg = RemoveBg("L878rmVDpmbeiSeBzbgdFXSq", "error.log")
# filePath = "E:\\图片"
# bg.remove_background_from_img_file(f"{filePath}\\long.JPG")

# bg = RemoveBg("L878rmVDpmbeiSeBzbgdFXSq", "error.log")
# filePath = "E:\\图片\\去水印"
# for pic in os.listdir(filePath):
#     img_path = os.path.join(filePath, pic)
#     bg.remove_background_from_img_file(img_path)
#     print(f"{img_path} is done")

def remove_bg(path):
    bg = RemoveBg("L878rmVDpmbeiSeBzbgdFXSq", "error.log")
    bg.remove_background_from_img_file(path)
