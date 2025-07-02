from langserve import RemoteRunnable

"""
langserve的client端
"""

"""
正常响应
"""
runnable = RemoteRunnable("http://127.0.0.1:8001/chain")
result = runnable.invoke({"language":"中文", "text": "hi"})
print(result)

"""
流式响应
"""
result2 = runnable.stream({"language":"中文", "text": "hi, my name is zhouyu"})
for i in result2:
    print(i)