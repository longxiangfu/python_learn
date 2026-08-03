"""
长期记忆： 演示 自我完善
"""

import os
from typing import Literal

from deepagents import create_deep_agent
from langchain.chat_models import init_chat_model
from tavily import TavilyClient
from deepagents.backends import FilesystemBackend

# 初始化Tavily客户端
tavily_client = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])

# 定义互联网搜索函数
def internet_search(
        query: str,
        max_results: int = 5,
        topic: Literal["general", "news", "finance"] = "general",
        include_raw_content: bool = False
):
    """
    互联网搜索函数
    Args:
        query: 搜索内容
        max_results: 返回的最大结果数
        topic: 主题
        include_raw_content: 是否包含原始内容

    Returns:

    """
    return tavily_client.search(
        query=query,
        max_results=max_results,
        topic=topic,
        include_raw_content=include_raw_content
    )

# 创建深度代理
# 自定义系统提示词
research_instruction = """
您在 /memories/instructions.txt 有一个包含其他说明和偏好的文件。
在对话开始时阅读此文件以了解用户的偏好。
当用户提供诸如“请总是执行 X”或“我更喜欢 Y”之类的反馈时，使用 edit_file 工具更新 /memories/instructions.txt。
当用户问他的偏好的话，就去/memories/instructions.txt中找。
"""
# model = init_chat_model("gemma4", model_provider="ollama", base_url="http://localhost:11434")
model = init_chat_model("deepseek-v4-flash", model_provider="deepseek")
agent = create_deep_agent(
    model = model,
    tools=[internet_search],
    system_prompt=research_instruction,
    # 本地文件持久化， 使用虚拟路径
    backend=FilesystemBackend(root_dir="D:\\workspace\\workspace-python\\python\\llm\\deepAgents", virtual_mode=True)
)

# 调用代理并打印结果
result = agent.invoke({"messages": [{"role": "user", "content": "比起吃苹果，我更喜欢吃香蕉"}]})
print(result["messages"][-1].content)
# 已经记住了，你比吃苹果更喜欢吃香蕉。


# 再次调用大模型，不用重新运行该文件
# 模型强大的话，会先去偏好文件中找；模型弱的话，需要发起新的会话
# 如果没有持久化，若要实现上下文，就需要将历史对话都发送给大模型
result = agent.invoke({"messages": [{"role": "user", "content": "苹果和香蕉，我更喜欢吃哪一个？"}]})
print(result["messages"][-1].content)
# 根据记录，你**更喜欢香蕉**，相比苹果而言。