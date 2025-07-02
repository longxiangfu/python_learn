from typing import Any, List

from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings import ZhipuAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter, TextSplitter
from langchain_text_splitters.character import _split_text_with_regex


"""
该类 [ZhouyuCharacterTextSplitter](file://D:\workspace\workspace-python\python\llm\langchain_langgraph\rag.py#L10-L22) 继承自 `TextSplitter`，用于按指定字符（默认为两个换行符 `\n\n`）分割文本。  

- [__init__](file://D:\workspace\workspace-python\python\llm\langchain_langgraph\rag.py#L13-L18)：初始化时接收分隔符 `separator` 和其他参数，传递给父类并保存分隔符。  
- [split_text](file://D:\workspace\workspace-python\python\llm\langchain_langgraph\rag.py#L20-L22)：调用 `_split_text_with_regex` 方法，使用正则按 `self._separator` 分割文本并返回结果列表。
"""
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


# 实例化文本加载器
loader = TextLoader("meituan-qa.txt", encoding="utf-8")

# 加载文档数据
documents = loader.load()

# 实例化文本切分器
text_splitter = ZhouyuCharacterTextSplitter()

# 切分文档
texts = text_splitter.split_documents(documents)

# 实例化向量模型
# embeddings = OpenAIEmbeddings(base_url="", api_key="")
embeddings = ZhipuAIEmbeddings(model="embedding-3", api_key="98dfaa5e4b5f700ec8f91b681c570d81.Pmxa9VnBPZ5Ol7CY")

# 将切分后的文本向量化，并存储到向量数据库中
vectorstore = FAISS.from_documents(texts, embeddings)

# 创建一个向量数据库检索器，该检索器可以检索出top2个最相近的文本片段
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

# 向量检索
docs = retriever.invoke("如何查看退款是否成功?")

print(docs)
# [Document(id='71967bf2-01aa-43b6-80b6-113bbfbd9c28', metadata={'source': 'meituan-qa.txt'}, page_content='Q：怎么查看退款是否成功？\n退款会在一个工作日之内到美团账户余额，可在“账号管理——我的账号”中查看是否到账。'), Document(id='dcc844c1-3b0a-4bdd-a294-23936941a6ad', metadata={'source': 'meituan-qa.txt'}, page_content='Q：怎么取消退款呢？\n请在订单页点击“不退款了”，商家还会正常送餐的。')]
