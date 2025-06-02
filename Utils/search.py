from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings, ChatOpenAI



# 1. Initialize Pinecone
# Step 1: Initialize Pinecone client (v3+)
load_dotenv()
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

def search_vector_store(query,index_name):
    index = pc.Index(index_name)
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    vector_store = PineconeVectorStore(
        index=index,
        embedding=embeddings
        )
    query=query
    results = vector_store.similarity_search(query, k=5)
    return results
