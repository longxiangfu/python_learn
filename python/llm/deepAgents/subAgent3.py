"""
子Agent：保持系统提示的详细性
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
    "description": "使用网络搜索进行深入研究并综合发现",
    "system_prompt": """
        你是一位彻底的研究员。你的工作是：
        1. 将研究问题分解为可搜索的查询
        2. 使用 internet_search 查找相关信息
        3. 将发现综合成一个全面但简洁的摘要
        4. 提出主张时引用来源
        
        输出格式：
        - 摘要（2-3段）
        - 主要发现（项目符号）
        - 来源（附带URL）
        
        保持你的回应在500字以内，以保持上下文的整洁。""",
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
