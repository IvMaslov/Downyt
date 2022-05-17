
from pytube import YouTube  

class YT_HANDLER():
	def __init__(self,url):
		self.url = url
		self.YT = YouTube(url)
		self.YT_streams = self.YT.streams

	def audio_filter(self):
		"""
		[itag + mime_type + abr + audio_codec]

		"""
		audio_streams = self.YT_streams.filter(type='audio')

		audio_processed_streams = []
		for i,stream in enumerate(audio_streams):
			audio_processed_streams.append([])
			audio_processed_streams[i].append(stream.itag)
			audio_processed_streams[i].append(stream.mime_type)
			audio_processed_streams[i].append(stream.abr)
			audio_processed_streams[i].append(stream.audio_codec)

		for stream in audio_streams:
			stream.mime_type = stream.mime_type.split("/")[-1]

		return audio_streams

	def video_filter(self):
		video_streams = self.YT_streams.filter(type='video',progressive=True)

		for stream in video_streams:
			stream.mime_type = stream.mime_type.split("/")[-1]
		return video_streams



		

# y = YT_HANDLER("https://www.youtube.com/watch?v=AqdAtTu8Aes")
