from langchain_core.messages import HumanMessage, ToolMessage
from langchain_core.tools import tool
from langchain_deepseek import ChatDeepSeek
from langchain_openai import ChatOpenAI


@tool
def add(a: int, b: int) -> int:
    """Adds a and b."""
    return a + b


@tool
def multiply(a: int, b: int) -> int:
    """Multiplies a and b."""
    return a * b


tools = [add, multiply]

# 智普 支持工具调佣，但是这个例子中验证不行
# model = ChatOpenAI(model="glm-4-0520", base_url="https://open.bigmodel.cn/api/paas/v4/", api_key="98dfaa5e4b5f700ec8f91b681c570d81.Pmxa9VnBPZ5Ol7CY")
# deepseek  不支持工具调佣
# model = ChatDeepSeek(model="deepseek-chat", api_key="sk-d31136f3bc6549669a98e9be69c8ef9a")
model = ChatOpenAI(model="gpt-4o", base_url="", api_key="")

llm_with_tools = model.bind_tools(tools)

query = "What is 3 * 12? Also, what is 11 + 49?"

messages = [HumanMessage(query)]
ai_msg = llm_with_tools.invoke(messages)
messages.append(ai_msg)

# 执行工具，得到工具执行结果
for tool_call in ai_msg.tool_calls:
    selected_tool = {"add": add, "multiply": multiply}[tool_call["name"].lower()]
    tool_output = selected_tool.invoke(tool_call["args"])
    messages.append(ToolMessage(tool_output, tool_call_id=tool_call["id"]))

result = llm_with_tools.invoke(messages)

print(result)
