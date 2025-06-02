from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings, ChatOpenAI

from Utils.utils import textSplitter


# 1. Initialize Pinecone
# Step 1: Initialize Pinecone client (v3+)
load_dotenv()
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

# # 2. Define index name
# index_name = "transcript-demo"

def insert_vector_store(index_name, chunks, transcript):
    chunks = textSplitter(transcript)
    embeddings = OpenAIEmbeddings(model= 'text-embedding-3-small')
    vector_store = PineconeVectorStore.from_documents(chunks, embeddings, index_name=index_name)
    return vector_store

    
    