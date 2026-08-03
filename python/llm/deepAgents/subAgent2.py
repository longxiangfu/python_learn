"""
子Agent: CompiledSubAgent
对于更复杂的用例，你可以提供自己预构建的 LangGraph 图作为子Agent
"""

from deepagents import create_deep_agent, CompiledSubAgent
from langchain.chat_models import init_chat_model
from langchain_deepseek import ChatDeepSeek
from langgraph.graph import END, MessageGraph

# 创建一个自定义的图agent
def getGraphAgent():
    model = ChatDeepSeek(model="deepseek-chat", api_key="sk-d31136f3bc6549669a98e9be69c8ef9a")

    # 返回MessageGraph对象
    graph = MessageGraph()

    # 添加节点
    graph.add_node("begin", model)

    # 添加边
    graph.add_edge("begin", END)

    # 设置入口节点
    graph.set_entry_point("begin")

    # 返回可运行的对象：CompiledStateGraph
    runnable = graph.compile()
    return runnable

# 定义子代理
custom_subagent = CompiledSubAgent(
    name="data-analyzer",
    description="用于复杂数据分析任务的专业Agent",
    runnable= getGraphAgent(),
)
subagents = [custom_subagent]

# 创建深度代理
model = init_chat_model("deepseek-chat", model_provider="deepseek")
agent = create_deep_agent(
    model= model,
    system_prompt= "你协调数据分析和报告。使用子Agent完成专业任务。",
    subagents= subagents
)


# 调用代理并打印结果
result = agent.invoke({"messages": [{"role": "user", "content": "langgraph的基本架构是什么?请用中文回答"}]})
print(result["messages"][-1].content)
