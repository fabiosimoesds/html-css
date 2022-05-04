from pytube import YouTube

yt = YouTube(str("https://www.youtube.com/watch?v=FQC_-WAiKWw"))
video = yt.streams.filter(only_audio=True).first()
video.download()