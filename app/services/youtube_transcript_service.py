from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled


def fetch_transcript (video_id: str) -> str:
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=["en"])
    return " ".join(chunk["text"] for chunk in transcript_list)
