from django.conf.urls import patterns, url, include
from principal import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^register/$', views.register, name='register'),
                       url(r'^login/$', views.user_login, name='login'),
                       url(r'^publish/$', views.publish, name='publish'),
                       url(r'^details/$', views.user_data, name='details'),
                       url(r'^logout', views.user_logout, name='logout'),
                       url(r'^post/(?P<post_id>[\w\-]+)/$', views.posts, name='posts'),
                       url(r'^map/$', views.principalmap, name='map'),
                       url(r'^profile/$', views.profile, name='profile'),
                       url(r'^myposts/$', views.myposts, name='myposts'),
                       )
