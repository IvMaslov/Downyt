from django.urls import path,include,re_path

from . import views

urlpatterns = [
	path('',views.index,name='index'),
	re_path(r'\w{,11}/\d{,4}',views.Download.as_view(),name='download'),
	re_path(r'\w{,11}',views.Videos.as_view(),name='videos'),
]