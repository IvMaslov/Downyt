from django.shortcuts import render

import os
from django.views.generic import TemplateView
from django.views.generic.base import View
from .yt import YT_HANDLER
from wsgiref.util import FileWrapper
import os,mimetypes
from django.http import HttpResponse,StreamingHttpResponse,FileResponse
# Create your views here.



def index(request):

	return render(request,'main.html')


class Videos(View):
	def __init__(self):
		template_name = 'videos.html'

	
	def get(self,request):
		yt_url = "https://www.youtube.com/watch?v={}".format(request.get_full_path().split("/")[2])
		self.yt_hand = YT_HANDLER(yt_url)
		self.audio_streams = self.yt_hand.audio_filter()
		self.video_streams = self.yt_hand.video_filter()
		context_dict = {"video_streams":self.video_streams,"audio_streams":self.audio_streams,"url_for_transition":f"http://localhost:5000/videos/download/{request.get_full_path().split('/')[2]}"}

		return render(request,'videos.html',context_dict)


class Download(Videos):
	def get(self,request):
		print(request.get_full_path())
		yt_url = "https://www.youtube.com/watch?v={}".format(request.get_full_path().split("/")[3])
		base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
		download_dir = base_dir + "/files/"


		self.yt_hand = YT_HANDLER(yt_url)
		self.audio_streams = self.yt_hand.audio_filter()
		self.video_streams = self.yt_hand.video_filter()
		itag = request.get_full_path().split("/")[-1]
		
		needs_stream = self.audio_streams.get_by_itag(itag)
		if not needs_stream:
			needs_stream = self.video_streams.get_by_itag(itag)

		print(needs_stream)
		filename = needs_stream.title + "." + needs_stream.mime_type.split("/")[-1]


		needs_stream.download(download_dir,filename=filename)

		return FileResponse(open(download_dir + filename,"rb"),as_attachment=True)

