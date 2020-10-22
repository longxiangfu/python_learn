"""
百度语音合成  利用百度sdk,也可使用api接口
"""
from aip import AipSpeech

APP_ID = '22861039'
API_KEY = 'IBRHc9BaIwpaM5zgpju9i3Fb'
SECRET_KEY = 'Yb39UQ308fzGTuB683rvUrDr9Mb5KCR6'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

s = '我是龙相甫，我的书，你看过了吗？还没有吗？不看书，不是好孩子哦'
result = client.synthesis(s, 'zh', 1, {
    'vol': 5,
    'per': 3,
    'spd': 6,
    'pit': 6
})
if not isinstance(result, dict):
    with open('audio.mp3', 'wb') as f:
        f.write(result)
else:
    print(result)
