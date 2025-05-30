import os
from dotenv import load_dotenv
import requests
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled

load_dotenv()
SCRAPER_API_KEY = os.getenv("SCRAPER_API_KEY")

def fetch_transcript (video_id: str) -> str:
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=["en"])
    for entry in transcript:
        print(f"{entry['text']}")
    return " ".join(chunk["text"] for chunk in transcript)