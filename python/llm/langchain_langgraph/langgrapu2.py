from langchain_core.messages import BaseMessage, HumanMessage
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langgraph.graph import END, MessageGraph
from langgraph.prebuilt import ToolNode
from typing import Literal, List



@tool
def multiply(first_number: int, second_number: int):
    """对两个数字进行相乘."""
    return first_number * second_number


model = ChatOpenAI(model="gpt-4o", base_url="", api_key="")
model_with_tools = model.bind_tools([multiply])

builder = MessageGraph()

builder.add_node("begin", model_with_tools)

tool_node = ToolNode([multiply])
builder.add_node("multiply", tool_node)

builder.add_edge("multiply", END)

builder.set_entry_point("begin")


def router(state: List[BaseMessage]) -> Literal["multiply", "__end__"]:
    tool_calls = state[-1].additional_kwargs.get("tool_calls", [])
    if len(tool_calls):
        return "multiply"
    else:
        return "__end__"


builder.add_conditional_edges("begin", router)

runnable = builder.compile()

result = runnable.invoke(HumanMessage("123 * 456等于多少"))
print(result)
