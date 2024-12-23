from youtube_transcript_api import YouTubeTranscriptApi
video_id = 'lZ3bPUKo5zc' 
data=YouTubeTranscriptApi.get_transcript(video_id)
print(data)