from fastapi import FastAPI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_deepseek import ChatDeepSeek
from langserve import add_routes

model = ChatDeepSeek(model="deepseek-chat", api_key="sk-d31136f3bc6549669a98e9be69c8ef9a")

prompt_template = ChatPromptTemplate.from_messages(
    [("system", "翻译以下英文为{language}:"), ("user", "{text}")]
)
# 查看模版填充结果
# result = prompt_template.invoke({"language": "中文", "text": "hi"})

parser = StrOutputParser()

chain = prompt_template | model | parser

result = chain.invoke({"language": "中文", "text": "hi"})

print(result) # 嗨



app = FastAPI()

# 添加路由规则
add_routes(
    app,
    chain,
    path="/chain",
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8001)