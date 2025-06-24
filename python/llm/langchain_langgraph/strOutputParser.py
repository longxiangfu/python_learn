from langchain_core.output_parsers import StrOutputParser
from langchain_deepseek import ChatDeepSeek
from langchain_core.messages import HumanMessage, SystemMessage

model = ChatDeepSeek(model="deepseek-chat", api_key="sk-d31136f3bc6549669a98e9be69c8ef9a")

messages = [
    SystemMessage(content="翻译以下英文为中文"),
    HumanMessage(content="hi!"),
]

parser = StrOutputParser()
chain = model | parser
result = chain.invoke(messages)
print(result) #嗨！
