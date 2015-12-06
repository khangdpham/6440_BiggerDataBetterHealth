from django.conf.urls import patterns, url
from app_hcare import views

urlpatterns = patterns('',
    url('^$', views.main, name='main'),
	url('^about/$', views.about, name='about'),
    url('process_data$', views.process_data, name='process_data'),
    url('process_data_corr$', views.process_data_corr, name='process_data_corr'),
)