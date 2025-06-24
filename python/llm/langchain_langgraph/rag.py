from typing import Any, List

from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter, TextSplitter
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

docs = retriever.invoke("如何查看退款是否成功?")

print(docs)