"""
长期记忆： 演示 记录持久化的内容
在系统提示中，阐明何时使用长期存储与短期存储

# 使用清晰的、分层的路径组织长期文件
# ✅ 好的：有组织且具有描述性
/memories/user_preferences/language.txt
/memories/projects/project_alpha/status.txt
/memories/research/quantum_computing/sources.txt
# ❌ 坏的：通用且无组织
/memories/temp.txt
/memories/data.txt
/memories/file1.txt
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
您可以访问两种类型的存储：

短期（没有 /memories/ 的路径）：
- 当前对话记录
- 临时草稿
- 草稿文件

长期（以 /memories/ 开头的路径）：
- 用户偏好和设置
- 已完成的报告和文档
- 应在对话之间持久存在的知识
- 项目状态和进度

对于应在本次对话之后保留的信息，请始终使用 /memories/。

如果用户问到你认为应该被保存到 /memories/下的内容，请先去 /memories/下查找。
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
result = agent.invoke({"messages": [{"role": "user", "content": "比起睡觉，我更喜欢运动"}]})
print(result["messages"][-1].content)
# 已记录到你的偏好中。运动是个好习惯！有什么具体的运动项目是你特别喜欢的吗？


# 再次调用大模型，不用重新运行该文件
# 模型强大的话，会先去偏好文件中找；模型弱的话，需要发起新的会话
# 如果没有持久化，若要实现上下文，就需要将历史对话都发送给大模型
result = agent.invoke({"messages": [{"role": "user", "content": "睡觉和运动，我更喜欢哪一个？"}]})
print(result["messages"][-1].content)
# 根据我记录到的你的偏好信息，答案是：**你更喜欢运动**。
# 我曾在 `/memories/preferences.md` 中记录了你的运动偏好——比起睡觉，你更喜欢运动。