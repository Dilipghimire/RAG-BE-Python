
from fastapi import APIRouter, HTTPException
from youtube_transcript_api import  TranscriptsDisabled
from app.Utils.utils import get_transcript_internal, retrieveContent
from app.services.youtube_transcript_service import fetch_transcript
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
import os
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel
from dotenv import load_dotenv



router = APIRouter()
# Load API key from .env
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


class QuestionRequest(BaseModel):
    askQuestion: str
    videoTranscript: str
    

@router.get("/transcript/{video_id}")
async def get_transcript(video_id: str):
    try:
        return get_transcript_internal(video_id)
    
    except TranscriptsDisabled:
        raise HTTPException(status_code=404, detail="Captions are disabled for this video")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    


@router.post("/aks-question")
async def ask_questions(request:QuestionRequest):
    try:
        return retrieveContent(request.askQuestion, request.videoTranscript)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    




