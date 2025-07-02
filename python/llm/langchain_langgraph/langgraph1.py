from langchain_deepseek import ChatDeepSeek
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langgraph.graph import END, MessageGraph

# langchain: 链条，不封闭
# langgraph: 图，可以封闭调佣

# model = ChatOpenAI(model="gpt-4o", base_url="", api_key="")
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

result = runnable.invoke(HumanMessage("1+1等于几?"))

# print(result)
# [HumanMessage(content='1+1等于几?', additional_kwargs={}, response_metadata={}, id='2cf7343e-f4c8-4827-9003-41ed0056136b'), AIMessage(content='1 + 1 等于 **2**。  \n\n这是最基本的加法运算，表示将两个单独的“1”合并在一起，总和为“2”。  \n\n如果你有其他有趣的解释（比如在二进制中 1 + 1 = 10，或在某些逻辑系统中 1 + 1 = 1），可以告诉我，我会为你补充说明！ 😊', additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 73, 'prompt_tokens': 9, 'total_tokens': 82, 'completion_tokens_details': None, 'prompt_tokens_details': {'audio_tokens': None, 'cached_tokens': 0}, 'prompt_cache_hit_tokens': 0, 'prompt_cache_miss_tokens': 9}, 'model_name': 'deepseek-chat', 'system_fingerprint': 'fp_8802369eaa_prod0623_fp8_kvcache', 'finish_reason': 'stop', 'logprobs': None}, id='run-14c9374c-f058-4e40-afe5-e967c675f582-0', usage_metadata={'input_tokens': 9, 'output_tokens': 73, 'total_tokens': 82, 'input_token_details': {'cache_read': 0}, 'output_token_details': {}})]
print(result[1].content)