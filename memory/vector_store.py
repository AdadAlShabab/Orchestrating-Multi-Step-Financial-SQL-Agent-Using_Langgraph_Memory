from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
import os

class VectorMemory:
    def __init__(self):
        self.embeddings = OpenAIEmbeddings()
        self.db = FAISS.load_local("memory/index", self.embeddings)

    def retrieve(self, query):
        return self.db.similarity_search(query)
