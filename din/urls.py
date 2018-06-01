from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^new/$', views.myyolo_new, name='myyolo_new'),
    url(r'^(?P<slug>\w+)/$', views.my_yolo, name='my_yolo')
]