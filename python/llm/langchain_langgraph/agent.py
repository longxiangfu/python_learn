from datetime import datetime
from typing import Any, List

from langchain import hub
from langchain.agents import AgentExecutor
from langchain.agents import create_tool_calling_agent
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings import ZhipuAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.tools import create_retriever_tool, tool
from langchain_deepseek import ChatDeepSeek
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_text_splitters import TextSplitter
from langchain_text_splitters.character import _split_text_with_regex


class ZhouyuCharacterTextSplitter(TextSplitter):
    """Splitting text that looks at characters."""

    def __init__(
            self, separator: str = "\n\n", **kwargs: Any
    ) -> None:
        """Create a new TextSplitter."""
        super().__init__(**kwargs)
        self._separator = separator

    def split_text(self, text: str) -> List[str]:
        splits = _split_text_with_regex(text, self._separator, self._keep_separator)
        return splits


loader = TextLoader("meituan-qa.txt", encoding="utf-8")
documents = loader.load()
text_splitter = ZhouyuCharacterTextSplitter()
texts = text_splitter.split_documents(documents)
# embeddings = OpenAIEmbeddings(base_url="", api_key="")
embeddings = ZhipuAIEmbeddings(model="embedding-3", api_key="98dfaa5e4b5f700ec8f91b681c570d81.Pmxa9VnBPZ5Ol7CY")
vectorstore = FAISS.from_documents(texts, embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

# 创建检索工具
retriever_tool = create_retriever_tool(
    retriever,
    "qa_search",
    "关于任何退款的问题，你都应该使用这个工具!",
)

@tool
def today() -> datetime:
    """用来获取今天的日期."""
    return datetime.now()

# 从hub中加载公共的提示词模版  https://smith.langchain.com/hub/hwchase17/openai-functions-agent
prompt = hub.pull("hwchase17/openai-functions-agent")

# model = ChatOpenAI(model="gpt-4o", base_url="", api_key="")
model = ChatDeepSeek(model="deepseek-chat", api_key="sk-d31136f3bc6549669a98e9be69c8ef9a")

tools = [today, retriever_tool]

# 创建一个工具调用代理
agent = create_tool_calling_agent(model, tools, prompt)

# 创建一个代理执行器
agent_executor = AgentExecutor(agent=agent, tools=tools)

# 运行代理
result = agent_executor.invoke({"input": "今天的退款什么时候会到账"})

print(result)
# {'input': '今天的退款什么时候会到账', 'output': '退款通常会在一个工作日内到账至您的美团账户余额，您可以在“账号管理——我的账号”中查看是否到账。
# 如果退款是提现到支付账户，可能需要1-7个工作日到账，具体时间以银行处理为准。今天是2025年7月2日，您可以据此估算到账时间。'}
