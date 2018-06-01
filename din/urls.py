from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<id>\d+)/new/$', views.din_new, name='din_new'),
    url(r'^(?P<id>\d+)/edit/$', views.din_edit, name='din_edit'),
    url(r'^(?P<slug>\w+)/$', views.din, name='din'),
    url(r'^(?P<slug>\w+)/(?P<id>\d+)/', views.din_detail, name='din_detail')
]