"""import webbrowser
url = "https://www.youtube.com/watch?v=4e5BjUACyRM"
download = url[:12] + "ss" + url[12:]
webbrowser.open(url)"""
from pytubefix import YouTube
from pytubefix import YouTube
from pytubefix.cli import on_progress

url = "https://www.youtube.com/watch?v=4e5BjUACyRM"

yt = YouTube(url, on_progress_callback=on_progress)
print(yt.title)

ys = yt.streams.get_highest_resolution()
ys.download()