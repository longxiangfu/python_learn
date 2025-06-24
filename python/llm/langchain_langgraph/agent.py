from datetime import datetime
from typing import Any, List

from langchain import hub
from langchain.agents import AgentExecutor
from langchain.agents import create_tool_calling_agent
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_core.tools import create_retriever_tool, tool
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


loader = TextLoader("meituan-qa.txt")

documents = loader.load()
text_splitter = ZhouyuCharacterTextSplitter()
texts = text_splitter.split_documents(documents)
embeddings = OpenAIEmbeddings(base_url="", api_key="")
vectorstore = FAISS.from_documents(texts, embeddings)

retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

retriever_tool = create_retriever_tool(
    retriever,
    "qa_search",
    "关于任何退款的问题，你都应该使用这个工具!",
)

@tool
def today() -> datetime:
    """用来获取今天的日期."""
    return datetime.now()

prompt = hub.pull("hwchase17/openai-functions-agent")
model = ChatOpenAI(model="gpt-4o", base_url="", api_key="")
tools = [today, retriever_tool]
agent = create_tool_calling_agent(model, tools, prompt)

agent_executor = AgentExecutor(agent=agent, tools=tools)

result = agent_executor.invoke({"input": "今天的退款什么时候会到账"})

print(result)
