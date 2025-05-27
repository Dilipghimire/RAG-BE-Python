from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled


def fetch_transcript (video_id: str) -> str:
    proxies = {
        "https":"http://45.12.150.82:8080",
        "https":"57.129.81.201:8080",
        }
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=["en"], proxies=proxies)
    return " ".join(chunk["text"] for chunk in transcript_list)
