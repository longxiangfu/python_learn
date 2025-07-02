from langchain_core.messages import HumanMessage, ToolMessage
from langchain_core.output_parsers import StrOutputParser
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

# 智普 支持工具调佣
# model = ChatOpenAI(model="glm-4-0520", base_url="https://open.bigmodel.cn/api/paas/v4/", api_key="98dfaa5e4b5f700ec8f91b681c570d81.Pmxa9VnBPZ5Ol7CY")
# deepseek
model = ChatDeepSeek(model="deepseek-chat", api_key="sk-d31136f3bc6549669a98e9be69c8ef9a")
# model = ChatOpenAI(model="gpt-4o", base_url="", api_key="")

# 绑定工具到会话模型
# 返回的是Runnable[LanguageModelInput, BaseMessage]：语言模型输入，返回消息
llm_with_tools = model.bind_tools(tools)

query = "What is 3 * 12? Also, what is 11 + 49?"

# 定义用户message,并收集到列表中
messages = [HumanMessage(query)]

# 调用会话模型
# invoke的输入和输出可以是任意类型
ai_msg = llm_with_tools.invoke(messages)

# 将大模型的响应放到会话列表中
messages.append(ai_msg)

# 循环执行工具
for tool_call in ai_msg.tool_calls:
    # 获取调用的工具函数
    selected_tool = {"add": add, "multiply": multiply}[tool_call["name"].lower()]
    # 调用工具
    tool_output = selected_tool.invoke(tool_call["args"])
    # 将工具的响应放到会话列表中
    messages.append(ToolMessage(tool_output, tool_call_id=tool_call["id"]))


parser = StrOutputParser()
chain = llm_with_tools | parser

# 获取大模型的最终响应
result = chain.invoke(messages)

print(result) # The result of \(3 \times 12\) is \(36\), and the result of \(11 + 49\) is \(60\).
