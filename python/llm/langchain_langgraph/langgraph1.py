from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langgraph.graph import END, MessageGraph

# langchain: 链条，不封闭
# langgraph: 图，可以封闭调佣

model = ChatOpenAI(model="gpt-4o", base_url="", api_key="")

graph = MessageGraph()

graph.add_node("begin", model)
graph.add_edge("begin", END)

graph.set_entry_point("begin")

runnable = graph.compile()

result = runnable.invoke(HumanMessage("1+1等于几?"))

print(result)
