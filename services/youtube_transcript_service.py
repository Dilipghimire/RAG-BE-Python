import os
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled


def fetch_transcript (video_id: str) -> str:
    proxies = {
       "http": os.getenv("PROXY"),
       "https": os.getenv("PROXY")
        }
    print('proxies', proxies)
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=["en"], proxies=proxies)
    return " ".join(chunk["text"] for chunk in transcript_list)
