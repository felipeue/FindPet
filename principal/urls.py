from django.conf.urls import patterns, url, include
from principal import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^register/$', views.register, name='register'),
                       url(r'^login/$', views.user_login, name='login'),
                       url(r'^publish/$', views.publish, name='publish'),
                       )
