import os
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled

load_dotenv()

def fetch_transcript (video_id: str) -> str:
    proxies = {
       "http": os.getenv("PROXY"),
       "https": os.getenv("PROXY")
        }
    print('proxies', proxies)
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=["en"], proxies=proxies, timeout=10)
    return " ".join(chunk["text"] for chunk in transcript_list)
