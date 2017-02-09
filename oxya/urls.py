from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^$', views.index, name='homepage'),
    url(r'^login/$', auth_views.login, {'template_name': 'authentication/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'authentication/logout.html'}, name='logout'),
    url(r'^clients/', include('clients.urls')),
    url(r'^rooms/', include('rooms.urls')),
    #url(r'^infras/', include('infras.urls')),
    #url(r'^servers/', include('servers.urls')),
    #url(r'^networks/', include('networks.urls')),
    #url(r'^storages/', include('storages.urls')),
    url(r'^admin/', admin.site.urls),
]
