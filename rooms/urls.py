from django.conf.urls import url

from . import views

app_name = 'rooms'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create/$', views.create_room, name='create_room'),
    url(r'^modify/(?P<slug>[\w-]+)$', views.modify_room, name='modify_room'),
    url(r'^delete/(?P<slug>[\w-]+)$', views.delete_room, name='delete_room'),
]
