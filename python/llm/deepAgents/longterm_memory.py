"""
长期记忆： 演示写入本地文件系统
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
# 调用大模型时指定存储位置
result = agent.invoke({"messages": [{"role": "user", "content": "什么是 langgraph?请用中文回答。将草稿写入 /draft.txt，将最终报告保存到 /memories/report.txt"}]})


# -1 表示取列表的最后一个元素，即代理最终生成的回复消息。代理在执行过程中会产生多条消息（工具调用、工具返回、中间推理等），最后一条才是最终答案，所以用 -1 来获取。
print(result["messages"][-1].content)