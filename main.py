from fastapi import FastAPI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from fastapi.middleware.cors import CORSMiddleware



from api import  transcript
from api.login import login 




app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins= "[*]",  # Or use ["*"] to allow all (not recommended for production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include your routers
app.include_router(transcript.router)
app.include_router(login.router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
