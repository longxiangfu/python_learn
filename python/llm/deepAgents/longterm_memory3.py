"""
长期记忆： 演示 存储跨会话持久存在的用户偏好
再次启动该文件，调用大模型->跨会话
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
research_instruction = """您是一位专家级研究员。您的工作是进行彻底的研究，然后撰写一份精美的报告。
您可以访问互联网搜索工具，作为收集信息的主要方式。
## `internet_search`
使用此工具对给定查询进行互联网搜索。您可以指定要返回的最大结果数、主题以及是否包含原始内容。
## 当用户告诉您他们的偏好时，请将其保存到/memories/user_preferences.txt，以便您在将来的对话中记住它们。
当用户问他的爱好的话，就去/memories/user_preferences.txt中找。
"""
# model = init_chat_model("gemma4", model_provider="ollama", base_url="http://localhost:11434")
model = init_chat_model("deepseek-chat", model_provider="deepseek")
agent = create_deep_agent(
    model = model,
    tools=[internet_search],
    system_prompt=research_instruction,
    # 本地文件持久化， 使用虚拟路径
    backend=FilesystemBackend(root_dir="D:\\workspace\\workspace-python\\python\\llm\\deepAgents", virtual_mode=True)
)

# 调用代理并打印结果
result = agent.invoke({"messages": [{"role": "user", "content": "我喜欢吃香蕉、唱歌、旅游。"}]})
print(result["messages"][-1].content)
# 已经记住了！你喜欢的三个事情：
#
# 1. 🍌 **吃香蕉**
# 2. 🎤 **唱歌**
# 3. ✈️ **旅游**


# 再次调用大模型，不用重新运行该文件
# 模型强大的话，会先去偏好文件中找；模型弱的话，需要发起新的会话
# 如果没有持久化，若要实现上下文，就需要将历史对话都发送给大模型
result = agent.invoke({"messages": [{"role": "user", "content": "我爱好什么？"}]})
print(result["messages"][-1].content)
# 根据记录，你的爱好包括：
#
# 1. **吃香蕉** 🍌
# 2. **唱歌** 🎤
# 3. **旅游** ✈️