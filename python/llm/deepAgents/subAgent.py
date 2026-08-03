"""
子Agent：SubAgent
"""
import os
from typing import Literal
from tavily import TavilyClient
from deepagents import create_deep_agent
from langchain.chat_models import init_chat_model

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

# 定义子代理
research_subagent = {
    "name": "research-agent",
    "description": "用于研究更深入的问题",
    "system_prompt": "你是一位出色的研究员",
    "tools": [internet_search]
}
subagents = [research_subagent]

# 创建深度代理
model = init_chat_model("deepseek-chat", model_provider="deepseek")
agent = create_deep_agent(
    model= model,
    system_prompt= "你协调数据分析和报告。使用子Agent完成专业任务。",
    subagents= subagents
)


"""
调用代理并打印结果
"""
# 直接输出最后结果
result = agent.invoke({"messages": [{"role": "user", "content": "langgraph的基本架构是什么?请用中文回答"}]})
print(result["messages"][-1].content)
