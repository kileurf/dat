from django.conf.urls import url

from . import views

app_name = 'clients'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create/$', views.create_client, name='create_client'),
    url(r'^modify/(?P<slug>[\w-]+)$', views.modify_client, name='modify_client'),
    url(r'^delete/(?P<slug>[\w-]+)$', views.delete_client, name='delete_client'),
]
