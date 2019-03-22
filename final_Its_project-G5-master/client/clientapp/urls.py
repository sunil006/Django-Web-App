from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^rend/$', views.rend, name='rend'),
    url(r'^rend1/$', views.rend1, name='rend1'),
    url(r'^home/$', views.home, name='home'),
    url(r'^map/$', views.map, name='map'),
    url(r'^mail/$', views.mail, name='mail'),
    url(r'^crop/$', views.crop, name='crop'),
    url(r'^fertilizer/$', views.fertilizer, name='fertilizer'),
    url(r'^get_name/$', views.get_name, name='get_name'),
 
]

