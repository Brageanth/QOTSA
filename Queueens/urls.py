from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.home),
	url(r'^gracias/$', views.gracias,  name='gracias'),
	url(r'^csv/$', views.exportCsv)
]