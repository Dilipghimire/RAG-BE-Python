from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
import os
from langchain_core.prompts import PromptTemplate

from app.services.youtube_transcript_service import fetch_transcript

def get_transcript_internal(video_id: str):
    transcript = fetch_transcript(video_id)
    return transcript

def textSplitter(transcriptText):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    return  splitter.create_documents([transcriptText])

def embeddingsUsingOpenAI(chunks):
    embeddings = OpenAIEmbeddings(model= 'text-embedding-3-small')
    return FAISS.from_documents(chunks, embeddings)

def prompt():
    return PromptTemplate(
        template= """
        You are a helpful assistance 
        ANSWER only from provided transcript context
        If the context is insufficient, just say you don't know 
        
        {context}
        Question: {question}
        """,
        input_variables=['context', 'question']
        )

def retrieveContent(askQuestion,transcriptText ):
    chunks = textSplitter(transcriptText)
    vector_stores = embeddingsUsingOpenAI(chunks)
    retriever =  vector_stores.as_retriever(search_type="similarity", search_kwargs={"k":5})
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)
    question= askQuestion
    reterieved_docs = retriever.invoke(question)
    context_text = "\n\n".join(doc.page_content for doc in reterieved_docs)
    final_prompt = prompt().invoke({'context': context_text, 'question': question})
    answer = llm.invoke(final_prompt)

    return answer.content