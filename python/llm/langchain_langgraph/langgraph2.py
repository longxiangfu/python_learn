from langchain_core.messages import BaseMessage, HumanMessage
from langchain_core.tools import tool
from langchain_deepseek import ChatDeepSeek
from langchain_openai import ChatOpenAI
from langgraph.graph import END, MessageGraph
from langgraph.prebuilt import ToolNode
from typing import Literal, List



@tool
def multiply(first_number: int, second_number: int):
    """对两个数字进行相乘."""
    return first_number * second_number


# model = ChatOpenAI(model="gpt-4o", base_url="", api_key="")
# model = ChatDeepSeek(model="deepseek-chat", api_key="sk-d31136f3bc6549669a98e9be69c8ef9a")
model = ChatOpenAI(model="glm-4-0520", base_url="https://open.bigmodel.cn/api/paas/v4/", api_key="98dfaa5e4b5f700ec8f91b681c570d81.Pmxa9VnBPZ5Ol7CY")


model_with_tools = model.bind_tools([multiply])

graph = MessageGraph()

graph.add_node("begin", model_with_tools)

tool_node = ToolNode([multiply])
graph.add_node("multiply", tool_node)

graph.add_edge("multiply", END)

graph.set_entry_point("begin")


def router(state: List[BaseMessage]) -> Literal["multiply", "__end__"]:
    """
    根据状态中的工具调用决定路由。

    参数:
    state (List[BaseMessage]): 包含对话历史的消息列表。

    返回:
    Literal["multiply", "__end__"]: 如果有工具调用则返回'multiply'，否则返回'__end__'。
    """
    tool_calls = state[-1].additional_kwargs.get("tool_calls", [])
    if len(tool_calls):
        return "multiply"
    else:
        return "__end__"

# 添加条件边
graph.add_conditional_edges("begin", router)

runnable = graph.compile()

result = runnable.invoke(HumanMessage("123 * 456等于多少"))
# print(result[1].content)
print(result)
